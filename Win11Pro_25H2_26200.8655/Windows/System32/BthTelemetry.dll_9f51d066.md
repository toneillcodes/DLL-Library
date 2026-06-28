# Binary Specification: BthTelemetry.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\BthTelemetry.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9f51d066c3faa513a9bc71fa7d49b9cb90aad71964b9cbdbdbd94414d381a5e5`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `BthProcessEventDataDword` | `0xB590` | 237 | UnwindData |  |
| 4 | `BthProcessEventOccurrence` | `0xB690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `BthProcessEventOccurrenceBthaddr` | `0xB6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `BthProcessEventOccurrenceResult` | `0xB6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `BthProcessEventOccurrenceResultBthaddr` | `0xB6C0` | 13,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `BthCollectFingerprintInfo` | `0xEA70` | 4,673 | UnwindData |  |
| 2 | `BthCollectRadioPerformanceInfo` | `0x13590` | 707 | UnwindData |  |
