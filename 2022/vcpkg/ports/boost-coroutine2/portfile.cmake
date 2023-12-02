# Automatically generated by scripts/boost/generate-ports.ps1

vcpkg_from_github(
    OUT_SOURCE_PATH SOURCE_PATH
    REPO boostorg/coroutine2
    REF boost-1.80.0
    SHA512 5a0ea6f9e69373edb52b83e6efeb552fc0d211e2316c65d3506ad3dd5f547a9025a14924615df35e790c9d351a0c6a5269c31ab961eadcf019f25f5e739b5bc0
    HEAD_REF master
)

include(${CURRENT_INSTALLED_DIR}/share/boost-vcpkg-helpers/boost-modular-headers.cmake)
boost_modular_headers(SOURCE_PATH ${SOURCE_PATH})