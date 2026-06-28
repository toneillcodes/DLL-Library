# Binary Specification: DispBroker.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DispBroker.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1719666ee32e6e343bc4594599d104ffd3c4f45d9fd540eae8ad81531bfa6a55`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DispBrokerTraceLogHelper` | `0x144C0` | 193 | UnwindData |  |
| 4 | `DllCanUnloadNow` | `0x16A70` | 60 | UnwindData |  |
| 5 | `DllGetActivationFactory` | `0x280F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllGetClassObject` | `0x28100` | 65 | UnwindData |  |
| 1 | `DispBrokerTraceLogCallback` | `0x29640` | 61 | UnwindData |  |
| 2 | `DispBrokerTraceLogCaptureRingBuffer` | `0x29690` | 44 | UnwindData |  |
