# Binary Specification: dxtrans.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dxtrans.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c97a3103ccf0b02cbde9b358c924c99d86cd24769f62c1d6f5334b312a0dabe1`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `DllRegisterServer` | `0x4550` | 6,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DllUnregisterServer` | `0x4550` | 6,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllCanUnloadNow` | `0x5FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllEnumClassObjects` | `0x5FD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllGetClassObject` | `0x6020` | 14,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `?DXConstOverArray@@YAXPEAVDXPMSAMPLE@@AEBV1@K@Z` | `0x9910` | 230 | UnwindData |  |
| 2 | `?DXConstUnderArray@@YAXPEAVDXPMSAMPLE@@AEBV1@K@Z` | `0x9A00` | 123 | UnwindData |  |
| 3 | `?DXDitherArray@@YAXPEBUDXDITHERDESC@@@Z` | `0x9A90` | 269 | UnwindData |  |
| 4 | `?DXLinearInterpolateArray@@YAXPEBVDXBASESAMPLE@@PEAUDXLIMAPINFO@@PEAV1@K@Z` | `0x9BB0` | 216 | UnwindData |  |
| 5 | `?DXOverArray@@YAXPEAVDXPMSAMPLE@@PEBV1@K@Z` | `0x9C90` | 135 | UnwindData |  |
| 6 | `?DXOverArrayMMX@@YAXPEAVDXPMSAMPLE@@PEBV1@K@Z` | `0x9C90` | 135 | UnwindData |  |
