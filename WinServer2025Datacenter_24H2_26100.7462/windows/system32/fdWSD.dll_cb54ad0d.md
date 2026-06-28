# Binary Specification: fdWSD.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\fdWSD.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cb54ad0db6d1edac56688c17bef42bc5ca60fd76b1d78acbc8002fccd679261e`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x6160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x6180` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x63E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x63F0` | 127 | UnwindData |  |
| 5 | `FdphostSessionChange` | `0x6480` | 20 | UnwindData |  |
| 6 | `FdphostSetComContext` | `0x64A0` | 69 | UnwindData |  |
| 7 | `FdphostSetSharedService` | `0x64F0` | 59 | UnwindData |  |
