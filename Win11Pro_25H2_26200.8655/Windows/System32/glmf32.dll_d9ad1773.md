# Binary Specification: glmf32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\glmf32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d9ad1773e13adf739f05e846b919fbe618d1e37d0531a7dc2dd5732c133675d1`
* **Total Exported Functions:** 134

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `glsAppRef` | `0x40210` | 67 | UnwindData |  |
| 9 | `glsBeginGLS` | `0x40260` | 65 | UnwindData |  |
| 10 | `glsBeginObj` | `0x402B0` | 54 | UnwindData |  |
| 12 | `glsBlock` | `0x402F0` | 52 | UnwindData |  |
| 15 | `glsCallStream` | `0x40330` | 59 | UnwindData |  |
| 19 | `glsCharubz` | `0x40380` | 69 | UnwindData |  |
| 23 | `glsComment` | `0x403D0` | 54 | UnwindData |  |
| 30 | `glsDisplayMapfv` | `0x40410` | 97 | UnwindData |  |
| 32 | `glsEndGLS` | `0x40480` | 45 | UnwindData |  |
| 33 | `glsEndObj` | `0x404C0` | 45 | UnwindData |  |
| 35 | `glsError` | `0x40500` | 65 | UnwindData |  |
| 37 | `glsGLRC` | `0x40550` | 52 | UnwindData |  |
| 38 | `glsGLRCLayer` | `0x40590` | 81 | UnwindData |  |
| 74 | `glsHeaderGLRCi` | `0x405F0` | 81 | UnwindData |  |
| 75 | `glsHeaderLayerf` | `0x40650` | 81 | UnwindData |  |
| 76 | `glsHeaderLayeri` | `0x406B0` | 81 | UnwindData |  |
| 77 | `glsHeaderf` | `0x40710` | 68 | UnwindData |  |
| 78 | `glsHeaderfv` | `0x40760` | 67 | UnwindData |  |
| 79 | `glsHeaderi` | `0x407B0` | 65 | UnwindData |  |
| 80 | `glsHeaderiv` | `0x40800` | 67 | UnwindData |  |
| 81 | `glsHeaderubz` | `0x40850` | 67 | UnwindData |  |
| 90 | `glsNumb` | `0x408A0` | 67 | UnwindData |  |
| 91 | `glsNumbv` | `0x408F0` | 83 | UnwindData |  |
| 92 | `glsNumd` | `0x40950` | 70 | UnwindData |  |
| 93 | `glsNumdv` | `0x409A0` | 83 | UnwindData |  |
| 94 | `glsNumf` | `0x40A00` | 70 | UnwindData |  |
| 95 | `glsNumfv` | `0x40A50` | 83 | UnwindData |  |
| 96 | `glsNumi` | `0x40AB0` | 67 | UnwindData |  |
| 97 | `glsNumiv` | `0x40B00` | 83 | UnwindData |  |
| 98 | `glsNuml` | `0x40B60` | 69 | UnwindData |  |
| 99 | `glsNumlv` | `0x40BB0` | 83 | UnwindData |  |
| 100 | `glsNums` | `0x40C10` | 69 | UnwindData |  |
| 101 | `glsNumsv` | `0x40C60` | 83 | UnwindData |  |
| 102 | `glsNumub` | `0x40CC0` | 67 | UnwindData |  |
| 103 | `glsNumubv` | `0x40D10` | 83 | UnwindData |  |
| 104 | `glsNumui` | `0x40D70` | 67 | UnwindData |  |
| 105 | `glsNumuiv` | `0x40DC0` | 83 | UnwindData |  |
| 106 | `glsNumul` | `0x40E20` | 69 | UnwindData |  |
| 107 | `glsNumulv` | `0x40E70` | 83 | UnwindData |  |
| 108 | `glsNumus` | `0x40ED0` | 69 | UnwindData |  |
| 109 | `glsNumusv` | `0x40F20` | 83 | UnwindData |  |
| 110 | `glsPad` | `0x40F80` | 45 | UnwindData |  |
| 115 | `glsRequireExtension` | `0x40FC0` | 54 | UnwindData |  |
| 116 | `glsSwapBuffers` | `0x41000` | 52 | UnwindData |  |
| 131 | `glsUnsupportedCommand` | `0x41040` | 45 | UnwindData |  |
| 11 | `glsBinary` | `0x41080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `glsCommandAPI` | `0x410A0` | 71 | UnwindData |  |
| 22 | `glsCommandString` | `0x410F0` | 48 | UnwindData |  |
| 24 | `glsContext` | `0x41130` | 419 | UnwindData |  |
| 27 | `glsDeleteContext` | `0x412E0` | 316 | UnwindData |  |
| 34 | `glsEnumString` | `0x41430` | 170 | UnwindData |  |
| 39 | `glsGenContext` | `0x414E0` | 206 | UnwindData |  |
| 40 | `glsGetAllContexts` | `0x415C0` | 166 | UnwindData |  |
| 44 | `glsGetCommandAlignment` | `0x41670` | 184 | UnwindData |  |
| 45 | `glsGetCommandAttrib` | `0x41730` | 50 | UnwindData |  |
| 47 | `glsGetConsti` | `0x41770` | 110 | UnwindData |  |
| 48 | `glsGetConstiv` | `0x417F0` | 74 | UnwindData |  |
| 49 | `glsGetConstubz` | `0x41840` | 116 | UnwindData |  |
| 56 | `glsGetCurrentContext` | `0x418C0` | 61 | UnwindData |  |
| 57 | `glsGetCurrentTime` | `0x41910` | 265 | UnwindData |  |
| 58 | `glsGetError` | `0x41A20` | 71 | UnwindData |  |
| 67 | `glsGetOpcodeCount` | `0x41A70` | 81 | UnwindData |  |
| 68 | `glsGetOpcodes` | `0x41AD0` | 85 | UnwindData |  |
| 82 | `glsIsContext` | `0x41B30` | 76 | UnwindData |  |
| 84 | `glsIsExtensionSupported` | `0x41B90` | 176 | UnwindData |  |
| 85 | `glsIsUTF8String` | `0x41C50` | 70 | UnwindData |  |
| 86 | `glsLong` | `0x41CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `glsLongHigh` | `0x41CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `glsLongLow` | `0x41CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `glsULongLow` | `0x41CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `glsPixelSetup` | `0x41CE0` | 18 | UnwindData |  |
| 117 | `glsUCS1toUTF8z` | `0x41D00` | 109 | UnwindData |  |
| 118 | `glsUCS2toUTF8z` | `0x41D80` | 123 | UnwindData |  |
| 119 | `glsUCS4toUTF8` | `0x41E10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `glsUCS4toUTF8z` | `0x41E70` | 149 | UnwindData |  |
| 121 | `glsUCStoUTF8z` | `0x41F10` | 135 | UnwindData |  |
| 122 | `glsULong` | `0x41FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `glsULongHigh` | `0x41FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `glsUTF8toUCS1z` | `0x41FD0` | 118 | UnwindData |  |
| 126 | `glsUTF8toUCS2z` | `0x42050` | 131 | UnwindData |  |
| 127 | `glsUTF8toUCS4` | `0x420E0` | 105 | UnwindData |  |
| 128 | `glsUTF8toUCS4z` | `0x42150` | 112 | UnwindData |  |
| 129 | `glsUTF8toUCSz` | `0x421D0` | 135 | UnwindData |  |
| 3 | `__glsString_appendChar` | `0x43590` | 96 | UnwindData |  |
| 4 | `__glsString_assign` | `0x43600` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `__glsString_init` | `0x43650` | 3,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `glsAbortCall` | `0x442E0` | 52 | UnwindData |  |
| 8 | `glsBeginCapture` | `0x44320` | 368 | UnwindData |  |
| 13 | `glsCallArray` | `0x444A0` | 75 | UnwindData |  |
| 14 | `glsCallArrayInContext` | `0x44500` | 373 | UnwindData |  |
| 16 | `glsCaptureFlags` | `0x44680` | 99 | UnwindData |  |
| 17 | `glsCaptureFunc` | `0x446F0` | 139 | UnwindData |  |
| 18 | `glsChannel` | `0x44790` | 145 | UnwindData |  |
| 21 | `glsCommandFunc` | `0x44830` | 145 | UnwindData |  |
| 25 | `glsCopyStream` | `0x448D0` | 769 | UnwindData |  |
| 26 | `glsDataPointer` | `0x44BE0` | 50 | UnwindData |  |
| 28 | `glsDeleteReadPrefix` | `0x44C20` | 164 | UnwindData |  |
| 29 | `glsDeleteStream` | `0x44CD0` | 320 | UnwindData |  |
| 31 | `glsEndCapture` | `0x44E20` | 176 | UnwindData |  |
| 36 | `glsFlush` | `0x44EE0` | 179 | UnwindData |  |
| 43 | `glsGetCaptureFlags` | `0x44FA0` | 71 | UnwindData |  |
| 46 | `glsGetCommandFunc` | `0x44FF0` | 74 | UnwindData |  |
| 50 | `glsGetContextFunc` | `0x45040` | 167 | UnwindData |  |
| 51 | `glsGetContextListl` | `0x450F0` | 168 | UnwindData |  |
| 52 | `glsGetContextListubz` | `0x451A0` | 285 | UnwindData |  |
| 53 | `glsGetContextPointer` | `0x452D0` | 145 | UnwindData |  |
| 54 | `glsGetContexti` | `0x45370` | 275 | UnwindData |  |
| 55 | `glsGetContextubz` | `0x45490` | 166 | UnwindData |  |
| 59 | `glsGetGLRCi` | `0x45540` | 208 | UnwindData |  |
| 60 | `glsGetHeaderf` | `0x45620` | 167 | UnwindData |  |
| 61 | `glsGetHeaderfv` | `0x456D0` | 494 | UnwindData |  |
| 62 | `glsGetHeaderi` | `0x458D0` | 171 | UnwindData |  |
| 63 | `glsGetHeaderiv` | `0x45990` | 196 | UnwindData |  |
| 64 | `glsGetHeaderubz` | `0x45A60` | 265 | UnwindData |  |
| 65 | `glsGetLayerf` | `0x45B70` | 185 | UnwindData |  |
| 66 | `glsGetLayeri` | `0x45C30` | 464 | UnwindData |  |
| 69 | `glsGetStreamAttrib` | `0x45E10` | 131 | UnwindData |  |
| 70 | `glsGetStreamCRC32` | `0x45EA0` | 339 | UnwindData |  |
| 71 | `glsGetStreamReadName` | `0x46000` | 261 | UnwindData |  |
| 72 | `glsGetStreamSize` | `0x46110` | 396 | UnwindData |  |
| 73 | `glsGetStreamType` | `0x462B0` | 271 | UnwindData |  |
| 83 | `glsIsContextStream` | `0x463D0` | 80 | UnwindData |  |
| 112 | `glsPixelSetupGen` | `0x46430` | 42 | UnwindData |  |
| 113 | `glsReadFunc` | `0x46460` | 50 | UnwindData |  |
| 114 | `glsReadPrefix` | `0x464A0` | 314 | UnwindData |  |
| 130 | `glsUnreadFunc` | `0x465E0` | 50 | UnwindData |  |
| 133 | `glsWriteFunc` | `0x46620` | 50 | UnwindData |  |
| 134 | `glsWritePrefix` | `0x46660` | 81 | UnwindData |  |
| 1 | `__glsParser_create` | `0x46800` | 934 | UnwindData |  |
| 2 | `__glsParser_print` | `0x46C60` | 93 | UnwindData |  |
| 41 | `glsGetCaptureDispatchTable` | `0x4F2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `glsGetCaptureExecTable` | `0x4F2E0` | 78 | UnwindData |  |
| 89 | `glsNullCommandFunc` | `0x4F340` | 48 | UnwindData |  |
| 132 | `glsUpdateCaptureExecTable` | `0x4F380` | 230 | UnwindData |  |
