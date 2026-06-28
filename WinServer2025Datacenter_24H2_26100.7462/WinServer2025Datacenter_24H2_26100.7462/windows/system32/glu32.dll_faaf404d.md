# Binary Specification: glu32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\glu32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `faaf404d90bc761c61cad6c6d7188c6e0b1d1996af2fbac0b39b5feb8ee0e159`
* **Total Exported Functions:** 52

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `gluBeginCurve` | `0x19E0` | 21 | UnwindData |  |
| 3 | `gluBeginSurface` | `0x1A00` | 21 | UnwindData |  |
| 4 | `gluBeginTrim` | `0x1A20` | 113 | UnwindData |  |
| 8 | `gluDeleteNurbsRenderer` | `0x1AA0` | 62 | UnwindData |  |
| 12 | `gluEndCurve` | `0x1AF0` | 56 | UnwindData |  |
| 14 | `gluEndSurface` | `0x1B30` | 56 | UnwindData |  |
| 15 | `gluEndTrim` | `0x1B70` | 56 | UnwindData |  |
| 18 | `gluGetNurbsProperty` | `0x1BB0` | 284 | UnwindData |  |
| 21 | `gluLoadSamplingMatrices` | `0x1CE0` | 121 | UnwindData |  |
| 23 | `gluNewNurbsRenderer` | `0x1D60` | 45 | UnwindData |  |
| 27 | `gluNurbsCallback` | `0x1DA0` | 54 | UnwindData |  |
| 28 | `gluNurbsCurve` | `0x1DE0` | 420 | UnwindData |  |
| 29 | `gluNurbsProperty` | `0x1F90` | 900 | UnwindData |  |
| 30 | `gluNurbsSurface` | `0x2320` | 492 | UnwindData |  |
| 36 | `gluPwlCurve` | `0x2520` | 452 | UnwindData |  |
| 2 | `gluBeginPolygon` | `0x3830` | 29 | UnwindData |  |
| 10 | `gluDeleteTess` | `0x3860` | 41 | UnwindData |  |
| 13 | `gluEndPolygon` | `0x3890` | 27 | UnwindData |  |
| 20 | `gluGetTessProperty` | `0x38C0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `gluNewTess` | `0x3940` | 249 | UnwindData |  |
| 26 | `gluNextContour` | `0x3A40` | 27 | UnwindData |  |
| 44 | `gluTessBeginContour` | `0x3A70` | 58 | UnwindData |  |
| 45 | `gluTessBeginPolygon` | `0x3AB0` | 72 | UnwindData |  |
| 46 | `gluTessCallback` | `0x3B00` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `gluTessEndContour` | `0x3CD0` | 36 | UnwindData |  |
| 48 | `gluTessEndPolygon` | `0x3D00` | 482 | UnwindData |  |
| 49 | `gluTessNormal` | `0x3EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `gluTessProperty` | `0x3F10` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `gluTessVertex` | `0x3FF0` | 323 | UnwindData |  |
| 5 | `gluBuild1DMipmaps` | `0x9000` | 1,160 | UnwindData |  |
| 6 | `gluBuild2DMipmaps` | `0x9490` | 1,320 | UnwindData |  |
| 42 | `gluScaleImage` | `0x99C0` | 661 | UnwindData |  |
| 7 | `gluCylinder` | `0xA360` | 3,086 | UnwindData |  |
| 9 | `gluDeleteQuadric` | `0xAF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `gluDisk` | `0xAFA0` | 46 | UnwindData |  |
| 24 | `gluNewQuadric` | `0xAFE0` | 54 | UnwindData |  |
| 32 | `gluPartialDisk` | `0xB020` | 3,333 | UnwindData |  |
| 37 | `gluQuadricCallback` | `0xBD30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `gluQuadricDrawStyle` | `0xBD60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `gluQuadricNormals` | `0xBDA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `gluQuadricOrientation` | `0xBDD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `gluQuadricTexture` | `0xBE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `gluSphere` | `0xBE10` | 4,224 | UnwindData |  |
| 16 | `gluErrorString` | `0xCEA0` | 171 | UnwindData |  |
| 17 | `gluErrorUnicodeStringEXT` | `0xCF60` | 168 | UnwindData |  |
| 19 | `gluGetString` | `0xD440` | 116 | UnwindData |  |
| 22 | `gluLookAt` | `0xD7C0` | 610 | UnwindData |  |
| 31 | `gluOrtho2D` | `0xDA30` | 34 | UnwindData |  |
| 33 | `gluPerspective` | `0xDA60` | 406 | UnwindData |  |
| 34 | `gluPickMatrix` | `0xDC00` | 211 | UnwindData |  |
| 35 | `gluProject` | `0xDCE0` | 258 | UnwindData |  |
| 52 | `gluUnProject` | `0xDDF0` | 467 | UnwindData |  |
