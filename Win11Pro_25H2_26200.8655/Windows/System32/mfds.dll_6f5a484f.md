# Binary Specification: mfds.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mfds.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6f5a484f1971aae128fa20cf7f024ef11d9768ff9614ac262a054f30e0b31237`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 15 | `InitMpeg1VideoStream_` | `0x178A0` | 373 | UnwindData |  |
| 20 | `PESHeaderLength` | `0x364C0` | 2,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `PESPacketLength` | `0x36CA0` | 53,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x43CC0` | 64 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x489D0` | 4,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `PESPacketPTSinPCR` | `0x49A10` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `PackSCR` | `0x4A0A0` | 4,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `xMediaSubTypeTransform` | `0x4B1C0` | 35,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `InitAC3AudioStream_` | `0x53AB0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `InitDTSAudioStream_` | `0x53B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `InitAC4AudioStream_` | `0x53BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `InitDDPlusAudioStream_` | `0x53BB0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `PackMuxRate` | `0x53DC0` | 8,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `InitAACAudioStream_` | `0x55EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `InitBDAVLPCMAudioStream_` | `0x55EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `InitH264Stream_` | `0x55EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `InitHEVCStream_` | `0x55ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `InitLPCMAudioStream_` | `0x55EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `InitLPCMMiracastAudioStream_` | `0x55EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `InitMpeg2VideoStream_` | `0x55F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `InitMpegAudioStream_` | `0x55F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `InitMpegHAudioStream_` | `0x55F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `InitTrueHDAudioStream_` | `0x55F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `xCreateCannedMediaType` | `0x55F40` | 34,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x5E5C0` | 104 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x5E630` | 26 | UnwindData |  |
