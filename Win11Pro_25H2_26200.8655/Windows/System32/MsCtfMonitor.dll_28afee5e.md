# Binary Specification: MsCtfMonitor.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MsCtfMonitor.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `28afee5e95c7a994ab2a4dcc0524da81c5076ae055895e0e8214deff5f56fbc5`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x9D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x9D20` | 248 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x9E20` | 538 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xA040` | 340 | UnwindData |  |
| 5 | `DoMsCtfMonitor` | `0xAB00` | 2,175 | UnwindData |  |
| 6 | `InitLocalMsCtfMonitor` | `0xB5D0` | 220 | UnwindData |  |
| 7 | `UninitLocalMsCtfMonitor` | `0xB6C0` | 143 | UnwindData |  |
