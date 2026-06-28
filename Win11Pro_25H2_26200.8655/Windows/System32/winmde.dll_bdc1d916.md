# Binary Specification: winmde.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\winmde.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bdc1d916ac53caa32a925cc4b2dfcbe16bb67b645568c14066c2a828fe73c170`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x41190` | 12,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x41190` | 12,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x44180` | 50 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x441C0` | 83 | UnwindData |  |
| 6 | `MFCreateWMPMDEOpCenter` | `0x44530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MFCreateWinMDEOpCenter` | `0x44550` | 31,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MFCreateNetVRoot` | `0x4C140` | 473 | UnwindData |  |
