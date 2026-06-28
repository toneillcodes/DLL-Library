# Binary Specification: mfreadwrite.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mfreadwrite.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fbb1093e19baa466828285b4fa9ca7211deb7550dce9dbd451737021e90fe4f0`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `MFCreateSourceReaderFromMediaSource` | `0x5F1F0` | 224 | UnwindData |  |
| 3 | `MFCreateSinkWriterFromMediaSink` | `0x61730` | 40 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x66A90` | 18,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x6B2A0` | 20,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MFCreateSinkWriterFromURL` | `0x70200` | 402 | UnwindData |  |
| 7 | `MFCreateSourceReaderFromURL` | `0x703A0` | 40 | UnwindData |  |
| 5 | `MFCreateSourceReaderFromByteStream` | `0x7E850` | 40 | UnwindData |  |
