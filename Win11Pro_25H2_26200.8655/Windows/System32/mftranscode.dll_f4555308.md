# Binary Specification: mftranscode.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mftranscode.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f4555308bc3073aedb0f27cdb32122d872a3ec61645d130be09f048d2420fb3e`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MFCreateTranscodeTopologyFromByteStream` | `0x1790` | 15 | UnwindData |  |
| 8 | `MFTranscodeGetAudioOutputAvailableTypes` | `0x5460` | 2,011 | UnwindData |  |
| 1 | `GetTranscodeComponentCreator` | `0x10420` | 402 | UnwindData |  |
| 4 | `MFCreateTranscodeProfile` | `0x105C0` | 494 | UnwindData |  |
| 2 | `MFCreateSmartRemuxEngine` | `0x20EC0` | 43,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MFCreateTranscodeEngine` | `0x2B990` | 25,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MFCreateTranscodeSinkActivate` | `0x31E50` | 6,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MFCreateTranscodeTopology` | `0x338A0` | 2,361 | UnwindData |  |
