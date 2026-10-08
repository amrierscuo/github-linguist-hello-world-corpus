{
  "patcher": {
    "fileversion": 1,
    "appversion": {
      "major": 8,
      "minor": 6,
      "revision": 4,
      "architecture": "x64",
      "modernui": 1
    },
    "classnamespace": "box",
    "rect": [
      0.0,
      0.0,
      400.0,
      200.0
    ],
    "boxes": [
      {
        "box": {
          "id": "obj-1",
          "maxclass": "message",
          "text": "Hello\\, World!",
          "numinlets": 2,
          "numoutlets": 1,
          "outlettype": [
            ""
          ],
          "patching_rect": [
            40.0,
            40.0,
            120.0,
            22.0
          ]
        }
      },
      {
        "box": {
          "id": "obj-2",
          "maxclass": "newobj",
          "text": "print greeting",
          "numinlets": 1,
          "numoutlets": 0,
          "patching_rect": [
            40.0,
            100.0,
            100.0,
            22.0
          ]
        }
      }
    ],
    "lines": [
      {
        "patchline": {
          "source": [
            "obj-1",
            0
          ],
          "destination": [
            "obj-2",
            0
          ]
        }
      }
    ]
  }
}
