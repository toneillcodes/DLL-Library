# Binary Specification: mftranscode.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mftranscode.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `760b748b067cb76678ae28e007363124efcf7a04d85fba1efa3929dc471fbcbc`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MFCreateTranscodeTopologyFromByteStream` | `0x17C0` | 15 | UnwindData |  |
| 8 | `MFTranscodeGetAudioOutputAvailableTypes` | `0x5490` | 2,011 | UnwindData |  |
| 1 | `GetTranscodeComponentCreator` | `0x10450` | 402 | UnwindData |  |
| 4 | `MFCreateTranscodeProfile` | `0x105F0` | 494 | UnwindData |  |
| 2 | `MFCreateSmartRemuxEngine` | `0x20F60` | 43,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MFCreateTranscodeEngine` | `0x2BA40` | 25,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MFCreateTranscodeSinkActivate` | `0x31F00` | 6,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MFCreateTranscodeTopology` | `0x33950` | 2,361 | UnwindData |  |
