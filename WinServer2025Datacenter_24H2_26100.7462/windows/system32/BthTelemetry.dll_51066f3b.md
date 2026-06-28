# Binary Specification: BthTelemetry.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\BthTelemetry.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `51066f3b30452affa36c44ece71d7a34963620a65ed2e6832c6da4459fb077a6`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `BthProcessEventDataDword` | `0xB4C0` | 237 | UnwindData |  |
| 4 | `BthProcessEventOccurrence` | `0xB5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `BthProcessEventOccurrenceBthaddr` | `0xB5D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `BthProcessEventOccurrenceResult` | `0xB5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `BthProcessEventOccurrenceResultBthaddr` | `0xB5F0` | 13,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `BthCollectFingerprintInfo` | `0xE990` | 4,673 | UnwindData |  |
| 2 | `BthCollectRadioPerformanceInfo` | `0x14010` | 707 | UnwindData |  |
