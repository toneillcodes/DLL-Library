# Binary Specification: DispBroker.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\DispBroker.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6da34f6306585cf49de395be8e9104240c0b90ccc4e99ab7fc9aa370abd494c1`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DispBrokerTraceLogHelper` | `0x154F0` | 193 | UnwindData |  |
| 4 | `DllCanUnloadNow` | `0x17E10` | 60 | UnwindData |  |
| 5 | `DllGetActivationFactory` | `0x26470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllGetClassObject` | `0x26480` | 65 | UnwindData |  |
| 1 | `DispBrokerTraceLogCallback` | `0x26A80` | 61 | UnwindData |  |
| 2 | `DispBrokerTraceLogCaptureRingBuffer` | `0x26AD0` | 44 | UnwindData |  |
