{
  "targets": [
    {
      "target_name": "scs3reader_addon",
      "sources": [
	      "scs3reader_addon.cc",
	      "seismogram.cc",
	      "seismogramimpl.cc"
      ],
      "cflags" : [ "-std=c++11"],
      'conditions': [
        [ 'OS!="win"', {
          "cflags+": [ "-std=c++11" ],
          "cflags_c+": [ "-std=c++11" ],
          "cflags_cc+": [ "-std=c++11" ],
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'OTHER_CPLUSPLUSFLAGS' : ['-std=c++11','-stdlib=libc++'],
            'OTHER_LDFLAGS': ['-stdlib=libc++'],
            'MACOSX_DEPLOYMENT_TARGET': '10.10'
          }
        }]
      ]
    }
  ]
}
