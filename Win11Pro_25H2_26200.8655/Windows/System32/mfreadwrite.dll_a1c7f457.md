# Binary Specification: mfreadwrite.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mfreadwrite.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a1c7f457fa01cb6418b6a0a512af9b5e914e562d68669e0d98b7e7661ca33e2e`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `MFCreateSourceReaderFromMediaSource` | `0x5EF40` | 224 | UnwindData |  |
| 3 | `MFCreateSinkWriterFromMediaSink` | `0x61480` | 40 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x667E0` | 18,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x6AFF0` | 20,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MFCreateSinkWriterFromURL` | `0x6FF50` | 402 | UnwindData |  |
| 7 | `MFCreateSourceReaderFromURL` | `0x700F0` | 40 | UnwindData |  |
| 5 | `MFCreateSourceReaderFromByteStream` | `0x7E5C0` | 40 | UnwindData |  |
