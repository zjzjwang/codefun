cmake_minimum_required(VERSION 3.10)
project(code)

set(CMAKE_CXX_STANDARD 17)

add_compile_definitions(INPUT)

# 递归地获取当前文件夹及其子文件夹中的所有cpp文件路径
file(GLOB_RECURSE SOURCE_FILES "*.cc")

# 设置可执行文件输出目录
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

# 遍历每个cpp文件
foreach (source_file ${SOURCE_FILES})
    # 获取cpp文件的相对路径
    file(RELATIVE_PATH relative_path ${PROJECT_SOURCE_DIR} ${source_file})

    # 获取cpp文件的文件名（不包含扩展名）
    get_filename_component(file_name ${relative_path} NAME_WE)

    # 创建子目录
    get_filename_component(dir ${relative_path} DIRECTORY)
    string(REPLACE "/" "\\" dir ${dir})
    set(output_dir "${EXECUTABLE_OUTPUT_PATH}/${dir}")
    file(MAKE_DIRECTORY ${output_dir})

    # 添加可执行文件，并设置输出路径
    add_executable(${file_name} ${source_file})
    set_target_properties(${file_name} PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${output_dir})

    # 将复制in.txt文件的命令添加到自定义命令中
    add_custom_command(TARGET ${file_name} POST_BUILD
            COMMAND ${CMAKE_COMMAND} -E copy_if_different
            ${CMAKE_CURRENT_SOURCE_DIR}/in.txt
            ${output_dir}/in.txt)

    # 将可执行文件路径添加到变量中
    list(APPEND EXECUTABLE_PATHS ${output_dir}/${file_name})
endforeach ()

# 创建自定义目标，用于一次性复制所有in.txt文件
add_custom_target(CopyInFiles ALL
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        ${CMAKE_CURRENT_SOURCE_DIR}/in.txt
        ${EXECUTABLE_PATHS}
        COMMENT "Copying in.txt to executable directories")

