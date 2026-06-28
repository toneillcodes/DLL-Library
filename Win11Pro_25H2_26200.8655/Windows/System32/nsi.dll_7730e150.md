# Binary Specification: nsi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\nsi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7730e150a0305a2c5aa8a1040dd6fc5899428ed7d2297a5dc5e39564b2132adc`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `NsiGetParameterEx` | `0x1010` | 30 | UnwindData |  |
| 7 | `NsiEnumerateObjectsAllParametersEx` | `0x1140` | 33 | UnwindData |  |
| 2 | `NsiAllocateAndGetTable` | `0x1250` | 1,638 | UnwindData |  |
| 6 | `NsiEnumerateObjectsAllParameters` | `0x18C0` | 148 | UnwindData |  |
| 13 | `NsiGetAllPersistentParametersWithMask` | `0x1B00` | 135 | UnwindData |  |
| 3 | `NsiCancelChangeNotification` | `0x1B90` | 58 | UnwindData |  |
| 19 | `NsiRequestChangeNotification` | `0x1BD0` | 62 | UnwindData |  |
| 20 | `NsiRequestChangeNotificationEx` | `0x1C20` | 89 | UnwindData |  |
| 22 | `NsiSetAllParametersEx` | `0x1C80` | 59 | UnwindData |  |
| 21 | `NsiSetAllParameters` | `0x1CD0` | 146 | UnwindData |  |
| 25 | `NsiSetParameter` | `0x1D70` | 160 | UnwindData |  |
| 26 | `NsiSetParameterEx` | `0x1E20` | 50 | UnwindData |  |
| 5 | `NsiDeregisterChangeNotificationEx` | `0x1E60` | 59 | UnwindData |  |
| 18 | `NsiRegisterChangeNotificationEx` | `0x1EB0` | 73 | UnwindData |  |
| 11 | `NsiGetAllParameters` | `0x2150` | 144 | UnwindData |  |
| 15 | `NsiGetParameter` | `0x2390` | 108 | UnwindData |  |
| 12 | `NsiGetAllParametersEx` | `0x25B0` | 34 | UnwindData |  |
| 10 | `NsiFreeTable` | `0x2740` | 157 | UnwindData |  |
| 14 | `NsiGetObjectSecurity` | `0x2B60` | 52 | UnwindData |  |
| 24 | `NsiSetObjectSecurity` | `0x2BA0` | 52 | UnwindData |  |
| 1 | `NsiAllocateAndGetPersistentDataWithMaskTable` | `0x2BE0` | 621 | UnwindData |  |
| 4 | `NsiDeregisterChangeNotification` | `0x2E60` | 77 | UnwindData |  |
| 8 | `NsiEnumerateObjectsAllPersistentParametersWithMask` | `0x2EC0` | 193 | UnwindData |  |
| 9 | `NsiFreePersistentDataWithMaskTable` | `0x2F90` | 115 | UnwindData |  |
| 17 | `NsiRegisterChangeNotification` | `0x3010` | 124 | UnwindData |  |
| 23 | `NsiSetAllPersistentParametersWithMask` | `0x30A0` | 178 | UnwindData |  |
