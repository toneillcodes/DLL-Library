# Binary Specification: atl.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\atl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6cfc2475c5b23062f193d7ce26cfa647765763a4f62a3f5bbfa9153686e71d98`
* **Total Exported Functions:** 54

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 32 | `AtlInternalQueryInterface` | `0x1010` | 63 | UnwindData |  |
| 30 | `AtlComPtrAssign` | `0x11D0` | 93 | UnwindData |  |
| 15 | `AtlModuleGetClassObject` | `0x1A40` | 366 | UnwindData |  |
| 16 | `AtlModuleInit` | `0x2A00` | 484 | UnwindData |  |
| 21 | `AtlModuleTerm` | `0x2BF0` | 18 | UnwindData |  |
| 31 | `AtlComQIPtrAssign` | `0x3720` | 29 | UnwindData |  |
| 54 | `AtlGetObjectSourceInterface` | `0x5100` | 862 | UnwindData |  |
| 52 | `AtlIPersistPropertyBag_Load` | `0x5470` | 911 | UnwindData |  |
| 53 | `AtlIPersistPropertyBag_Save` | `0x5810` | 991 | UnwindData |  |
| 60 | `AtlIPersistStreamInit_GetSizeMax` | `0x5C00` | 20 | UnwindData |  |
| 50 | `AtlIPersistStreamInit_Load` | `0x5EB0` | 390 | UnwindData |  |
| 51 | `AtlIPersistStreamInit_Save` | `0x6040` | 30 | UnwindData |  |
| 62 | `DllRegisterServer` | `0x76B0` | 23,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `DllUnregisterServer` | `0x76B0` | 23,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `AtlAdvise` | `0xD0A0` | 182 | UnwindData |  |
| 41 | `AtlAxAttachControl` | `0xD160` | 179 | UnwindData |  |
| 39 | `AtlAxCreateControl` | `0xD220` | 39 | UnwindData |  |
| 40 | `AtlAxCreateControlEx` | `0xD250` | 301 | UnwindData |  |
| 38 | `AtlAxCreateDialogA` | `0xD390` | 358 | UnwindData |  |
| 37 | `AtlAxCreateDialogW` | `0xD500` | 358 | UnwindData |  |
| 36 | `AtlAxDialogBoxA` | `0xD670` | 359 | UnwindData |  |
| 35 | `AtlAxDialogBoxW` | `0xD7E0` | 359 | UnwindData |  |
| 47 | `AtlAxGetControl` | `0xD950` | 67 | UnwindData |  |
| 48 | `AtlAxGetHost` | `0xD9A0` | 67 | UnwindData |  |
| 42 | `AtlAxWinInit` | `0xD9F0` | 305 | UnwindData |  |
| 26 | `AtlCreateTargetDC` | `0xDB30` | 149 | UnwindData |  |
| 29 | `AtlDevModeW2A` | `0xDBD0` | 272 | UnwindData |  |
| 12 | `AtlFreeMarshalStream` | `0xDCF0` | 73 | UnwindData |  |
| 34 | `AtlGetVersion` | `0xDD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `AtlHiMetricToPixel` | `0xDD50` | 214 | UnwindData |  |
| 13 | `AtlMarshalPtrInProc` | `0xDE30` | 160 | UnwindData |  |
| 43 | `AtlModuleAddCreateWndData` | `0xDEE0` | 142 | UnwindData |  |
| 58 | `AtlModuleAddTermFunc` | `0xDF80` | 160 | UnwindData |  |
| 44 | `AtlModuleExtractCreateWndData` | `0xE030` | 152 | UnwindData |  |
| 56 | `AtlModuleLoadTypeLib` | `0xE0D0` | 534 | UnwindData |  |
| 17 | `AtlModuleRegisterClassObjects` | `0xE2F0` | 128 | UnwindData |  |
| 18 | `AtlModuleRegisterServer` | `0xE380` | 260 | UnwindData |  |
| 19 | `AtlModuleRegisterTypeLib` | `0xE490` | 478 | UnwindData |  |
| 46 | `AtlModuleRegisterWndClassInfoA` | `0xE680` | 536 | UnwindData |  |
| 45 | `AtlModuleRegisterWndClassInfoW` | `0xE8A0` | 536 | UnwindData |  |
| 20 | `AtlModuleRevokeClassObjects` | `0xEAC0` | 105 | UnwindData |  |
| 55 | `AtlModuleUnRegisterTypeLib` | `0xEB30` | 251 | UnwindData |  |
| 22 | `AtlModuleUnregisterServer` | `0xEC40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `AtlModuleUnregisterServerEx` | `0xEC50` | 228 | UnwindData |  |
| 23 | `AtlModuleUpdateRegistryFromResourceD` | `0xED40` | 543 | UnwindData |  |
| 28 | `AtlPixelToHiMetric` | `0xEF70` | 190 | UnwindData |  |
| 49 | `AtlRegisterClassCategoriesHelper` | `0xF040` | 252 | UnwindData |  |
| 25 | `AtlSetErrorInfo` | `0xF150` | 538 | UnwindData |  |
| 59 | `AtlSetErrorInfo2` | `0xF370` | 301 | UnwindData |  |
| 11 | `AtlUnadvise` | `0xF4B0` | 165 | UnwindData |  |
| 14 | `AtlUnmarshalPtr` | `0xF560` | 107 | UnwindData |  |
| 24 | `AtlWaitWithMessageLoop` | `0xF5E0` | 180 | UnwindData |  |
| 33 | `DllCanUnloadNow` | `0xF6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `DllGetClassObject` | `0xF6C0` | 0 | Indeterminate |  |
