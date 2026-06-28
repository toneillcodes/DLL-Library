# Binary Specification: win32ui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\oobe\win32ui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6a95ba227194223163dfd362f12a242d83e1e1cbecc50a10d370ec7c0418b347`
* **Total Exported Functions:** 884

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 20 | `??0?$CSimpleStringT@G$0A@@ATL@@QEAA@PEAUIAtlStringMgr@1@@Z` | `0x81F0` | 57 | UnwindData |  |
| 39 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@XZ` | `0x8230` | 58 | UnwindData |  |
| 43 | `??0ConfigInfo@@QEAA@XZ` | `0x8280` | 136 | UnwindData |  |
| 48 | `??0DCWarningData@@QEAA@XZ` | `0x8310` | 63 | UnwindData |  |
| 17 | `??0?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEAA@XZ` | `0x8360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??0DiskConfig@@QEAA@XZ` | `0x8360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `??0DiskConfigInfo@@QEAA@XZ` | `0x8380` | 149 | UnwindData |  |
| 74 | `??0GenericWin32UIBase@@QEAA@$$QEAV0@@Z` | `0x8420` | 41 | UnwindData |  |
| 75 | `??0GenericWin32UIBase@@QEAA@AEBV0@@Z` | `0x8450` | 41 | UnwindData |  |
| 76 | `??0GenericWin32UIBase@@QEAA@XZ` | `0x8480` | 41 | UnwindData |  |
| 92 | `??0PantherCallback@@QEAA@AEBV0@@Z` | `0x84B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `??0PantherRMEHandler@@QEAA@$$QEAV0@@Z` | `0x8500` | 41 | UnwindData |  |
| 95 | `??0PantherRMEHandler@@QEAA@AEBV0@@Z` | `0x8530` | 41 | UnwindData |  |
| 96 | `??0PantherRMEHandler@@QEAA@XZ` | `0x8560` | 41 | UnwindData |  |
| 97 | `??0PartConfigInfo@@QEAA@XZ` | `0x8590` | 222 | UnwindData |  |
| 105 | `??0SetupCreateProgressWnd@@QEAA@$$QEAV0@@Z` | `0x8680` | 41 | UnwindData |  |
| 106 | `??0SetupCreateProgressWnd@@QEAA@AEBV0@@Z` | `0x8680` | 41 | UnwindData |  |
| 107 | `??0SetupCreateProgressWnd@@QEAA@XZ` | `0x86B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `??0WDSUIAppBase@@QEAA@$$QEAV0@@Z` | `0x86D0` | 41 | UnwindData |  |
| 125 | `??0WDSUIAppBase@@QEAA@AEBV0@@Z` | `0x8700` | 41 | UnwindData |  |
| 126 | `??0WDSUIAppBase@@QEAA@XZ` | `0x8730` | 41 | UnwindData |  |
| 133 | `??0Win32UiAppBase@@QEAA@$$QEAV0@@Z` | `0x8760` | 41 | UnwindData |  |
| 134 | `??0Win32UiAppBase@@QEAA@AEBV0@@Z` | `0x8790` | 41 | UnwindData |  |
| 135 | `??0Win32UiAppBase@@QEAA@XZ` | `0x87C0` | 41 | UnwindData |  |
| 156 | `??1?$CSimpleStringT@G$0A@@ATL@@QEAA@XZ` | `0x87F0` | 45 | UnwindData |  |
| 157 | `??1?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@XZ` | `0x87F0` | 45 | UnwindData |  |
| 162 | `??1DiskConfig@@QEAA@XZ` | `0x8940` | 20 | UnwindData |  |
| 181 | `??1SetupCreateProgressWnd@@UEAA@XZ` | `0x8960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `??4?$CSimpleStringT@G$0A@@ATL@@QEAAAEAV01@AEBV01@@Z` | `0x8980` | 131 | UnwindData |  |
| 204 | `??4?$CSimpleStringT@G$0A@@ATL@@QEAAAEAV01@AEBV?$CSimpleStringT@G$00@1@@Z` | `0x8980` | 131 | UnwindData |  |
| 207 | `??4?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@AEBV01@@Z` | `0x8A10` | 24 | UnwindData |  |
| 215 | `??4ConfigInfo@@QEAAAEAV0@$$QEAV0@@Z` | `0x8A30` | 309 | UnwindData |  |
| 216 | `??4ConfigInfo@@QEAAAEAV0@AEBV0@@Z` | `0x8B70` | 30 | UnwindData |  |
| 219 | `??4DCWarningData@@QEAAAEAV0@$$QEAV0@@Z` | `0x8BA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `??4DCWarningData@@QEAAAEAV0@AEBV0@@Z` | `0x8BF0` | 30 | UnwindData |  |
| 225 | `??4DiskConfig@@QEAAAEAV0@AEBV0@@Z` | `0x8C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `??4DiskConfigInfo@@QEAAAEAV0@$$QEAV0@@Z` | `0x8C40` | 68 | UnwindData |  |
| 229 | `??4DiskConfigInfo@@QEAAAEAV0@AEBV0@@Z` | `0x8C90` | 30 | UnwindData |  |
| 237 | `??4GenericWin32UIBase@@QEAAAEAV0@$$QEAV0@@Z` | `0x8CC0` | 31 | UnwindData |  |
| 270 | `??4WDSUIAppBase@@QEAAAEAV0@$$QEAV0@@Z` | `0x8CC0` | 31 | UnwindData |  |
| 275 | `??4Win32UiAppBase@@QEAAAEAV0@$$QEAV0@@Z` | `0x8CC0` | 31 | UnwindData |  |
| 277 | `??4Win32UiDeprecateDialogBase@@QEAAAEAV0@$$QEAV0@@Z` | `0x8CC0` | 31 | UnwindData |  |
| 282 | `??4Win32UiWelcomeDialogBase@@QEAAAEAV0@$$QEAV0@@Z` | `0x8CC0` | 31 | UnwindData |  |
| 238 | `??4GenericWin32UIBase@@QEAAAEAV0@AEBV0@@Z` | `0x8CF0` | 31 | UnwindData |  |
| 239 | `??4HWRequirementsDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x8CF0` | 31 | UnwindData |  |
| 261 | `??4WDSDeprecateDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x8CF0` | 31 | UnwindData |  |
| 271 | `??4WDSUIAppBase@@QEAAAEAV0@AEBV0@@Z` | `0x8CF0` | 31 | UnwindData |  |
| 276 | `??4Win32UiAppBase@@QEAAAEAV0@AEBV0@@Z` | `0x8CF0` | 31 | UnwindData |  |
| 278 | `??4Win32UiDeprecateDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x8CF0` | 31 | UnwindData |  |
| 283 | `??4Win32UiWelcomeDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x8CF0` | 31 | UnwindData |  |
| 230 | `??4DriveInfoCallback@@QEAAAEAV0@AEBV0@@Z` | `0x8D20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `??4DriverListCallback@@QEAAAEAV0@AEBV0@@Z` | `0x8D20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `??4PantherCallback@@QEAAAEAV0@AEBV0@@Z` | `0x8D20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `??4PantherInterface@@QEAAAEAV0@$$QEAV0@@Z` | `0x8D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `??4PantherInterface@@QEAAAEAV0@AEBV0@@Z` | `0x8D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `??B?$CSimpleStringT@G$0A@@ATL@@QEAAAEAV?$CSimpleStringT@G$00@1@XZ` | `0x8D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `??B?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV?$CSimpleStringT@G$00@1@XZ` | `0x8D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `??I?$CComPtrBase@UIUnknown@@@ATL@@QEAAPEAPEAUIUnknown@@XZ` | `0x8D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `??I?$CComPtrBase@UIWebBrowser2@@@ATL@@QEAAPEAPEAUIWebBrowser2@@XZ` | `0x8D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `??4PantherRMEHandler@@QEAAAEAV0@$$QEAV0@@Z` | `0x8D70` | 31 | UnwindData |  |
| 251 | `??4PantherRMEHandler@@QEAAAEAV0@AEBV0@@Z` | `0x8DA0` | 31 | UnwindData |  |
| 252 | `??4PartConfigInfo@@QEAAAEAV0@$$QEAV0@@Z` | `0x8DD0` | 270 | UnwindData |  |
| 253 | `??4PartConfigInfo@@QEAAAEAV0@AEBV0@@Z` | `0x8EF0` | 30 | UnwindData |  |
| 258 | `??4SetupCreateProgressWnd@@QEAAAEAV0@$$QEAV0@@Z` | `0x8F20` | 31 | UnwindData |  |
| 259 | `??4SetupCreateProgressWnd@@QEAAAEAV0@AEBV0@@Z` | `0x8F20` | 31 | UnwindData |  |
| 294 | `??B?$CComPtrBase@UIUnknown@@@ATL@@QEBAPEAUIUnknown@@XZ` | `0x8F50` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `??B?$CComPtrBase@UIWebBrowser2@@@ATL@@QEBAPEAUIWebBrowser2@@XZ` | `0x8F50` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `??B?$CSimpleStringT@G$0A@@ATL@@QEBAPEBGXZ` | `0x8F50` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `??C?$CComPtrBase@UIUnknown@@@ATL@@QEBAPEAV?$_NoAddRefReleaseOnCComPtr@UIUnknown@@@1@XZ` | `0x8F50` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `??C?$CComPtrBase@UIWebBrowser2@@@ATL@@QEBAPEAV?$_NoAddRefReleaseOnCComPtr@UIWebBrowser2@@@1@XZ` | `0x8F50` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `?GetData@?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEBAPEAHXZ` | `0x8F50` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `?GetString@?$CSimpleStringT@G$0A@@ATL@@QEBAPEBGXZ` | `0x8F50` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `?Attach@?$CSimpleStringT@G$0A@@ATL@@AEAAXPEAUCStringData@2@@Z` | `0x90D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `?CloneData@?$CSimpleStringT@G$0A@@ATL@@CAPEAUCStringData@2@PEAU32@@Z` | `0x90E0` | 140 | UnwindData |  |
| 422 | `?CopyChars@?$CSimpleStringT@G$0A@@ATL@@SAXPEAG_KPEBGH@Z` | `0x9180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `?CopyCharsOverlapped@?$CSimpleStringT@G$0A@@ATL@@SAXPEAG_KPEBGH@Z` | `0x91A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `?Empty@?$CSimpleStringT@G$0A@@ATL@@QEAAXXZ` | `0x91C0` | 134 | UnwindData |  |
| 467 | `?Fork@?$CSimpleStringT@G$0A@@ATL@@AEAAXH@Z` | `0x9250` | 192 | UnwindData |  |
| 482 | `?GetBuffer@?$CSimpleStringT@G$0A@@ATL@@QEAAPEAGH@Z` | `0x9320` | 49 | UnwindData |  |
| 682 | `?PrepareWrite@?$CSimpleStringT@G$0A@@ATL@@AEAAPEAGH@Z` | `0x9320` | 49 | UnwindData |  |
| 492 | `?GetData@?$CSimpleStringT@G$0A@@ATL@@AEBAPEAUCStringData@2@XZ` | `0x9360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 497 | `?GetLength@?$CSimpleStringT@G$0A@@ATL@@QEBAHXZ` | `0x9370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 555 | `?IsEmpty@?$CSimpleStringT@G$0A@@ATL@@QEBA_NXZ` | `0x9380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `?OnChanged@PantherRMEHandler@@EEAAXPEBG@Z` | `0x93A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 681 | `?PrepareWrite2@?$CSimpleStringT@G$0A@@ATL@@AEAAXH@Z` | `0x93C0` | 98 | UnwindData |  |
| 687 | `?ProcessWindowMessage@GenericWin32UIBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x9430` | 202 | UnwindData |  |
| 719 | `?Reallocate@?$CSimpleStringT@G$0A@@ATL@@AEAAXH@Z` | `0x9500` | 76 | UnwindData |  |
| 725 | `?ReleaseBufferSetLength@?$CSimpleStringT@G$0A@@ATL@@QEAAXH@Z` | `0x9560` | 50 | UnwindData |  |
| 762 | `?SetLength@?$CSimpleStringT@G$0A@@ATL@@AEAAXH@Z` | `0x9560` | 50 | UnwindData |  |
| 773 | `?SetString@?$CSimpleStringT@G$0A@@ATL@@QEAAXPEBGH@Z` | `0x95A0` | 223 | UnwindData |  |
| 800 | `?ThrowMemoryException@?$CSimpleStringT@G$0A@@ATL@@KAXXZ` | `0x98F0` | 15 | UnwindData |  |
| 16 | `??0?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEAA@AEBV01@@Z` | `0xA4D0` | 149 | UnwindData |  |
| 18 | `??0?$CSimpleStringT@G$0A@@ATL@@QEAA@AEBV01@@Z` | `0xA570` | 38 | UnwindData |  |
| 19 | `??0?$CSimpleStringT@G$0A@@ATL@@QEAA@AEBV?$CSimpleStringT@G$00@1@@Z` | `0xA570` | 38 | UnwindData |  |
| 25 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@AEBV01@@Z` | `0xA570` | 38 | UnwindData |  |
| 21 | `??0?$CSimpleStringT@G$0A@@ATL@@QEAA@PEBGHPEAUIAtlStringMgr@1@@Z` | `0xA5A0` | 181 | UnwindData |  |
| 22 | `??0?$CSimpleStringT@G$0A@@ATL@@QEAA@PEBGPEAUIAtlStringMgr@1@@Z` | `0xA660` | 196 | UnwindData |  |
| 23 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@AEBUtagVARIANT@@@Z` | `0xA730` | 191 | UnwindData |  |
| 24 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@AEBUtagVARIANT@@PEAUIAtlStringMgr@1@@Z` | `0xA800` | 210 | UnwindData |  |
| 26 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@DH@Z` | `0xA8E0` | 172 | UnwindData |  |
| 27 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@GH@Z` | `0xA9A0` | 517 | UnwindData |  |
| 28 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@PEAUIAtlStringMgr@1@@Z` | `0xABB0` | 66 | UnwindData |  |
| 29 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@PEBD@Z` | `0xAC00` | 109 | UnwindData |  |
| 30 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@PEBDH@Z` | `0xAC80` | 249 | UnwindData |  |
| 31 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@PEBDHPEAUIAtlStringMgr@1@@Z` | `0xAD80` | 261 | UnwindData |  |
| 32 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@PEBDPEAUIAtlStringMgr@1@@Z` | `0xAE90` | 117 | UnwindData |  |
| 33 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@PEBE@Z` | `0xAF10` | 87 | UnwindData |  |
| 34 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@PEBEPEAUIAtlStringMgr@1@@Z` | `0xAF70` | 95 | UnwindData |  |
| 35 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@PEBG@Z` | `0xAFE0` | 135 | UnwindData |  |
| 36 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@PEBGH@Z` | `0xB070` | 31 | UnwindData |  |
| 37 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@PEBGHPEAUIAtlStringMgr@1@@Z` | `0xB0A0` | 24 | UnwindData |  |
| 38 | `??0?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAA@PEBGPEAUIAtlStringMgr@1@@Z` | `0xB0C0` | 152 | UnwindData |  |
| 40 | `??0CancelDialogBase@@QEAA@$$QEAV0@@Z` | `0xB160` | 41 | UnwindData |  |
| 41 | `??0CancelDialogBase@@QEAA@AEBV0@@Z` | `0xB190` | 41 | UnwindData |  |
| 42 | `??0CancelDialogBase@@QEAA@XZ` | `0xB1C0` | 41 | UnwindData |  |
| 44 | `??0CreatePartitionCallback@@QEAA@AEBV0@@Z` | `0xB1F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??0DCCallbackData@@QEAA@AEBV0@@Z` | `0xB280` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??0DeletePartitionCallback@@QEAA@AEBV0@@Z` | `0xB310` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `??0DriveInfoCallback@@QEAA@AEBV0@@Z` | `0xB3A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `??0DriverListCallback@@QEAA@AEBV0@@Z` | `0xB3F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `??0ExtendPartitionCallback@@QEAA@AEBV0@@Z` | `0xB440` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `??0FormatPartitionCallback@@QEAA@AEBV0@@Z` | `0xB4D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `??0MediaDriverListDialogBase@@QEAA@AEBV0@@Z` | `0xB560` | 34 | UnwindData |  |
| 85 | `??0NDProgress@@QEAA@AEBV0@@Z` | `0xB590` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `??0OnlineDiskCallback@@QEAA@$$QEAV0@@Z` | `0xB5C0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `??0OnlineDiskCallback@@QEAA@AEBV0@@Z` | `0xB5C0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `??0PKDialogBase@@QEAA@AEBV0@@Z` | `0xB650` | 143 | UnwindData |  |
| 98 | `??0ProgressCommonDialogBase@@QEAA@AEBV0@@Z` | `0xB6F0` | 596 | UnwindData |  |
| 100 | `??0ProgressWinPEDialogBase@@QEAA@$$QEAV0@@Z` | `0xB950` | 45 | UnwindData |  |
| 101 | `??0ProgressWinPEDialogBase@@QEAA@AEBV0@@Z` | `0xB950` | 45 | UnwindData |  |
| 102 | `??0ProgressWinPEDialogBase@@QEAA@XZ` | `0xB990` | 45 | UnwindData |  |
| 139 | `??0Win32UiDiskConfigBase@@QEAA@AEBV0@@Z` | `0xBC00` | 385 | UnwindData |  |
| 141 | `??0Win32UiDriverListDialogBase@@QEAA@AEBV0@@Z` | `0xBD90` | 240 | UnwindData |  |
| 155 | `??1?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEAA@XZ` | `0xBEF0` | 48 | UnwindData |  |
| 729 | `?RemoveAll@?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEAAXXZ` | `0xBEF0` | 48 | UnwindData |  |
| 158 | `??1CreatePartitionCallback@@UEAA@XZ` | `0xC2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `??1DCCallbackData@@UEAA@XZ` | `0xC2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `??1DeletePartitionCallback@@UEAA@XZ` | `0xC2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `??1ExtendPartitionCallback@@UEAA@XZ` | `0xC2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `??1FormatPartitionCallback@@UEAA@XZ` | `0xC2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `??1OnlineDiskCallback@@UEAA@XZ` | `0xC2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `??1ProgressWinPEDialogBase@@UEAA@XZ` | `0xC310` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `??1WDSProgressDialogBase@@UEAA@XZ` | `0xC310` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `??4?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEAAAEAV01@AEBV01@@Z` | `0xC630` | 189 | UnwindData |  |
| 205 | `??4?$CSimpleStringT@G$0A@@ATL@@QEAAAEAV01@PEBG@Z` | `0xC700` | 49 | UnwindData |  |
| 212 | `??4?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@PEBG@Z` | `0xC700` | 49 | UnwindData |  |
| 206 | `??4?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@AEBUtagVARIANT@@@Z` | `0xC740` | 156 | UnwindData |  |
| 208 | `??4?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@D@Z` | `0xC7F0` | 29 | UnwindData |  |
| 209 | `??4?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@G@Z` | `0xC820` | 63 | UnwindData |  |
| 210 | `??4?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@PEBD@Z` | `0xC870` | 203 | UnwindData |  |
| 211 | `??4?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@PEBE@Z` | `0xC950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `??4CancelDialogBase@@QEAAAEAV0@$$QEAV0@@Z` | `0xC960` | 31 | UnwindData |  |
| 214 | `??4CancelDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0xC990` | 31 | UnwindData |  |
| 217 | `??4CreatePartitionCallback@@QEAAAEAV0@AEBV0@@Z` | `0xC9C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `??4DCCallbackData@@QEAAAEAV0@AEBV0@@Z` | `0xC9C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `??4DeletePartitionCallback@@QEAAAEAV0@AEBV0@@Z` | `0xC9C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `??4ExtendPartitionCallback@@QEAAAEAV0@AEBV0@@Z` | `0xC9C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `??4FormatPartitionCallback@@QEAAAEAV0@AEBV0@@Z` | `0xC9C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `??4OnlineDiskCallback@@QEAAAEAV0@$$QEAV0@@Z` | `0xC9C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `??4OnlineDiskCallback@@QEAAAEAV0@AEBV0@@Z` | `0xC9C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `??4MediaDriverListDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0xCA30` | 24 | UnwindData |  |
| 222 | `??4DWebBrowserEventsImpl@@QEAAAEAV0@$$QEAV0@@Z` | `0xCA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `??4DWebBrowserEventsImpl@@QEAAAEAV0@AEBV0@@Z` | `0xCA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `??4NDProgress@@QEAAAEAV0@AEBV0@@Z` | `0xCA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `??4PKDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0xCA70` | 133 | UnwindData |  |
| 254 | `??4ProgressCommonDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0xCB00` | 251 | UnwindData |  |
| 255 | `??4ProgressWinPEDialogBase@@QEAAAEAV0@$$QEAV0@@Z` | `0xCC10` | 24 | UnwindData |  |
| 256 | `??4ProgressWinPEDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0xCC10` | 24 | UnwindData |  |
| 268 | `??4WDSProgressDialogBase@@QEAAAEAV0@$$QEAV0@@Z` | `0xCC10` | 24 | UnwindData |  |
| 269 | `??4WDSProgressDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0xCC10` | 24 | UnwindData |  |
| 279 | `??4Win32UiDiskConfigBase@@QEAAAEAV0@AEBV0@@Z` | `0xCC30` | 352 | UnwindData |  |
| 280 | `??4Win32UiDriverListDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0xCDA0` | 151 | UnwindData |  |
| 291 | `??A?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEAAAEAHH@Z` | `0xCE40` | 40 | UnwindData |  |
| 292 | `??A?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEBAAEBHH@Z` | `0xCE40` | 40 | UnwindData |  |
| 293 | `??A?$CSimpleStringT@G$0A@@ATL@@QEBAGH@Z` | `0xCE70` | 40 | UnwindData |  |
| 481 | `?GetAt@?$CSimpleStringT@G$0A@@ATL@@QEBAGH@Z` | `0xCE70` | 40 | UnwindData |  |
| 307 | `??Y?$CSimpleStringT@G$0A@@ATL@@QEAAAEAV01@AEBV01@@Z` | `0xCF10` | 31 | UnwindData |  |
| 313 | `??Y?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@AEBV?$CSimpleStringT@G$0A@@1@@Z` | `0xCF10` | 31 | UnwindData |  |
| 308 | `??Y?$CSimpleStringT@G$0A@@ATL@@QEAAAEAV01@D@Z` | `0xCF40` | 27 | UnwindData |  |
| 314 | `??Y?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@D@Z` | `0xCF40` | 27 | UnwindData |  |
| 309 | `??Y?$CSimpleStringT@G$0A@@ATL@@QEAAAEAV01@E@Z` | `0xCF70` | 27 | UnwindData |  |
| 315 | `??Y?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@E@Z` | `0xCF70` | 27 | UnwindData |  |
| 310 | `??Y?$CSimpleStringT@G$0A@@ATL@@QEAAAEAV01@G@Z` | `0xCFA0` | 24 | UnwindData |  |
| 316 | `??Y?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@G@Z` | `0xCFA0` | 24 | UnwindData |  |
| 311 | `??Y?$CSimpleStringT@G$0A@@ATL@@QEAAAEAV01@PEBG@Z` | `0xCFC0` | 49 | UnwindData |  |
| 318 | `??Y?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@PEBG@Z` | `0xCFC0` | 49 | UnwindData |  |
| 312 | `??Y?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@AEBUtagVARIANT@@@Z` | `0xD000` | 156 | UnwindData |  |
| 317 | `??Y?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV01@PEBD@Z` | `0xD0B0` | 165 | UnwindData |  |
| 368 | `?Add@?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEAAHAEBH@Z` | `0xDE40` | 162 | UnwindData |  |
| 372 | `?AllocSysString@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBAPEAGXZ` | `0xDEF0` | 39 | UnwindData |  |
| 374 | `?Append@?$CSimpleStringT@G$0A@@ATL@@QEAAXAEBV12@@Z` | `0xDF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `?Append@?$CSimpleStringT@G$0A@@ATL@@QEAAXPEBG@Z` | `0xDF80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `?Append@?$CSimpleStringT@G$0A@@ATL@@QEAAXPEBGH@Z` | `0xDFB0` | 184 | UnwindData |  |
| 377 | `?AppendChar@?$CSimpleStringT@G$0A@@ATL@@QEAAXG@Z` | `0xE070` | 129 | UnwindData |  |
| 378 | `?AppendFormat@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAXIZZ` | `0xE100` | 208 | UnwindData |  |
| 379 | `?AppendFormat@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAXPEBGZZ` | `0xE1E0` | 34 | UnwindData |  |
| 380 | `?AppendFormatV@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAXPEBGPEAD@Z` | `0xE210` | 327 | UnwindData |  |
| 403 | `?CharToOemA@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAXXZ` | `0xE3C0` | 30 | UnwindData |  |
| 579 | `?OemToCharA@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAXXZ` | `0xE3C0` | 30 | UnwindData |  |
| 406 | `?CheckImplicitLoad@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@AEAA_NPEBX@Z` | `0xE3F0` | 39 | UnwindData |  |
| 413 | `?Collate@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBAHPEBG@Z` | `0xE420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `?CollateNoCase@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBAHPEBG@Z` | `0xE440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `?Compare@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBAHPEBG@Z` | `0xE460` | 63 | UnwindData |  |
| 416 | `?CompareNoCase@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBAHPEBG@Z` | `0xE4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `?Concatenate@?$CSimpleStringT@G$0A@@ATL@@KAXAEAV12@PEBGH1H@Z` | `0xE4D0` | 209 | UnwindData |  |
| 420 | `?Construct@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@SAXPEAV12@@Z` | `0xE5B0` | 55 | UnwindData |  |
| 421 | `?CopyChars@?$CSimpleStringT@G$0A@@ATL@@SAXPEAGPEBGH@Z` | `0xE610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `?CopyCharsOverlapped@?$CSimpleStringT@G$0A@@ATL@@SAXPEAGPEBGH@Z` | `0xE630` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `?Delete@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAHHH@Z` | `0xE820` | 266 | UnwindData |  |
| 436 | `?DeviceTimeout@MediaDriverListDialogBase@@EEAAHXZ` | `0xE930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `?DeviceTimeout@Win32UiDriverListDialogBase@@MEAAHXZ` | `0xE950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `?DisableButtons@Win32UiDriverListDialogBase@@IEAAXXZ` | `0xE960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `?DiskPartSetting@Win32UiDiskConfigBase@@QEAAPEAVCDiskPartUserSetting@@XZ` | `0xE980` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 461 | `?Find@?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEBAHAEBH@Z` | `0xEB50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `?Find@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBAHGH@Z` | `0xEB90` | 65 | UnwindData |  |
| 463 | `?Find@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBAHPEBGH@Z` | `0xEBE0` | 70 | UnwindData |  |
| 464 | `?FindOneOf@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBAHPEBG@Z` | `0xEF00` | 47 | UnwindData |  |
| 468 | `?Format@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAXIZZ` | `0xEF40` | 207 | UnwindData |  |
| 469 | `?Format@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAXPEBGZZ` | `0xF020` | 34 | UnwindData |  |
| 471 | `?FormatMessageV@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAXPEBGPEAPEAD@Z` | `0xF050` | 144 | UnwindData |  |
| 472 | `?FormatMessageW@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAXIZZ` | `0xF0F0` | 238 | UnwindData |  |
| 473 | `?FormatMessageW@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAXPEBGZZ` | `0xF1F0` | 58 | UnwindData |  |
| 474 | `?FormatV@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAXPEBGPEAD@Z` | `0xF2B0` | 320 | UnwindData |  |
| 476 | `?FreeExtra@?$CSimpleStringT@G$0A@@ATL@@QEAAXXZ` | `0xF400` | 246 | UnwindData |  |
| 477 | `?GetAction@Win32UiDriverListDialogBase@@IEAA?AW4ACTION@1@XZ` | `0xF540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 478 | `?GetAllocLength@?$CSimpleStringT@G$0A@@ATL@@QEBAHXZ` | `0xF550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `?GetBuffer@?$CSimpleStringT@G$0A@@ATL@@QEAAPEAGXZ` | `0xF560` | 36 | UnwindData |  |
| 484 | `?GetBufferSetLength@?$CSimpleStringT@G$0A@@ATL@@QEAAPEAGH@Z` | `0xF590` | 97 | UnwindData |  |
| 494 | `?GetEnvironmentVariableW@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAHPEBG@Z` | `0xF7D0` | 201 | UnwindData |  |
| 500 | `?GetManager@?$CSimpleStringT@G$0A@@ATL@@QEBAPEAUIAtlStringMgr@2@XZ` | `0xFC50` | 36 | UnwindData |  |
| 501 | `?GetManager@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBAPEAUIAtlStringMgr@2@XZ` | `0xFC80` | 62 | UnwindData |  |
| 513 | `?GetSize@?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEBAHXZ` | `0xFE10` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 543 | `?InitPage@Win32UiDiskConfigBase@@UEAAXXZ` | `0x10330` | 162 | UnwindData |  |
| 538 | `?InitPage@SetupCompatDialogBase@@UEAAXXZ` | `0x103E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 544 | `?InitPage@Win32UiDriverListDialogBase@@UEAAXXZ` | `0x103E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `?OnMediaInserted@@YAXXZ` | `0x103E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `?Insert@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAHHG@Z` | `0x103F0` | 246 | UnwindData |  |
| 548 | `?Insert@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAHHPEBG@Z` | `0x104F0` | 356 | UnwindData |  |
| 552 | `?InternalSetAtIndex@?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEAAXHAEBH@Z` | `0x10660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `?IsCurrentPage@Win32UiDriverListDialogBase@@IEAAHXZ` | `0x10680` | 54 | UnwindData |  |
| 562 | `?Left@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBA?AV12@H@Z` | `0x106C0` | 141 | UnwindData |  |
| 565 | `?LoadStringW@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAHI@Z` | `0x10760` | 182 | UnwindData |  |
| 566 | `?LoadStringW@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAHPEAUHINSTANCE__@@I@Z` | `0x10820` | 302 | UnwindData |  |
| 567 | `?LoadStringW@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAHPEAUHINSTANCE__@@IG@Z` | `0x10960` | 301 | UnwindData |  |
| 568 | `?LockBuffer@?$CSimpleStringT@G$0A@@ATL@@QEAAPEAGXZ` | `0x10AA0` | 52 | UnwindData |  |
| 569 | `?MakeLower@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV12@XZ` | `0x10E80` | 115 | UnwindData |  |
| 570 | `?MakeReverse@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV12@XZ` | `0x10F00` | 109 | UnwindData |  |
| 571 | `?MakeUpper@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV12@XZ` | `0x10F80` | 115 | UnwindData |  |
| 573 | `?Mid@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBA?AV12@H@Z` | `0x11130` | 34 | UnwindData |  |
| 574 | `?Mid@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBA?AV12@HH@Z` | `0x11160` | 233 | UnwindData |  |
| 675 | `?PerformingAction@Win32UiDriverListDialogBase@@IEAAHXZ` | `0x113F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `?Preallocate@?$CSimpleStringT@G$0A@@ATL@@QEAAXH@Z` | `0x11400` | 40 | UnwindData |  |
| 691 | `?ProcessWindowMessage@MediaDriverListDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x11590` | 129 | UnwindData |  |
| 692 | `?ProcessWindowMessage@PKDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x11620` | 364 | UnwindData |  |
| 693 | `?ProcessWindowMessage@ProgressCommonDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x117A0` | 161 | UnwindData |  |
| 694 | `?ProcessWindowMessage@ProgressWinPEDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x11850` | 64 | UnwindData |  |
| 705 | `?ProcessWindowMessage@Win32UiDiskConfigBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x118A0` | 909 | UnwindData |  |
| 706 | `?ProcessWindowMessage@Win32UiDriverListDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x11C40` | 645 | UnwindData |  |
| 715 | `?PromptString@MediaDriverListDialogBase@@EEAAIXZ` | `0x11ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `?PromptString@Win32UiDriverListDialogBase@@MEAAIXZ` | `0x11EE0` | 4,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 724 | `?ReleaseBuffer@?$CSimpleStringT@G$0A@@ATL@@QEAAXH@Z` | `0x13170` | 86 | UnwindData |  |
| 726 | `?Remove@?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEAAHAEBH@Z` | `0x131D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 727 | `?Remove@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAHG@Z` | `0x13210` | 204 | UnwindData |  |
| 730 | `?RemoveAt@?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEAAHH@Z` | `0x132F0` | 153 | UnwindData |  |
| 731 | `?Replace@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAHGG@Z` | `0x13390` | 208 | UnwindData |  |
| 732 | `?Replace@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAHPEBG0@Z` | `0x13470` | 779 | UnwindData |  |
| 734 | `?ReverseFind@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBAHG@Z` | `0x13800` | 47 | UnwindData |  |
| 735 | `?Right@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBA?AV12@H@Z` | `0x13840` | 174 | UnwindData |  |
| 739 | `?SetActive@CancelDialogBase@@UEAAXAEAH@Z` | `0x13A10` | 530 | UnwindData |  |
| 754 | `?SetAt@?$CSimpleStringT@G$0A@@ATL@@QEAAXHG@Z` | `0x13C30` | 135 | UnwindData |  |
| 755 | `?SetAtIndex@?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@QEAAHHAEBH@Z` | `0x13CC0` | 1,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 763 | `?SetManager@?$CSimpleStringT@G$0A@@ATL@@QEAAXPEAUIAtlStringMgr@2@@Z` | `0x143D0` | 85 | UnwindData |  |
| 765 | `?SetQuickDeviceTimeout@MediaDriverListDialogBase@@SAXH@Z` | `0x14430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 772 | `?SetString@?$CSimpleStringT@G$0A@@ATL@@QEAAXPEBG@Z` | `0x14440` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 774 | `?SetSysString@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBAPEAGPEAPEAG@Z` | `0x14470` | 51 | UnwindData |  |
| 786 | `?SpanExcluding@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBA?AV12@PEBG@Z` | `0x144B0` | 79 | UnwindData |  |
| 787 | `?SpanIncluding@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBA?AV12@PEBG@Z` | `0x14510` | 79 | UnwindData |  |
| 792 | `?StringLength@?$CSimpleStringT@G$0A@@ATL@@SAHPEBD@Z` | `0x14700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `?StringLength@?$CSimpleStringT@G$0A@@ATL@@SAHPEBG@Z` | `0x14720` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 801 | `?Tokenize@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEBA?AV12@PEBGAEAH@Z` | `0x14B30` | 407 | UnwindData |  |
| 802 | `?Trim@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV12@G@Z` | `0x14CD0` | 30 | UnwindData |  |
| 803 | `?Trim@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV12@PEBG@Z` | `0x14D00` | 30 | UnwindData |  |
| 804 | `?Trim@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV12@XZ` | `0x14D30` | 21 | UnwindData |  |
| 805 | `?TrimLeft@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV12@G@Z` | `0x14D50` | 224 | UnwindData |  |
| 806 | `?TrimLeft@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV12@PEBG@Z` | `0x14E40` | 274 | UnwindData |  |
| 807 | `?TrimLeft@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV12@XZ` | `0x14F60` | 256 | UnwindData |  |
| 808 | `?TrimRight@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV12@G@Z` | `0x15070` | 168 | UnwindData |  |
| 809 | `?TrimRight@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV12@PEBG@Z` | `0x15120` | 229 | UnwindData |  |
| 810 | `?TrimRight@?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAAAEAV12@XZ` | `0x15210` | 189 | UnwindData |  |
| 811 | `?Truncate@?$CSimpleStringT@G$0A@@ATL@@QEAAXH@Z` | `0x152E0` | 95 | UnwindData |  |
| 812 | `?UnlockBuffer@?$CSimpleStringT@G$0A@@ATL@@QEAAXXZ` | `0x15610` | 2,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `?v_Chk@PKDialogBase@@AEAAHK@Z` | `0x16090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 848 | `?v_Chk@ProgressCommonDialogBase@@AEAAHK@Z` | `0x160B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `?v_Clr@PKDialogBase@@AEAAXK@Z` | `0x160D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `?v_Clr@ProgressCommonDialogBase@@AEAAXK@Z` | `0x160E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `?v_Set@PKDialogBase@@AEAAXK@Z` | `0x160F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `?v_Set@ProgressCommonDialogBase@@AEAAXK@Z` | `0x16100` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `?ConfigureActions@DiskConfig@@AEAAHXZ` | `0x16580` | 876 | UnwindData |  |
| 446 | `?DoesUnusedSpaceExist@DiskConfig@@QEAAHK_KPEA_K@Z` | `0x16980` | 161 | UnwindData |  |
| 475 | `?FreeDiskArray@DiskConfig@@AEAAXXZ` | `0x16A30` | 87 | UnwindData |  |
| 563 | `?LoadFromBlackboard@DiskConfig@@QEAAHPEAU_BLACKBOARD@@PEAUHINSTANCE__@@@Z` | `0x16A90` | 4,110 | UnwindData |  |
| 564 | `?LoadPartitionInfo@DiskConfig@@AEAAXPEAU_BLACKBOARD@@PEBGPEAVPartConfigInfo@@PEAUHINSTANCE__@@H@Z` | `0x17AB0` | 1,456 | UnwindData |  |
| 45 | `??0CreatePartitionCallback@@QEAA@PEAUHWND__@@PEAVPartConfigInfo@@K@Z` | `0x180E0` | 541 | UnwindData |  |
| 47 | `??0DCCallbackData@@QEAA@PEAUHWND__@@IK@Z` | `0x18310` | 82 | UnwindData |  |
| 55 | `??0DeletePartitionCallback@@QEAA@PEAUHWND__@@PEAVPartConfigInfo@@@Z` | `0x18370` | 76 | UnwindData |  |
| 62 | `??0DriveInfoCallback@@QEAA@PEAUHWND__@@K@Z` | `0x183D0` | 97 | UnwindData |  |
| 64 | `??0DriverListCallback@@QEAA@PEAUHWND__@@PEBG@Z` | `0x18440` | 188 | UnwindData |  |
| 68 | `??0ExtendPartitionCallback@@QEAA@PEAUHWND__@@PEAVPartConfigInfo@@K@Z` | `0x18510` | 106 | UnwindData |  |
| 73 | `??0FormatPartitionCallback@@QEAA@PEAUHWND__@@PEAVPartConfigInfo@@@Z` | `0x18580` | 132 | UnwindData |  |
| 89 | `??0OnlineDiskCallback@@QEAA@PEAUHWND__@@PEAVPartConfigInfo@@@Z` | `0x18610` | 76 | UnwindData |  |
| 140 | `??0Win32UiDiskConfigBase@@QEAA@XZ` | `0x18670` | 225 | UnwindData |  |
| 164 | `??1DriveInfoCallback@@UEAA@XZ` | `0x18760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `??1DriverListCallback@@UEAA@XZ` | `0x18780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `??1Win32UiDiskConfigBase@@QEAA@XZ` | `0x187A0` | 523 | UnwindData |  |
| 400 | `?CanPageBeActivated@Win32UiDiskConfigBase@@UEAAHW4Direction@@PEAH@Z` | `0x18AD0` | 303 | UnwindData |  |
| 404 | `?CheckForNonZeroSize@Win32UiDiskConfigBase@@AEAAXXZ` | `0x18C10` | 112 | UnwindData |  |
| 405 | `?CheckForValidSize@Win32UiDiskConfigBase@@QEAAHPEAKHI@Z` | `0x18C90` | 359 | UnwindData |  |
| 419 | `?ConfirmAction@Win32UiDiskConfigBase@@QEAAHW4_DC_WARNING_TYPE@@@Z` | `0x18E00` | 184 | UnwindData |  |
| 442 | `?DiskConfigSubProc@Win32UiDiskConfigBase@@SA_JPEAUHWND__@@I_K_J@Z` | `0x18EF0` | 388 | UnwindData |  |
| 443 | `?DiskConfigWarningDlgProc@Win32UiDiskConfigBase@@SA_JPEAUHWND__@@I_K_J@Z` | `0x19080` | 355 | UnwindData |  |
| 447 | `?DrawItem@Win32UiDiskConfigBase@@QEAA_JPEAUtagNMLVCUSTOMDRAW@@@Z` | `0x191F0` | 757 | UnwindData |  |
| 448 | `?DrawSubItem@Win32UiDiskConfigBase@@QEAA_JPEAUtagNMLVCUSTOMDRAW@@@Z` | `0x194F0` | 665 | UnwindData |  |
| 470 | `?FormatDiskMessage@Win32UiDiskConfigBase@@QEAAXAEAV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEBG@Z` | `0x19790` | 100 | UnwindData |  |
| 493 | `?GetDiskNumber@DCCallbackData@@QEAAHXZ` | `0x19800` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `?GetErrorTextFromErrorCode@Win32UiDiskConfigBase@@QEAA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@J@Z` | `0x19830` | 945 | UnwindData |  |
| 507 | `?GetPartitionDescriptionId@Win32UiDiskConfigBase@@AEAAIPEAVPartConfigInfo@@@Z` | `0x19BF0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `?GetPartitionOffset@DCCallbackData@@QEAA_KXZ` | `0x19C80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `?GetSelectedPartitionInfo@Win32UiDiskConfigBase@@AEAAPEAVPartConfigInfo@@PEAUHWND__@@@Z` | `0x19CB0` | 166 | UnwindData |  |
| 515 | `?GetStyledFont@Win32UiDiskConfigBase@@QEAAPEAUHFONT__@@HH@Z` | `0x19D60` | 216 | UnwindData |  |
| 518 | `?HideSizeControls@Win32UiDiskConfigBase@@QEAAXXZ` | `0x19E40` | 434 | UnwindData |  |
| 529 | `?Init@DCCallbackData@@IEAAXPEAVPartConfigInfo@@@Z` | `0x1A000` | 320 | UnwindData |  |
| 531 | `?InitCustomButtons@Win32UiDiskConfigBase@@QEAAXXZ` | `0x1A150` | 2,044 | UnwindData |  |
| 369 | `?AddRef@DWebBrowserEventsImpl@@EEAAKXZ` | `0x1A960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | `?ImageLanguageRequired@WDSImageSelectionDialogBase@@UEAAHXZ` | `0x1A960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `?IsWDS@WDSDeprecateDialogBase@@QEAAHXZ` | `0x1A960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 575 | `?NotifyWizBack@Win32UiDiskConfigBase@@UEAAHAEAH@Z` | `0x1A960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 642 | `?OnInitDialog@Win32UiDeprecateDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x1A960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 646 | `?OnInitDialog@Win32UiWelcomeDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x1A960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `?OnActionComplete@Win32UiDiskConfigBase@@QEAA_JI_K_JAEAH@Z` | `0x1A970` | 565 | UnwindData |  |
| 581 | `?OnCallback@DCCallbackData@@MEAA_KPEBUWDS_DATA@@@Z` | `0x1ABB0` | 30 | UnwindData |  |
| 582 | `?OnCallback@DriverListCallback@@MEAA_KPEBUWDS_DATA@@@Z` | `0x1ABE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 586 | `?OnClick@Win32UiDiskConfigBase@@QEAA_JHPEAUtagNMHDR@@AEAH@Z` | `0x1AC00` | 105 | UnwindData |  |
| 587 | `?OnCommandAdvanced@Win32UiDiskConfigBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1AC70` | 151 | UnwindData |  |
| 592 | `?OnCommandContinue@Win32UiDiskConfigBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1AD10` | 1,177 | UnwindData |  |
| 595 | `?OnCommandCreate@Win32UiDiskConfigBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1B1B0` | 84 | UnwindData |  |
| 598 | `?OnCommandDelete@Win32UiDiskConfigBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1B210` | 416 | UnwindData |  |
| 600 | `?OnCommandExtend@Win32UiDiskConfigBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1B3C0` | 84 | UnwindData |  |
| 601 | `?OnCommandFormat@Win32UiDiskConfigBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1B420` | 421 | UnwindData |  |
| 603 | `?OnCommandLoadDriver@Win32UiDiskConfigBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1B5D0` | 88 | UnwindData |  |
| 607 | `?OnCommandRefresh@Win32UiDiskConfigBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1B630` | 165 | UnwindData |  |
| 610 | `?OnCommandShowMessage@Win32UiDiskConfigBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1B6E0` | 381 | UnwindData |  |
| 618 | `?OnCustomDraw@Win32UiDiskConfigBase@@QEAA_JHPEAUtagNMHDR@@AEAH@Z` | `0x1B870` | 108 | UnwindData |  |
| 628 | `?OnFKeyPressed@Win32UiDiskConfigBase@@QEAA_JI_K_JAEAH@Z` | `0x1B8F0` | 163 | UnwindData |  |
| 629 | `?OnGetDispInfo@Win32UiDiskConfigBase@@QEAA_JHPEAUtagNMHDR@@AEAH@Z` | `0x1B9A0` | 962 | UnwindData |  |
| 643 | `?OnInitDialog@Win32UiDiskConfigBase@@QEAA_JI_K_JAEAH@Z` | `0x1BD70` | 972 | UnwindData |  |
| 651 | `?OnItemChanging@Win32UiDiskConfigBase@@QEAA_JHPEAUtagNMHDR@@AEAH@Z` | `0x1C150` | 271 | UnwindData |  |
| 653 | `?OnKeyDown@Win32UiDiskConfigBase@@QEAA_JHPEAUtagNMHDR@@AEAH@Z` | `0x1C270` | 186 | UnwindData |  |
| 655 | `?OnMouseOver@Win32UiDiskConfigBase@@QEAA_JHPEAUtagNMHDR@@AEAH@Z` | `0x1C330` | 229 | UnwindData |  |
| 664 | `?OnSetFocus@Win32UiDiskConfigBase@@QEAA_JHPEAUtagNMHDR@@AEAH@Z` | `0x1C420` | 71 | UnwindData |  |
| 665 | `?OnSizeCancel@Win32UiDiskConfigBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1C470` | 124 | UnwindData |  |
| 666 | `?OnSizeOk@Win32UiDiskConfigBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1C500` | 1,114 | UnwindData |  |
| 671 | `?OnUDDeltaPos@Win32UiDiskConfigBase@@QEAA_JHPEAUtagNMHDR@@AEAH@Z` | `0x1C960` | 247 | UnwindData |  |
| 676 | `?PickInstallableRegion@Win32UiDiskConfigBase@@QEAAHPEAUHWND__@@@Z` | `0x1CA60` | 266 | UnwindData |  |
| 720 | `?RefreshListViewFromBlackboard@Win32UiDiskConfigBase@@QEAAHXZ` | `0x1CB70` | 336 | UnwindData |  |
| 750 | `?SetActive@Win32UiDiskConfigBase@@UEAAXAEAH@Z` | `0x1CCD0` | 237 | UnwindData |  |
| 757 | `?SetButtonState@Win32UiDiskConfigBase@@QEAAXIH@Z` | `0x1CDD0` | 659 | UnwindData |  |
| 758 | `?SetDCMessageLinkText@Win32UiDiskConfigBase@@QEAAHKPEAVPartConfigInfo@@@Z` | `0x1D070` | 381 | UnwindData |  |
| 759 | `?SetErrorTextFromResource@Win32UiDiskConfigBase@@QEAA?AW4_ENUMTEXTSETTYPE@@K@Z` | `0x1D200` | 221 | UnwindData |  |
| 760 | `?SetErrorTextFromString@Win32UiDiskConfigBase@@QEAA?AW4_ENUMTEXTSETTYPE@@PEBG@Z` | `0x1D2F0` | 244 | UnwindData |  |
| 761 | `?SetInlineDiskMessage@Win32UiDiskConfigBase@@QEAA?AW4_ENUMTEXTSETTYPE@@K_KHJ@Z` | `0x1D3F0` | 978 | UnwindData |  |
| 770 | `?SetSizeErrorText@Win32UiDiskConfigBase@@QEAAXKH@Z` | `0x1D7D0` | 552 | UnwindData |  |
| 778 | `?ShowAdvancedOptions@Win32UiDiskConfigBase@@QEAAXH@Z` | `0x1DA00` | 236 | UnwindData |  |
| 779 | `?ShowDiskError@Win32UiDiskConfigBase@@SAXKJ@Z` | `0x1DB00` | 277 | UnwindData |  |
| 782 | `?ShowSizeControls@Win32UiDiskConfigBase@@QEAAXII@Z` | `0x1DDE0` | 1,234 | UnwindData |  |
| 785 | `?SizeEditSubProc@Win32UiDiskConfigBase@@CA_JPEAUHWND__@@I_K_J@Z` | `0x1E2C0` | 940 | UnwindData |  |
| 795 | `?SyncToConfigInfo@Win32UiDiskConfigBase@@QEAAXPEAVConfigInfo@@@Z` | `0x1E680` | 1,163 | UnwindData |  |
| 84 | `??0MediaDriverListDialogBase@@QEAA@XZ` | `0x1EDA0` | 34 | UnwindData |  |
| 142 | `??0Win32UiDriverListDialogBase@@QEAA@XZ` | `0x1EDD0` | 117 | UnwindData |  |
| 173 | `??1MediaDriverListDialogBase@@UEAA@XZ` | `0x1EE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `??1Win32UiDriverListDialogBase@@UEAA@XZ` | `0x1EE70` | 538 | UnwindData |  |
| 381 | `?AsyncScanForDrivers@Win32UiDriverListDialogBase@@IEAAXPEBG@Z` | `0x1F090` | 192 | UnwindData |  |
| 391 | `?CanPageBeActivated@MediaDriverListDialogBase@@UEAAHW4Direction@@PEAH@Z` | `0x1F160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `?CanReadMedia@MediaDriverListDialogBase@@AEAAHXZ` | `0x1F180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `?CloseCurrentBrowse@Win32UiDriverListDialogBase@@IEAAXXZ` | `0x1F1A0` | 44 | UnwindData |  |
| 445 | `?DoBrowse@Win32UiDriverListDialogBase@@IEAAHXZ` | `0x1F1E0` | 377 | UnwindData |  |
| 450 | `?DriverScanCallback@Win32UiDriverListDialogBase@@KAXPEAXH@Z` | `0x1F360` | 200 | UnwindData |  |
| 454 | `?EnableButtons@Win32UiDriverListDialogBase@@IEAAXXZ` | `0x1F430` | 57 | UnwindData |  |
| 455 | `?EnableControls@Win32UiDriverListDialogBase@@IEAAXH@Z` | `0x1F470` | 355 | UnwindData |  |
| 466 | `?FirstVisit@Win32UiDriverListDialogBase@@EEAAXXZ` | `0x1F5E0` | 54 | UnwindData |  |
| 510 | `?GetSelectedItems@Win32UiDriverListDialogBase@@IEAAHPEAV?$CSimpleArray@HV?$CSimpleArrayEqualHelper@H@ATL@@@ATL@@@Z` | `0x1F620` | 290 | UnwindData |  |
| 549 | `?InstallDriverCallback@Win32UiDriverListDialogBase@@KAXPEAXH@Z` | `0x1F750` | 214 | UnwindData |  |
| 550 | `?InstallSelectedDriver@Win32UiDriverListDialogBase@@IEAAHXZ` | `0x1F830` | 170 | UnwindData |  |
| 561 | `?KillActive@Win32UiDriverListDialogBase@@UEAAXAEAH@Z` | `0x1F8E0` | 333 | UnwindData |  |
| 588 | `?OnCommandBrowse@Win32UiDriverListDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1FA40` | 39 | UnwindData |  |
| 593 | `?OnCommandContinue@Win32UiDriverListDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1FA70` | 26 | UnwindData |  |
| 608 | `?OnCommandRefresh@Win32UiDriverListDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1FA90` | 30 | UnwindData |  |
| 611 | `?OnCommandToggleDriverList@Win32UiDriverListDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x1FAC0` | 129 | UnwindData |  |
| 614 | `?OnControlKeyPressed@Win32UiDriverListDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x1FB50` | 261 | UnwindData |  |
| 617 | `?OnCtlColorStatic@Win32UiDriverListDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x1FC60` | 131 | UnwindData |  |
| 621 | `?OnDestroy@Win32UiDriverListDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x1FCF0` | 48 | UnwindData |  |
| 623 | `?OnDeviceArrival@MediaDriverListDialogBase@@EEAAXH@Z` | `0x1FD30` | 200 | UnwindData |  |
| 624 | `?OnDeviceArrival@Win32UiDriverListDialogBase@@MEAAXH@Z` | `0x1FE00` | 57 | UnwindData |  |
| 625 | `?OnDeviceChange@MediaDriverListDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x1FE40` | 52 | UnwindData |  |
| 626 | `?OnDriverScanComplete@Win32UiDriverListDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x1FE80` | 255 | UnwindData |  |
| 644 | `?OnInitDialog@Win32UiDriverListDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x1FF90` | 845 | UnwindData |  |
| 648 | `?OnInstallDriverDone@Win32UiDriverListDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x202F0` | 667 | UnwindData |  |
| 650 | `?OnItemChanged@Win32UiDriverListDialogBase@@QEAA_JHPEAUtagNMHDR@@AEAH@Z` | `0x205A0` | 74 | UnwindData |  |
| 662 | `?OnPromptAndScanForDrivers@Win32UiDriverListDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x205F0` | 110 | UnwindData |  |
| 663 | `?OnRefreshComplete@Win32UiDriverListDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x20670` | 194 | UnwindData |  |
| 669 | `?OnTimer@Win32UiDriverListDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x20740` | 29 | UnwindData |  |
| 679 | `?PopulateDriverList@Win32UiDriverListDialogBase@@IEAAXXZ` | `0x20770` | 394 | UnwindData |  |
| 736 | `?SHBrowseForFolderCallback@Win32UiDriverListDialogBase@@CAHPEAUHWND__@@I_J1@Z` | `0x20900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `?ScanForDrivers@Win32UiDriverListDialogBase@@IEAAXII@Z` | `0x20920` | 207 | UnwindData |  |
| 738 | `?SetAction@Win32UiDriverListDialogBase@@IEAAXW4ACTION@1@@Z` | `0x20A00` | 370 | UnwindData |  |
| 751 | `?SetActive@Win32UiDriverListDialogBase@@UEAAXAEAH@Z` | `0x20B80` | 107 | UnwindData |  |
| 766 | `SetQuickMediaDeviceTimeout` | `0x20C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `?ShowMessage@Win32UiDriverListDialogBase@@IEAAHPEBG0I@Z` | `0x20C20` | 122 | UnwindData |  |
| 823 | `?WaitForDevice@Win32UiDriverListDialogBase@@IEAAXXZ` | `0x20CA0` | 56 | UnwindData |  |
| 15 | `??0?$CDynamicArray@PEAVIImageData@@PEAV1@@@QEAA@_K@Z` | `0x20CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `??0Win32UiDeprecateDialogBase@@QEAA@$$QEAV0@@Z` | `0x20D00` | 41 | UnwindData |  |
| 137 | `??0Win32UiDeprecateDialogBase@@QEAA@AEBV0@@Z` | `0x20D30` | 41 | UnwindData |  |
| 138 | `??0Win32UiDeprecateDialogBase@@QEAA@XZ` | `0x20D60` | 41 | UnwindData |  |
| 143 | `??0Win32UiFinishDialogBase@@QEAA@AEBV0@@Z` | `0x20D90` | 73 | UnwindData |  |
| 145 | `??0Win32UiWelcomeDialogBase@@QEAA@$$QEAV0@@Z` | `0x20DE0` | 41 | UnwindData |  |
| 146 | `??0Win32UiWelcomeDialogBase@@QEAA@AEBV0@@Z` | `0x20E10` | 41 | UnwindData |  |
| 147 | `??0Win32UiWelcomeDialogBase@@QEAA@XZ` | `0x20E40` | 41 | UnwindData |  |
| 148 | `??0Win32uiImageSelectionDialogBase@@QEAA@AEBV0@@Z` | `0x20E70` | 113 | UnwindData |  |
| 149 | `??0Win32uiImageSelectionDialogBase@@QEAA@XZ` | `0x20EF0` | 86 | UnwindData |  |
| 154 | `??1?$CDynamicArray@PEAVIImageData@@PEAV1@@@QEAA@XZ` | `0x20F50` | 30 | UnwindData |  |
| 194 | `??1Win32uiImageSelectionDialogBase@@UEAA@XZ` | `0x20F80` | 195 | UnwindData |  |
| 201 | `??4?$CDynamicArray@PEAVIImageData@@PEAV1@@@QEAAAEAV0@AEBV0@@Z` | `0x21050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `??4FinishDialogBase@@QEAAAEAV0@$$QEAV0@@Z` | `0x21070` | 63 | UnwindData |  |
| 235 | `??4FinishDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x21070` | 63 | UnwindData |  |
| 264 | `??4WDSFinishDialogBase@@QEAAAEAV0@$$QEAV0@@Z` | `0x21070` | 63 | UnwindData |  |
| 265 | `??4WDSFinishDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x21070` | 63 | UnwindData |  |
| 281 | `??4Win32UiFinishDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x21070` | 63 | UnwindData |  |
| 266 | `??4WDSImageSelectionDialogBase@@QEAAAEAV0@$$QEAV0@@Z` | `0x210C0` | 103 | UnwindData |  |
| 267 | `??4WDSImageSelectionDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x210C0` | 103 | UnwindData |  |
| 284 | `??4Win32uiImageSelectionDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x210C0` | 103 | UnwindData |  |
| 366 | `??_F?$CDynamicArray@PEAVIImageData@@PEAV1@@@QEAAXXZ` | `0x211B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `?Add@?$CDynamicArray@PEAVIImageData@@PEAV1@@@QEAAHAEAPEAVIImageData@@@Z` | `0x21210` | 60 | UnwindData |  |
| 452 | `?ElementAt@?$CDynamicArray@PEAVIImageData@@PEAV1@@@QEAAAEAPEAVIImageData@@_K@Z` | `0x21260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `?GetSize@?$CDynamicArray@PEAVIImageData@@PEAV1@@@QEBA_KXZ` | `0x21270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `?ImageSelectionSetting@Win32uiImageSelectionDialogBase@@QEAAPEAVCWDSUIImageSelectionSetting@@XZ` | `0x21280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `?Init@?$CDynamicArray@PEAVIImageData@@PEAV1@@@IEAAX_K@Z` | `0x21290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `?InitPage@Win32uiImageSelectionDialogBase@@UEAAXXZ` | `0x212B0` | 316 | UnwindData |  |
| 578 | `?NotifyWizNext@Win32UiFinishDialogBase@@UEAAHAEAH@Z` | `0x21400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `?OnCommandContinue@Win32uiImageSelectionDialogBase@@UEAA_JGGPEAUHWND__@@AEAH@Z` | `0x21420` | 1,397 | UnwindData |  |
| 619 | `?OnCustomDraw@Win32uiImageSelectionDialogBase@@QEAA_JHPEAUtagNMHDR@@AEAH@Z` | `0x219A0` | 331 | UnwindData |  |
| 630 | `?OnGetDispInfo@Win32uiImageSelectionDialogBase@@QEAA_JHPEAUtagNMHDR@@AEAH@Z` | `0x21B00` | 469 | UnwindData |  |
| 647 | `?OnInitDialog@Win32uiImageSelectionDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x21CE0` | 513 | UnwindData |  |
| 652 | `?OnItemChanging@Win32uiImageSelectionDialogBase@@QEAA_JHPEAUtagNMHDR@@AEAH@Z` | `0x21EF0` | 801 | UnwindData |  |
| 704 | `?ProcessWindowMessage@Win32UiDeprecateDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x22220` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 708 | `?ProcessWindowMessage@Win32UiWelcomeDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x22220` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 707 | `?ProcessWindowMessage@Win32UiFinishDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x22250` | 213 | UnwindData |  |
| 709 | `?ProcessWindowMessage@Win32uiImageSelectionDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x22330` | 372 | UnwindData |  |
| 728 | `?RemoveAll@?$CDynamicArray@PEAVIImageData@@PEAV1@@@QEAAXXZ` | `0x224B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `?SetActive@Win32uiImageSelectionDialogBase@@UEAAXAEAH@Z` | `0x224C0` | 276 | UnwindData |  |
| 769 | `?SetSize@?$CDynamicArray@PEAVIImageData@@PEAV1@@@QEAAH_K@Z` | `0x225E0` | 126 | UnwindData |  |
| 850 | `?v_ClearArray@Win32uiImageSelectionDialogBase@@AEAAXXZ` | `0x22670` | 87 | UnwindData |  |
| 854 | `?v_CreateListViewColumns@Win32uiImageSelectionDialogBase@@AEAAHPEAUHWND__@@@Z` | `0x226D0` | 845 | UnwindData |  |
| 856 | `?v_EnableLanguageDropdownList@Win32uiImageSelectionDialogBase@@AEAAXH@Z` | `0x22A30` | 109 | UnwindData |  |
| 857 | `?v_GetColumnAt@Win32uiImageSelectionDialogBase@@AEAAHH@Z` | `0x22AB0` | 86 | UnwindData |  |
| 872 | `?v_PopulateImageList@Win32uiImageSelectionDialogBase@@IEAAXXZ` | `0x22B10` | 1,411 | UnwindData |  |
| 873 | `?v_ScaleListViewColumns@Win32uiImageSelectionDialogBase@@AEAAXPEAUHWND__@@@Z` | `0x230A0` | 464 | UnwindData |  |
| 881 | `?v_ShowDescription@Win32uiImageSelectionDialogBase@@AEAAXPEBGH@Z` | `0x23280` | 707 | UnwindData |  |
| 86 | `??0NDProgress@@QEAA@XZ` | `0x24170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `??1NDProgress@@UEAA@XZ` | `0x24190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `?Init@NDProgress@@QEAAXPEAUHWND__@@@Z` | `0x241B0` | 157 | UnwindData |  |
| 733 | `?Reset@NDProgress@@QEAAXXZ` | `0x24260` | 116 | UnwindData |  |
| 788 | `?Start@NDProgress@@QEAAXXZ` | `0x242E0` | 52 | UnwindData |  |
| 789 | `?StaticCallback@NDProgress@@CAXPEAUHWND__@@I_KK@Z` | `0x24320` | 131 | UnwindData |  |
| 791 | `?Stop@NDProgress@@QEAAXXZ` | `0x243B0` | 49 | UnwindData |  |
| 649 | `?OnInstallTypeSelected@@YAXH@Z` | `0x26130` | 144 | UnwindData |  |
| 673 | `OnlineUI` | `0x261D0` | 89 | UnwindData |  |
| 780 | `?ShowFinish@@YAHXZ` | `0x26230` | 780 | UnwindData |  |
| 783 | `?SimulateCallbackCancelSetup@@YAXXZ` | `0x26550` | 83 | UnwindData |  |
| 784 | `?SimulateCallbackShowError@@YAXXZ` | `0x265B0` | 149 | UnwindData |  |
| 826 | `Win32UI` | `0x26650` | 130 | UnwindData |  |
| 827 | `WinPeUI` | `0x266E0` | 548 | UnwindData |  |
| 93 | `??0PantherCallback@@QEAA@PEAXPEBGIPEAUHWND__@@I@Z` | `0x26F80` | 145 | UnwindData |  |
| 177 | `??1PantherCallback@@UEAA@XZ` | `0x27020` | 82 | UnwindData |  |
| 525 | `?ImageLanguageRequired@IBSImageSelectionDialogBase@@UEAAHXZ` | `0x27080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `?OnCallback@PantherCallback@@MEAA_KPEBUWDS_DATA@@@Z` | `0x27080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 639 | `?OnInitDialog@UnattendDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x27080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 723 | `?Release@DWebBrowserEventsImpl@@EEAAKXZ` | `0x27080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 717 | `?PublishImmediateAsync@PantherCallback@@QEAAHXZ` | `0x27090` | 55 | UnwindData |  |
| 790 | `?StaticCallback@PantherCallback@@KAXW4WDS_EVENT_RESULT@@PEBUWDS_DATA@@PEAX@Z` | `0x270D0` | 150 | UnwindData |  |
| 91 | `??0PKDialogBase@@QEAA@XZ` | `0x27170` | 222 | UnwindData |  |
| 150 | `??1?$CComPtr@UIUnknown@@@ATL@@QEAA@XZ` | `0x27260` | 40 | UnwindData |  |
| 151 | `??1?$CComPtr@UIWebBrowser2@@@ATL@@QEAA@XZ` | `0x27260` | 40 | UnwindData |  |
| 176 | `??1PKDialogBase@@UEAA@XZ` | `0x27290` | 227 | UnwindData |  |
| 392 | `?CanPageBeActivated@PKDialogBase@@UEAAHW4Direction@@PEAH@Z` | `0x273C0` | 76 | UnwindData |  |
| 509 | `?GetPid@PKDialogBase@@QEAAPEAVPIDUtilStringView@@XZ` | `0x27420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `?InitPage@PKDialogBase@@UEAAXXZ` | `0x27440` | 173 | UnwindData |  |
| 605 | `?OnCommandPrivacyStmt@PKDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x27500` | 162 | UnwindData |  |
| 613 | `?OnContinue@PKDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x275B0` | 341 | UnwindData |  |
| 636 | `?OnInitDialog@PKDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x27710` | 790 | UnwindData |  |
| 656 | `?OnOSK@PKDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x27A30` | 199 | UnwindData |  |
| 657 | `?OnPKChanged@PKDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x27B00` | 285 | UnwindData |  |
| 658 | `?OnPKChangedEx@PKDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x27C30` | 113 | UnwindData |  |
| 659 | `?OnPkValidateDone@PKDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x27CB0` | 909 | UnwindData |  |
| 660 | `?OnProductKeySkip@PKDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x28050` | 149 | UnwindData |  |
| 677 | `?PidValidateCallback@PKDialogBase@@SAXPEAX_K@Z` | `0x280F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 678 | `?PkEditSubProc@PKDialogBase@@SA_JPEAUHWND__@@I_K_J@Z` | `0x28120` | 403 | UnwindData |  |
| 745 | `?SetActive@PKDialogBase@@UEAAXAEAH@Z` | `0x282C0` | 48 | UnwindData |  |
| 851 | `?v_CloseOSK@PKDialogBase@@AEAAXXZ` | `0x28A40` | 51 | UnwindData |  |
| 855 | `?v_Enable@PKDialogBase@@AEAAXH@Z` | `0x28A80` | 91 | UnwindData |  |
| 858 | `?v_GetDUStateForBackButtonState@PKDialogBase@@AEAAXXZ` | `0x28AF0` | 132 | UnwindData |  |
| 860 | `?v_GetSetting@PKDialogBase@@AEAAPEAVCProductKeyUserSetting@@XZ` | `0x28B80` | 86 | UnwindData |  |
| 861 | `?v_InitEdit@PKDialogBase@@AEAAXXZ` | `0x28BE0` | 274 | UnwindData |  |
| 862 | `?v_InitOSK@PKDialogBase@@AEAAXXZ` | `0x28D00` | 488 | UnwindData |  |
| 863 | `?v_InitPrivacyStmt@PKDialogBase@@AEAAXXZ` | `0x28EF0` | 227 | UnwindData |  |
| 864 | `?v_InitProductKeySkipButton@PKDialogBase@@AEAAXXZ` | `0x28FE0` | 227 | UnwindData |  |
| 877 | `?v_SetBackButtonState@PKDialogBase@@AEAAXXZ` | `0x290D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 878 | `?v_SetFont@PKDialogBase@@AEAAXPEAUHWND__@@@Z` | `0x29100` | 348 | UnwindData |  |
| 879 | `?v_SetNextButtonState@PKDialogBase@@AEAAXXZ` | `0x29270` | 219 | UnwindData |  |
| 429 | `?CreateProgressWnd@SetupCreateProgressWnd@@UEAAPEAUHWND__@@PEAU2@PEAUProgressCreateStruct@@@Z` | `0x295E0` | 519 | UnwindData |  |
| 99 | `??0ProgressCommonDialogBase@@QEAA@XZ` | `0x2A860` | 171 | UnwindData |  |
| 178 | `??1ProgressCommonDialogBase@@UEAA@XZ` | `0x2A920` | 270 | UnwindData |  |
| 393 | `?CanPageBeActivated@ProgressCommonDialogBase@@UEAAHW4Direction@@PEAH@Z` | `0x2AA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 559 | `?KillActive@ProgressCommonDialogBase@@UEAAXAEAH@Z` | `0x2AA90` | 113 | UnwindData |  |
| 585 | `?OnChanged@ProgressCommonDialogBase@@UEAAXPEAUIProgress@@PEAUIProgressTask@@@Z` | `0x2AB10` | 96 | UnwindData |  |
| 627 | `?OnEraseBkGnd@ProgressCommonDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x2AB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 637 | `?OnInitDialog@ProgressCommonDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x2ABA0` | 177 | UnwindData |  |
| 661 | `?OnProgressUpdate@ProgressCommonDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x2AC60` | 218 | UnwindData |  |
| 667 | `?OnTimer@ProgressCommonDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x2AD40` | 52 | UnwindData |  |
| 713 | `?ProgressTextCallback@ProgressCommonDialogBase@@SAXW4WDS_EVENT_RESULT@@PEBUWDS_DATA@@PEAX@Z` | `0x2AD80` | 420 | UnwindData |  |
| 746 | `?SetActive@ProgressCommonDialogBase@@UEAAXAEAH@Z` | `0x2AF30` | 1,505 | UnwindData |  |
| 747 | `?SetActive@ProgressWinPEDialogBase@@UEAAXAEAH@Z` | `0x2B520` | 135 | UnwindData |  |
| 771 | `?SetStatusText@ProgressCommonDialogBase@@QEAAXKK@Z` | `0x2B5B0` | 173 | UnwindData |  |
| 775 | `?SetTextOnWindow@ProgressCommonDialogBase@@QEAAXKPEBG@Z` | `0x2B670` | 221 | UnwindData |  |
| 846 | `?v_AnnounceCurrentProgress@ProgressCommonDialogBase@@AEAAXXZ` | `0x2B8A0` | 115 | UnwindData |  |
| 859 | `?v_GetPercentComplete@ProgressCommonDialogBase@@AEAAIPEAUIProgress@@@Z` | `0x2B920` | 94 | UnwindData |  |
| 865 | `?v_ListCreate@ProgressCommonDialogBase@@AEAAIXZ` | `0x2B990` | 995 | UnwindData |  |
| 866 | `?v_ListGetIdx@ProgressCommonDialogBase@@AEAAIXZ` | `0x2BD80` | 160 | UnwindData |  |
| 867 | `?v_ListReset@ProgressCommonDialogBase@@AEAAXXZ` | `0x2BE30` | 177 | UnwindData |  |
| 868 | `?v_ListSetState@ProgressCommonDialogBase@@AEAAXIW4ProgressState@@@Z` | `0x2BEF0` | 74 | UnwindData |  |
| 869 | `?v_ListSetText@ProgressCommonDialogBase@@AEAAXIW4ProgressState@@@Z` | `0x2BF40` | 625 | UnwindData |  |
| 870 | `?v_ListUpdate@ProgressCommonDialogBase@@AEAAXXZ` | `0x2C1C0` | 116 | UnwindData |  |
| 871 | `?v_LoadStr@ProgressCommonDialogBase@@AEAAPEAVUTLString@@I@Z` | `0x2C240` | 130 | UnwindData |  |
| 880 | `?v_SetProgressText@ProgressCommonDialogBase@@AEAAXXZ` | `0x2C2D0` | 648 | UnwindData |  |
| 882 | `?v_TaskGetName@ProgressCommonDialogBase@@AEAAPEAVUTLString@@PEAUIProgress@@@Z` | `0x2C560` | 47 | UnwindData |  |
| 883 | `?v_TaskRegister@ProgressCommonDialogBase@@AEAAXXZ` | `0x2C5A0` | 107 | UnwindData |  |
| 884 | `?v_TaskUnregister@ProgressCommonDialogBase@@AEAAXXZ` | `0x2C620` | 107 | UnwindData |  |
| 1 | `??0?$CComPtr@UIUnknown@@@ATL@@QEAA@AEBV01@@Z` | `0x2C6A0` | 52 | UnwindData |  |
| 5 | `??0?$CComPtr@UIWebBrowser2@@@ATL@@QEAA@AEBV01@@Z` | `0x2C6A0` | 52 | UnwindData |  |
| 2 | `??0?$CComPtr@UIUnknown@@@ATL@@QEAA@H@Z` | `0x2C6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0?$CComPtr@UIUnknown@@@ATL@@QEAA@XZ` | `0x2C6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0?$CComPtr@UIWebBrowser2@@@ATL@@QEAA@H@Z` | `0x2C6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0?$CComPtr@UIWebBrowser2@@@ATL@@QEAA@XZ` | `0x2C6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0?$CComPtrBase@UIUnknown@@@ATL@@IEAA@H@Z` | `0x2C6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0?$CComPtrBase@UIUnknown@@@ATL@@IEAA@XZ` | `0x2C6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0?$CComPtrBase@UIWebBrowser2@@@ATL@@IEAA@H@Z` | `0x2C6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??0?$CComPtrBase@UIWebBrowser2@@@ATL@@IEAA@XZ` | `0x2C6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0?$CComPtr@UIUnknown@@@ATL@@QEAA@PEAUIUnknown@@@Z` | `0x2C6F0` | 52 | UnwindData |  |
| 7 | `??0?$CComPtr@UIWebBrowser2@@@ATL@@QEAA@PEAUIWebBrowser2@@@Z` | `0x2C6F0` | 52 | UnwindData |  |
| 10 | `??0?$CComPtrBase@UIUnknown@@@ATL@@IEAA@PEAUIUnknown@@@Z` | `0x2C730` | 51 | UnwindData |  |
| 13 | `??0?$CComPtrBase@UIWebBrowser2@@@ATL@@IEAA@PEAUIWebBrowser2@@@Z` | `0x2C730` | 51 | UnwindData |  |
| 49 | `??0DUWelcomeDialogBase@@QEAA@AEBV0@@Z` | `0x2E4A0` | 85 | UnwindData |  |
| 50 | `??0DUWelcomeDialogBase@@QEAA@XZ` | `0x2E500` | 59 | UnwindData |  |
| 51 | `??0DWebBrowserEventsImpl@@QEAA@$$QEAV0@@Z` | `0x2E550` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??0DWebBrowserEventsImpl@@QEAA@AEBV0@@Z` | `0x2E550` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `??0DWebBrowserEventsImpl@@QEAA@XZ` | `0x2E580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??0DiskConfigDialogBase@@QEAA@$$QEAV0@@Z` | `0x2E5A0` | 34 | UnwindData |  |
| 58 | `??0DiskConfigDialogBase@@QEAA@AEBV0@@Z` | `0x2E5A0` | 34 | UnwindData |  |
| 59 | `??0DiskConfigDialogBase@@QEAA@XZ` | `0x2E5D0` | 34 | UnwindData |  |
| 65 | `??0EulaDialogBase@@QEAA@AEBV0@@Z` | `0x2E600` | 271 | UnwindData |  |
| 66 | `??0EulaDialogBase@@QEAA@XZ` | `0x2E720` | 57 | UnwindData |  |
| 69 | `??0FinishDialogBase@@QEAA@$$QEAV0@@Z` | `0x2E760` | 83 | UnwindData |  |
| 70 | `??0FinishDialogBase@@QEAA@AEBV0@@Z` | `0x2E760` | 83 | UnwindData |  |
| 71 | `??0FinishDialogBase@@QEAA@XZ` | `0x2E7C0` | 34 | UnwindData |  |
| 77 | `??0HWRequirementsDialogBase@@QEAA@AEBV0@@Z` | `0x2E7F0` | 41 | UnwindData |  |
| 78 | `??0HWRequirementsDialogBase@@QEAA@XZ` | `0x2E820` | 41 | UnwindData |  |
| 79 | `??0IBSImageSelectionDialogBase@@QEAA@AEBV0@@Z` | `0x2E850` | 54 | UnwindData |  |
| 80 | `??0IBSImageSelectionDialogBase@@QEAA@XZ` | `0x2E890` | 39 | UnwindData |  |
| 81 | `??0InstallTypeDialogBase@@QEAA@AEBV0@@Z` | `0x2E8C0` | 77 | UnwindData |  |
| 82 | `??0InstallTypeDialogBase@@QEAA@XZ` | `0x2E920` | 55 | UnwindData |  |
| 103 | `??0SetupCompatDialogBase@@QEAA@AEBV0@@Z` | `0x2E960` | 339 | UnwindData |  |
| 108 | `??0UnattendDialogBase@@QEAA@AEBV0@@Z` | `0x2EAC0` | 61 | UnwindData |  |
| 109 | `??0UnattendDialogBase@@QEAA@XZ` | `0x2EB10` | 41 | UnwindData |  |
| 131 | `??0WelcomeDialogBase@@QEAA@AEBV0@@Z` | `0x2EB40` | 61 | UnwindData |  |
| 132 | `??0WelcomeDialogBase@@QEAA@XZ` | `0x2EB90` | 41 | UnwindData |  |
| 152 | `??1?$CComPtrBase@UIUnknown@@@ATL@@QEAA@XZ` | `0x2EBC0` | 40 | UnwindData |  |
| 153 | `??1?$CComPtrBase@UIWebBrowser2@@@ATL@@QEAA@XZ` | `0x2EBC0` | 40 | UnwindData |  |
| 160 | `??1DUWelcomeDialogBase@@UEAA@XZ` | `0x2F720` | 173 | UnwindData |  |
| 163 | `??1DiskConfigDialogBase@@QEAA@XZ` | `0x2F7E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `??1WDSDiskConfigDialogBase@@QEAA@XZ` | `0x2F7E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `??1EulaDialogBase@@QEAA@XZ` | `0x2F7F0` | 85 | UnwindData |  |
| 168 | `??1FinishDialogBase@@QEAA@XZ` | `0x2F850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `??1WDSFinishDialogBase@@QEAA@XZ` | `0x2F850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `??1HWRequirementsDialogBase@@QEAA@XZ` | `0x2F860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `??1IBSImageSelectionDialogBase@@UEAA@XZ` | `0x2F880` | 78 | UnwindData |  |
| 172 | `??1InstallTypeDialogBase@@QEAA@XZ` | `0x2F8E0` | 115 | UnwindData |  |
| 180 | `??1SetupCompatDialogBase@@QEAA@XZ` | `0x2F960` | 92 | UnwindData |  |
| 182 | `??1UnattendDialogBase@@QEAA@XZ` | `0x2F9D0` | 85 | UnwindData |  |
| 190 | `??1WelcomeDialogBase@@QEAA@XZ` | `0x2FA30` | 85 | UnwindData |  |
| 195 | `??4?$CComPtr@UIUnknown@@@ATL@@QEAAPEAUIUnknown@@AEBV01@@Z` | `0x2FA90` | 94 | UnwindData |  |
| 197 | `??4?$CComPtr@UIWebBrowser2@@@ATL@@QEAAPEAUIWebBrowser2@@AEBV01@@Z` | `0x2FA90` | 94 | UnwindData |  |
| 196 | `??4?$CComPtr@UIUnknown@@@ATL@@QEAAPEAUIUnknown@@PEAU2@@Z` | `0x2FB00` | 94 | UnwindData |  |
| 198 | `??4?$CComPtr@UIWebBrowser2@@@ATL@@QEAAPEAUIWebBrowser2@@PEAU2@@Z` | `0x2FB00` | 94 | UnwindData |  |
| 199 | `??4?$CComPtrBase@UIUnknown@@@ATL@@QEAAAEAV01@AEBV01@@Z` | `0x2FB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `??4?$CComPtrBase@UIWebBrowser2@@@ATL@@QEAAAEAV01@AEBV01@@Z` | `0x2FB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `??4DUWelcomeDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x2FB90` | 75 | UnwindData |  |
| 226 | `??4DiskConfigDialogBase@@QEAAAEAV0@$$QEAV0@@Z` | `0x2FBF0` | 24 | UnwindData |  |
| 227 | `??4DiskConfigDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x2FBF0` | 24 | UnwindData |  |
| 262 | `??4WDSDiskConfigDialogBase@@QEAAAEAV0@$$QEAV0@@Z` | `0x2FBF0` | 24 | UnwindData |  |
| 263 | `??4WDSDiskConfigDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x2FBF0` | 24 | UnwindData |  |
| 232 | `??4EulaDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x2FC10` | 123 | UnwindData |  |
| 240 | `??4IBSImageSelectionDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x2FCA0` | 111 | UnwindData |  |
| 241 | `??4InstallTypeDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x2FD20` | 67 | UnwindData |  |
| 257 | `??4SetupCompatDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x2FD70` | 251 | UnwindData |  |
| 260 | `??4UnattendDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x2FE80` | 51 | UnwindData |  |
| 273 | `??4WDSWelcomeDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x2FE80` | 51 | UnwindData |  |
| 274 | `??4WelcomeDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x2FE80` | 51 | UnwindData |  |
| 285 | `??7?$CComPtrBase@UIUnknown@@@ATL@@QEBA_NXZ` | `0x2FEC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `??7?$CComPtrBase@UIWebBrowser2@@@ATL@@QEBA_NXZ` | `0x2FEC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `??8?$CComPtrBase@UIUnknown@@@ATL@@QEBA_NPEAUIUnknown@@@Z` | `0x2FED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `??8?$CComPtrBase@UIWebBrowser2@@@ATL@@QEBA_NPEAUIWebBrowser2@@@Z` | `0x2FED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `??9?$CComPtrBase@UIUnknown@@@ATL@@QEBA_NPEAUIUnknown@@@Z` | `0x2FEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `??9?$CComPtrBase@UIWebBrowser2@@@ATL@@QEBA_NPEAUIWebBrowser2@@@Z` | `0x2FEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `??D?$CComPtrBase@UIUnknown@@@ATL@@QEBAAEAUIUnknown@@XZ` | `0x2FEF0` | 29 | UnwindData |  |
| 302 | `??D?$CComPtrBase@UIWebBrowser2@@@ATL@@QEBAAEAUIWebBrowser2@@XZ` | `0x2FEF0` | 29 | UnwindData |  |
| 305 | `??M?$CComPtrBase@UIUnknown@@@ATL@@QEBA_NPEAUIUnknown@@@Z` | `0x2FF20` | 1,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `??M?$CComPtrBase@UIWebBrowser2@@@ATL@@QEBA_NPEAUIWebBrowser2@@@Z` | `0x2FF20` | 1,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `?Advise@?$CComPtrBase@UIUnknown@@@ATL@@QEAAJPEAUIUnknown@@AEBU_GUID@@PEAK@Z` | `0x305F0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `?Advise@?$CComPtrBase@UIWebBrowser2@@@ATL@@QEAAJPEAUIUnknown@@AEBU_GUID@@PEAK@Z` | `0x305F0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `?Attach@?$CComPtrBase@UIUnknown@@@ATL@@QEAAXPEAUIUnknown@@@Z` | `0x306F0` | 61 | UnwindData |  |
| 383 | `?Attach@?$CComPtrBase@UIWebBrowser2@@@ATL@@QEAAXPEAUIWebBrowser2@@@Z` | `0x306F0` | 61 | UnwindData |  |
| 386 | `?CanPageBeActivated@DUWelcomeDialogBase@@UEAAHW4Direction@@PEAH@Z` | `0x30910` | 300 | UnwindData |  |
| 387 | `?CanPageBeActivated@GenericWin32UIBase@@UEAAHW4Direction@@PEAH@Z` | `0x30A50` | 487 | UnwindData |  |
| 388 | `?CanPageBeActivated@HWRequirementsDialogBase@@UEAAHW4Direction@@PEAH@Z` | `0x30C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `?CanPageBeActivated@IBSImageSelectionDialogBase@@UEAAHW4Direction@@PEAH@Z` | `0x30C60` | 313 | UnwindData |  |
| 390 | `?CanPageBeActivated@InstallTypeDialogBase@@UEAAHW4Direction@@PEAH@Z` | `0x30DA0` | 333 | UnwindData |  |
| 395 | `?CanPageBeActivated@UnattendDialogBase@@UEAAHW4Direction@@PEAH@Z` | `0x30F00` | 85 | UnwindData |  |
| 398 | `?CanPageBeActivated@WDSWelcomeDialogBase@@UEAAHW4Direction@@PEAH@Z` | `0x30F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `?CanPageBeActivated@WelcomeDialogBase@@UEAAHW4Direction@@PEAH@Z` | `0x30F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `?CoCreateInstance@?$CComPtrBase@UIUnknown@@@ATL@@QEAAJAEBU_GUID@@PEAUIUnknown@@K@Z` | `0x30F80` | 52 | UnwindData |  |
| 410 | `?CoCreateInstance@?$CComPtrBase@UIUnknown@@@ATL@@QEAAJPEBGPEAUIUnknown@@K@Z` | `0x30FC0` | 124 | UnwindData |  |
| 411 | `?CoCreateInstance@?$CComPtrBase@UIWebBrowser2@@@ATL@@QEAAJAEBU_GUID@@PEAUIUnknown@@K@Z` | `0x31050` | 52 | UnwindData |  |
| 412 | `?CoCreateInstance@?$CComPtrBase@UIWebBrowser2@@@ATL@@QEAAJPEBGPEAUIUnknown@@K@Z` | `0x31090` | 124 | UnwindData |  |
| 425 | `?CopyTo@?$CComPtrBase@UIUnknown@@@ATL@@QEAAJPEAPEAUIUnknown@@@Z` | `0x31120` | 59 | UnwindData |  |
| 426 | `?CopyTo@?$CComPtrBase@UIWebBrowser2@@@ATL@@QEAAJPEAPEAUIWebBrowser2@@@Z` | `0x31120` | 59 | UnwindData |  |
| 432 | `?DUWelcomeSetting@DUWelcomeDialogBase@@QEAAPEAVCDUUIWelcomeSetting@@XZ` | `0x31DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `?Detach@?$CComPtrBase@UIUnknown@@@ATL@@QEAAPEAUIUnknown@@XZ` | `0x31DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `?Detach@?$CComPtrBase@UIWebBrowser2@@@ATL@@QEAAPEAUIWebBrowser2@@XZ` | `0x31DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `?DisableNextButton@EulaDialogBase@@QEAAXXZ` | `0x31DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 743 | `?SetActive@HWRequirementsDialogBase@@UEAAXAEAH@Z` | `0x31DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `?DuOptIn@DUWelcomeDialogBase@@AEAAHXZ` | `0x31DE0` | 548 | UnwindData |  |
| 456 | `?EnableNextButton@EulaDialogBase@@QEAAXXZ` | `0x32010` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `?EulaEditSubProc@EulaDialogBase@@SA_JPEAUHWND__@@I_K_J@Z` | `0x32090` | 58 | UnwindData |  |
| 460 | `?EulaSetting@EulaDialogBase@@QEAAPEAVCEulaSetting@@XZ` | `0x320D0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 794 | `?SummarySetting@UnattendDialogBase@@QEAAPEAVCSetupUISummarySetting@@XZ` | `0x320D0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 813 | `?UpgradeSetting@InstallTypeDialogBase@@QEAAPEAVCUpgradeUserSetting@@XZ` | `0x320D0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 822 | `?WDSWelcomeSetting@WDSWelcomeDialogBase@@QEAAPEAVCWDSUIWelcomeSetting@@XZ` | `0x320D0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 825 | `?WelcomeSetting@WelcomeDialogBase@@QEAAPEAVCSetupUIWelcomeSetting@@XZ` | `0x320D0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 480 | `?GetAppTitle@Win32UiAppBase@@MEAAKXZ` | `0x321E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `?GetCancelConfirmationID@Win32UiAppBase@@MEAAKXZ` | `0x321F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 487 | `?GetCancelDialogTitle@WDSUIAppBase@@MEAAKXZ` | `0x32200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `?GetCancelDialogTitle@Win32UiAppBase@@MEAAKXZ` | `0x32200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 489 | `?GetColumns@IBSImageSelectionDialogBase@@UEAAXXZ` | `0x32210` | 204 | UnwindData |  |
| 498 | `?GetMajorEvent@IBSImageSelectionDialogBase@@UEBAPEBGXZ` | `0x322F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `?GetMinorEventDone@IBSImageSelectionDialogBase@@UEBAIXZ` | `0x32300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `?GetMinorEventImageList@IBSImageSelectionDialogBase@@UEBAIXZ` | `0x32310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 506 | `?GetNext@UnattendDialogBase@@QEAAHXZ` | `0x32320` | 106 | UnwindData |  |
| 532 | `?InitPage@DUWelcomeDialogBase@@UEAAXXZ` | `0x32D90` | 316 | UnwindData |  |
| 533 | `?InitPage@EulaDialogBase@@UEAAXXZ` | `0x32EE0` | 101 | UnwindData |  |
| 534 | `?InitPage@HWRequirementsDialogBase@@UEAAXXZ` | `0x32F50` | 226 | UnwindData |  |
| 535 | `?InitPage@IBSImageSelectionDialogBase@@UEAAXXZ` | `0x33040` | 98 | UnwindData |  |
| 536 | `?InitPage@InstallTypeDialogBase@@UEAAXXZ` | `0x330B0` | 91 | UnwindData |  |
| 539 | `?InitPage@UnattendDialogBase@@UEAAXXZ` | `0x33120` | 91 | UnwindData |  |
| 542 | `?InitPage@WelcomeDialogBase@@UEAAXXZ` | `0x33190` | 91 | UnwindData |  |
| 556 | `?IsEqualObject@?$CComPtrBase@UIUnknown@@@ATL@@QEAA_NPEAUIUnknown@@@Z` | `0x33200` | 175 | UnwindData |  |
| 557 | `?IsEqualObject@?$CComPtrBase@UIWebBrowser2@@@ATL@@QEAA_NPEAUIUnknown@@@Z` | `0x33200` | 175 | UnwindData |  |
| 576 | `?NotifyWizCancel@GenericWin32UIBase@@UEAAHAEAH@Z` | `0x33570` | 548 | UnwindData |  |
| 589 | `?OnCommandClean@InstallTypeDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x33AB0` | 146 | UnwindData |  |
| 596 | `?OnCommandDUNo@DUWelcomeDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x33B50` | 182 | UnwindData |  |
| 597 | `?OnCommandDUYes@DUWelcomeDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x33C10` | 134 | UnwindData |  |
| 599 | `?OnCommandEulaYes@EulaDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x33CA0` | 92 | UnwindData |  |
| 604 | `?OnCommandPrivacyStmt@DUWelcomeDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x33D10` | 165 | UnwindData |  |
| 612 | `?OnCommandUpgrade@InstallTypeDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x33DC0` | 146 | UnwindData |  |
| 615 | `?OnCtlColorStatic@EulaDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x33E60` | 173 | UnwindData |  |
| 616 | `?OnCtlColorStatic@GenericWin32UIBase@@QEAA_JI_K_JAEAH@Z` | `0x33F20` | 141 | UnwindData |  |
| 620 | `?OnDestroy@GenericWin32UIBase@@QEAA_JI_K_JAEAH@Z` | `0x33FC0` | 59 | UnwindData |  |
| 631 | `?OnInitDialog@DUWelcomeDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x34320` | 954 | UnwindData |  |
| 632 | `?OnInitDialog@EulaDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x346E0` | 187 | UnwindData |  |
| 633 | `?OnInitDialog@GenericWin32UIBase@@QEAA_JI_K_JAEAH@Z` | `0x347B0` | 141 | UnwindData |  |
| 634 | `?OnInitDialog@HWRequirementsDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x34850` | 198 | UnwindData |  |
| 635 | `?OnInitDialog@InstallTypeDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x34920` | 602 | UnwindData |  |
| 683 | `?ProcessWindowMessage@DUWelcomeDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x352D0` | 212 | UnwindData |  |
| 684 | `?ProcessWindowMessage@DiskConfigDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x353B0` | 64 | UnwindData |  |
| 698 | `?ProcessWindowMessage@WDSDiskConfigDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x353B0` | 64 | UnwindData |  |
| 685 | `?ProcessWindowMessage@EulaDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x35400` | 188 | UnwindData |  |
| 686 | `?ProcessWindowMessage@FinishDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x354D0` | 64 | UnwindData |  |
| 699 | `?ProcessWindowMessage@WDSFinishDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x354D0` | 64 | UnwindData |  |
| 688 | `?ProcessWindowMessage@HWRequirementsDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x35520` | 70 | UnwindData |  |
| 689 | `?ProcessWindowMessage@IBSImageSelectionDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x35570` | 64 | UnwindData |  |
| 700 | `?ProcessWindowMessage@WDSImageSelectionDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x35570` | 64 | UnwindData |  |
| 690 | `?ProcessWindowMessage@InstallTypeDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x35660` | 165 | UnwindData |  |
| 695 | `?ProcessWindowMessage@SetupCompatDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x35710` | 177 | UnwindData |  |
| 696 | `?ProcessWindowMessage@UnattendDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x357D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 721 | `?Release@?$CComPtrBase@UIUnknown@@@ATL@@QEAAXXZ` | `0x35800` | 47 | UnwindData |  |
| 722 | `?Release@?$CComPtrBase@UIWebBrowser2@@@ATL@@QEAAXXZ` | `0x35800` | 47 | UnwindData |  |
| 740 | `?SetActive@DUWelcomeDialogBase@@UEAAXAEAH@Z` | `0x35C60` | 113 | UnwindData |  |
| 741 | `?SetActive@EulaDialogBase@@UEAAXAEAH@Z` | `0x35CE0` | 737 | UnwindData |  |
| 742 | `?SetActive@GenericWin32UIBase@@UEAAXAEAH@Z` | `0x35FD0` | 1,017 | UnwindData |  |
| 744 | `?SetActive@InstallTypeDialogBase@@UEAAXAEAH@Z` | `0x363D0` | 618 | UnwindData |  |
| 756 | `?SetBaseURL@DWebBrowserEventsImpl@@QEAAXPEAG@Z` | `0x36640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | `?SetParent@DWebBrowserEventsImpl@@QEAAXPEAVSetupCompatDialogBase@@@Z` | `0x36650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | `?SetSite@?$CComPtrBase@UIUnknown@@@ATL@@QEAAJPEAUIUnknown@@@Z` | `0x36660` | 131 | UnwindData |  |
| 768 | `?SetSite@?$CComPtrBase@UIWebBrowser2@@@ATL@@QEAAJPEAUIUnknown@@@Z` | `0x36660` | 131 | UnwindData |  |
| 849 | `?v_Chk@SetupCompatDialogBase@@AEAAHK@Z` | `0x39ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 876 | `?v_Set@SetupCompatDialogBase@@AEAAXK@Z` | `0x39EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `??0Win32UiFinishDialogBase@@QEAA@XZ` | `0x39F00` | 46 | UnwindData |  |
| 193 | `??1Win32UiFinishDialogBase@@QEAA@XZ` | `0x3A090` | 61 | UnwindData |  |
| 577 | `?NotifyWizFinish@Win32UiFinishDialogBase@@UEAAHAEAH@Z` | `0x3B140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `?OnCommandRestart@Win32UiFinishDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x3B150` | 45 | UnwindData |  |
| 622 | `?OnDestroy@Win32UiFinishDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x3B190` | 48 | UnwindData |  |
| 645 | `?OnInitDialog@Win32UiFinishDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x3B1D0` | 589 | UnwindData |  |
| 670 | `?OnTimer@Win32UiFinishDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x3B430` | 441 | UnwindData |  |
| 752 | `?SetActive@Win32UiFinishDialogBase@@UEAAXAEAH@Z` | `0x3C9A0` | 427 | UnwindData |  |
| 110 | `??0WDSDeprecateDialogBase@@QEAA@AEBV0@@Z` | `0x3E5B0` | 41 | UnwindData |  |
| 111 | `??0WDSDeprecateDialogBase@@QEAA@XZ` | `0x3E5E0` | 41 | UnwindData |  |
| 112 | `??0WDSDiskConfigDialogBase@@QEAA@$$QEAV0@@Z` | `0x3E610` | 34 | UnwindData |  |
| 113 | `??0WDSDiskConfigDialogBase@@QEAA@AEBV0@@Z` | `0x3E610` | 34 | UnwindData |  |
| 114 | `??0WDSDiskConfigDialogBase@@QEAA@XZ` | `0x3E640` | 34 | UnwindData |  |
| 115 | `??0WDSFinishDialogBase@@QEAA@$$QEAV0@@Z` | `0x3E670` | 83 | UnwindData |  |
| 116 | `??0WDSFinishDialogBase@@QEAA@AEBV0@@Z` | `0x3E670` | 83 | UnwindData |  |
| 117 | `??0WDSFinishDialogBase@@QEAA@XZ` | `0x3E6D0` | 34 | UnwindData |  |
| 118 | `??0WDSImageSelectionDialogBase@@QEAA@$$QEAV0@@Z` | `0x3E700` | 34 | UnwindData |  |
| 119 | `??0WDSImageSelectionDialogBase@@QEAA@AEBV0@@Z` | `0x3E700` | 34 | UnwindData |  |
| 120 | `??0WDSImageSelectionDialogBase@@QEAA@XZ` | `0x3E730` | 34 | UnwindData |  |
| 121 | `??0WDSProgressDialogBase@@QEAA@$$QEAV0@@Z` | `0x3E760` | 45 | UnwindData |  |
| 122 | `??0WDSProgressDialogBase@@QEAA@AEBV0@@Z` | `0x3E760` | 45 | UnwindData |  |
| 123 | `??0WDSProgressDialogBase@@QEAA@XZ` | `0x3E7A0` | 45 | UnwindData |  |
| 127 | `??0WDSWaitingForServerDialogBase@@QEAA@AEBV0@@Z` | `0x3E7E0` | 69 | UnwindData |  |
| 128 | `??0WDSWaitingForServerDialogBase@@QEAA@XZ` | `0x3E830` | 51 | UnwindData |  |
| 129 | `??0WDSWelcomeDialogBase@@QEAA@AEBV0@@Z` | `0x3E870` | 61 | UnwindData |  |
| 130 | `??0WDSWelcomeDialogBase@@QEAA@XZ` | `0x3E8C0` | 41 | UnwindData |  |
| 183 | `??1WDSDeprecateDialogBase@@QEAA@XZ` | `0x3ED70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `??1WDSImageSelectionDialogBase@@UEAA@XZ` | `0x3ED90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `??1WDSWaitingForServerDialogBase@@UEAA@XZ` | `0x3EDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `??1WDSWelcomeDialogBase@@QEAA@XZ` | `0x3EDC0` | 85 | UnwindData |  |
| 272 | `??4WDSWaitingForServerDialogBase@@QEAAAEAV0@AEBV0@@Z` | `0x3EE20` | 59 | UnwindData |  |
| 396 | `?CanPageBeActivated@WDSDeprecateDialogBase@@UEAAHW4Direction@@PEAH@Z` | `0x3F230` | 88 | UnwindData |  |
| 397 | `?CanPageBeActivated@WDSImageSelectionDialogBase@@UEAAHW4Direction@@PEAH@Z` | `0x3F290` | 230 | UnwindData |  |
| 479 | `?GetAppTitle@WDSUIAppBase@@MEAAKXZ` | `0x3F9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `?GetCancelConfirmationID@WDSUIAppBase@@MEAAKXZ` | `0x3F9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `?GetColumns@WDSImageSelectionDialogBase@@UEAAXXZ` | `0x3F9D0` | 204 | UnwindData |  |
| 499 | `?GetMajorEvent@WDSImageSelectionDialogBase@@UEBAPEBGXZ` | `0x3FAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `?GetMinorEventDone@WDSImageSelectionDialogBase@@UEBAIXZ` | `0x3FAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `?GetMinorEventImageList@WDSImageSelectionDialogBase@@UEBAIXZ` | `0x3FAD0` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `?InitPage@WDSDeprecateDialogBase@@UEAAXXZ` | `0x3FF50` | 507 | UnwindData |  |
| 541 | `?InitPage@WDSWelcomeDialogBase@@UEAAXXZ` | `0x40160` | 316 | UnwindData |  |
| 560 | `?KillActive@WDSWaitingForServerDialogBase@@UEAAXAEAH@Z` | `0x40480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 591 | `?OnCommandContinue@WDSWelcomeDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x404A0` | 107 | UnwindData |  |
| 606 | `?OnCommandReboot@WDSDeprecateDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x40520` | 373 | UnwindData |  |
| 640 | `?OnInitDialog@WDSDeprecateDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x406A0` | 72 | UnwindData |  |
| 641 | `?OnInitDialog@WDSWaitingForServerDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x406F0` | 168 | UnwindData |  |
| 668 | `?OnTimer@WDSWaitingForServerDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x407A0` | 112 | UnwindData |  |
| 697 | `?ProcessWindowMessage@WDSDeprecateDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x408C0` | 120 | UnwindData |  |
| 701 | `?ProcessWindowMessage@WDSProgressDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x40940` | 63 | UnwindData |  |
| 702 | `?ProcessWindowMessage@WDSWaitingForServerDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x40990` | 105 | UnwindData |  |
| 703 | `?ProcessWindowMessage@WDSWelcomeDialogBase@@UEAAHPEAUHWND__@@I_K_JAEA_JK@Z` | `0x40A00` | 108 | UnwindData |  |
| 749 | `?SetActive@WDSWaitingForServerDialogBase@@UEAAXAEAH@Z` | `0x40A80` | 181 | UnwindData |  |
| 385 | `?BeforeNavigate@DWebBrowserEventsImpl@@AEAAJPEAGJ0PEAUtagVARIANT@@0PEAF@Z` | `0x43170` | 375 | UnwindData |  |
| 496 | `?GetIDsOfNames@DWebBrowserEventsImpl@@EEAAJAEBU_GUID@@PEAPEAGIKPEAJ@Z` | `0x432F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `?GetTypeInfo@DWebBrowserEventsImpl@@EEAAJIKPEAPEAUITypeInfo@@@Z` | `0x432F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | `?GetTypeInfoCount@DWebBrowserEventsImpl@@EEAAJPEAI@Z` | `0x432F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `?Invoke@DWebBrowserEventsImpl@@EEAAJJAEBU_GUID@@KGPEAUtagDISPPARAMS@@PEAUtagVARIANT@@PEAUtagEXCEPINFO@@PEAI@Z` | `0x43300` | 61 | UnwindData |  |
| 718 | `?QueryInterface@DWebBrowserEventsImpl@@EEAAJAEBU_GUID@@PEAPEAX@Z` | `0x43350` | 138 | UnwindData |  |
| 104 | `??0SetupCompatDialogBase@@QEAA@XZ` | `0x439A0` | 138 | UnwindData |  |
| 394 | `?CanPageBeActivated@SetupCompatDialogBase@@UEAAHW4Direction@@PEAH@Z` | `0x454E0` | 581 | UnwindData |  |
| 427 | `?CreateCopyOfReport@SetupCompatDialogBase@@QEAAXIPEBG@Z` | `0x46210` | 419 | UnwindData |  |
| 428 | `?CreateInternetExplorerControl@SetupCompatDialogBase@@QEAA?AV?$CComPtr@UIWebBrowser2@@@ATL@@PEAUHWND__@@V_U_RECT@3@K@Z` | `0x467A0` | 957 | UnwindData |  |
| 440 | `?DisableNextButton@SetupCompatDialogBase@@QEAAXXZ` | `0x46DF0` | 296 | UnwindData |  |
| 457 | `?EnableNextButton@SetupCompatDialogBase@@QEAAXXZ` | `0x46F50` | 326 | UnwindData |  |
| 590 | `?OnCommandContinue@SetupCompatDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x489F0` | 104 | UnwindData |  |
| 602 | `?OnCommandLoadDriver@SetupCompatDialogBase@@QEAA_JGGPEAUHWND__@@AEAH@Z` | `0x48A60` | 44 | UnwindData |  |
| 638 | `?OnInitDialog@SetupCompatDialogBase@@QEAA_JI_K_JAEAH@Z` | `0x48D00` | 1,337 | UnwindData |  |
| 748 | `?SetActive@SetupCompatDialogBase@@UEAAXAEAH@Z` | `0x4ACC0` | 1,561 | UnwindData |  |
| 829 | `?WriteHtmlReport@SetupCompatDialogBase@@QEAAXPEAG_K@Z` | `0x4BE10` | 534 | UnwindData |  |
| 347 | `??_7SetupCreateProgressWnd@@6B@` | `0x6B028` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `??_7Win32UiAppBase@@6B@` | `0x6B050` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `??_7GenericWin32UIBase@@6B@` | `0x6B0C8` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `??_7WDSUIAppBase@@6B@` | `0x6B140` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `??_7PantherCallback@@6B@` | `0x6B1B8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `??_7PantherRMEHandler@@6B@` | `0x6B1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `??_7ExtendPartitionCallback@@6B@` | `0x6B1E0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `??_7Win32UiDiskConfigBase@@6B@` | `0x6B1F8` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `??_7MediaDriverListDialogBase@@6B@` | `0x6B258` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `??_7ProgressCommonDialogBase@@6BWizardHandler@@@` | `0x6B2D8` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `??_7FormatPartitionCallback@@6B@` | `0x6B370` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `??_7CancelDialogBase@@6B@` | `0x6B388` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `??_7DriveInfoCallback@@6B@` | `0x6B3E8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `??_7OnlineDiskCallback@@6B@` | `0x6B400` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `??_7ProgressWinPEDialogBase@@6BIProgressEvent@@@` | `0x6B418` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `??_7DeletePartitionCallback@@6B@` | `0x6B428` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `??_7DCCallbackData@@6B@` | `0x6B440` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `??_7Win32UiDriverListDialogBase@@6B@` | `0x6B458` | 200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `??_7CreatePartitionCallback@@6B@` | `0x6B520` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `??_7PKDialogBase@@6B@` | `0x6B538` | 104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `??_7ProgressCommonDialogBase@@6BIProgressEvent@@@` | `0x6B5A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `??_7DriverListCallback@@6B@` | `0x6B5B0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `??_7NDProgress@@6B@` | `0x6B5C8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `??_7ProgressWinPEDialogBase@@6BWizardHandler@@@` | `0x6B5D8` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `??_7Win32UiWelcomeDialogBase@@6B@` | `0x6B650` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `??_7Win32uiImageSelectionDialogBase@@6B@` | `0x6B6B0` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `??_7Win32UiFinishDialogBase@@6B@` | `0x6B748` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `??_7Win32UiDeprecateDialogBase@@6B@` | `0x6B7A8` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `??_7EulaDialogBase@@6B@` | `0x6B850` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `??_7HWRequirementsDialogBase@@6B@` | `0x6B8B0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `??_7UnattendDialogBase@@6B@` | `0x6BA90` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `??_7SetupCompatDialogBase@@6B@` | `0x6BAF0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `??_7DiskConfigDialogBase@@6B@` | `0x6BC80` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `??_7IBSImageSelectionDialogBase@@6B@` | `0x6BF90` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `??_7DUWelcomeDialogBase@@6B@` | `0x6C028` | 680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `??_7DWebBrowserEventsImpl@@6B@` | `0x6C2D0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `??_7WelcomeDialogBase@@6B@` | `0x6C370` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `??_7InstallTypeDialogBase@@6B@` | `0x6C490` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `??_7FinishDialogBase@@6B@` | `0x6C500` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `??_7WDSImageSelectionDialogBase@@6B@` | `0x6C670` | 248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `??_7WDSFinishDialogBase@@6B@` | `0x6C768` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `??_7WDSWaitingForServerDialogBase@@6B@` | `0x6C888` | 104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `??_7WDSProgressDialogBase@@6BIProgressEvent@@@` | `0x6C8F0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `??_7WDSWelcomeDialogBase@@6B@` | `0x6C9D0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `??_7WDSProgressDialogBase@@6BWizardHandler@@@` | `0x6CC30` | 104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `??_7WDSDeprecateDialogBase@@6B@` | `0x6CC98` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `??_7WDSDiskConfigDialogBase@@6B@` | `0x6CCF8` | 23,044 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `?TIMER_INTERVAL@NDProgress@@0KB` | `0x726FC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 796 | `?TIMEOUT_DEVICE@Win32UiDriverListDialogBase@@1HB` | `0x72708` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `?ID_TIMER@NDProgress@@0KB` | `0x7270C` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `?PROGRESS_BAR_MAX@NDProgress@@0KB` | `0x72718` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `?TIMEOUT_MEDIADEVICE@MediaDriverListDialogBase@@0HB` | `0x72768` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | `?ID_DEVICE_TIMER@Win32UiDriverListDialogBase@@1HB` | `0x72778` | 9,204 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 832 | `?m_ProgressBarMax@WDSWaitingForServerDialogBase@@0HB` | `0x72778` | 9,204 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 523 | `?ID_REBOOT_TIMER@Win32UiFinishDialogBase@@1HB` | `0x74B6C` | 28,748 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `?TIME_REBOOT@Win32UiFinishDialogBase@@1HB` | `0x74B6C` | 28,748 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | `?m_TimerId@WDSWaitingForServerDialogBase@@0_KB` | `0x7BBB8` | 170,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 841 | `?s_OldDiskConfigProc@Win32UiDiskConfigBase@@0P6A_JPEAUHWND__@@I_K_J@ZEA` | `0xA56F0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 843 | `?s_OldSizeEditProc@Win32UiDiskConfigBase@@0P6A_JPEAUHWND__@@I_K_J@ZEA` | `0xA56F8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `?s_hwndBrowse@Win32UiDriverListDialogBase@@0PEAUHWND__@@EA` | `0xA5700` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `?s_fQuickDeviceTimeout@MediaDriverListDialogBase@@0HA` | `0xA5708` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | `?s_FirstTime@EulaDialogBase@@0HA` | `0xA5718` | 9,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `?DUProgressPage@@3VWizard_PageDesciption@@A` | `0xA7A78` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `?SetupCompliancePage@@3VWizard_PageDesciption@@A` | `0xA7BA8` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `?ProductkeyPage@@3VWizard_PageDesciption@@A` | `0xA7C40` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `?EulaPage@@3VWizard_PageDesciption@@A` | `0xA7C78` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `?ProgressWinPEPage@@3VWizard_PageDesciption@@A` | `0xA7CD0` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `?FinishPage@@3VWizard_PageDesciption@@A` | `0xA7D08` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `?IBSImageSelectionPage@@3VWizard_PageDesciption@@A` | `0xA7D58` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `?DUWelcomePage@@3VWizard_PageDesciption@@A` | `0xA7DD0` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `?AppCompatProgressPage@@3VWizard_PageDesciption@@A` | `0xA7E08` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `?DriverListPage@@3VWizard_PageDesciption@@A` | `0xA7E98` | 104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `?IBSLanguageNeutralSelectionPage@@3VWizard_PageDesciption@@A` | `0xA7F00` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 572 | `?MediaDriverListPage@@3VWizard_PageDesciption@@A` | `0xA7F38` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 777 | `?SetupProtoPages@@3VProtoPageList@@A` | `0xA7F70` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `?CancelPage@@3VWizard_PageDesciption@@A` | `0xA8050` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 711 | `?ProgressPage@@3VWizard_PageDesciption@@A` | `0xA80C8` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `?IBSLanguageSelectionPage@@3VWizard_PageDesciption@@A` | `0xA8100` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 441 | `?DiskConfigPage@@3VWizard_PageDesciption@@A` | `0xA8178` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | `?WelcomePage@@3VWizard_PageDesciption@@A` | `0xA81D0` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 551 | `?InstallTypePage@@3VWizard_PageDesciption@@A` | `0xA8228` | 552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 672 | `?OnlineProtoPages@@3VProtoPageList@@A` | `0xA8450` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `?WDSDiskConfigPage@@3VWizard_PageDesciption@@A` | `0xA8650` | 216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 816 | `?WDSFinishPage@@3VWizard_PageDesciption@@A` | `0xA8728` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `?WDSLanguageSelectionPage@@3VWizard_PageDesciption@@A` | `0xA8780` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 820 | `?WDSProtoPages@@3VProtoPageList@@A` | `0xA87E0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `?WDSImageSelectionPage@@3VWizard_PageDesciption@@A` | `0xA88A0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 821 | `?WDSWelcomePage@@3VWizard_PageDesciption@@A` | `0xA8930` | 328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | `?WDSProgressPage@@3VWizard_PageDesciption@@A` | `0xA8A78` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `?WDSDriverListPage@@3VWizard_PageDesciption@@A` | `0xA8B48` | 1,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `?ProgressPage@PantherInterface@@2PEAUHWND__@@EA` | `0xA9258` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 546 | `?InputEnd@PantherInterface@@2PEAXEA` | `0xA9260` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 839 | `?pRMEHandler@PantherInterface@@2PEAVPantherRMEHandler@@EA` | `0xA9268` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 830 | `?bDownlevel@PantherInterface@@2HA` | `0xA9270` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | `?g_ModuleId@PantherInterface@@2PEAXEA` | `0xA9278` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 828 | `?WizUI@PantherInterface@@2PEAVWizardUI@@EA` | `0xA9280` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 838 | `?pBlackboard@PantherInterface@@2PEAU_BLACKBOARD@@EA` | `0xA9288` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 835 | `?m_hProgressTextMutex@ProgressCommonDialogBase@@0PEAXEA` | `0xA92A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 836 | `?m_hTextFont@ProgressCommonDialogBase@@0PEAUHFONT__@@EA` | `0xA92B0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 837 | `?m_pProgressStatusText@ProgressCommonDialogBase@@0PEAVCCtlText@@EA` | `0xA92B8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 834 | `?m_hDlg@ProgressCommonDialogBase@@0PEAUHWND__@@EA` | `0xA92C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `?s_OldEulaEditProc@EulaDialogBase@@0P6A_JPEAUHWND__@@I_K_J@ZEA` | `0xA92D0` | 0 | Indeterminate |  |
