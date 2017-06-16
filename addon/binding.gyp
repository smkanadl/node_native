{
  "targets": [
    {
      "target_name": "hello",
      "sources": [ "hello.cpp" ],
      "include_dirs": ["<!@(node -p \"require('node-addon-api').include\")"],
      "dependencies": ["<!(node -p \"require('node-addon-api').gyp\")"],
      "defines": [ "NAPI_CPP_EXCEPTIONS" ],
      'cflags': [ '-std=c++14', '-fexceptions' ],
      'cflags_cc': [ '-std=c++14', '-fexceptions' ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7',
      },
      'msvs_settings': {
        'VCCLCompilerTool': {
          'ExceptionHandling': 1,
          'AdditionalOptions': [ '/EHsc' ]
        },
      }
    }
  ]
}
