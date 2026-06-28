# Binary Specification: spkvol.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\lenovofnandfunctionkeys.inf_amd64_5e21bf389d23855a\spkvol.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `547a18ebbdd4033d649be4c525bc1f1dff6b1b116588a1cb9e2d51f171820bfe`
* **Total Exported Functions:** 43

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `??0CMMNotificationClient@@QEAA@XZ` | `0x3EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??1CMMNotificationClient@@QEAA@XZ` | `0x3F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `?AddRef@CAudioEndpointVolumeCallback@@UEAAKXZ` | `0x3F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `?AddRef@CMMNotificationClient@@UEAAKXZ` | `0x3F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `?Release@CMMNotificationClient@@UEAAKXZ` | `0x3F30` | 54 | UnwindData |  |
| 28 | `?QueryInterface@CMMNotificationClient@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x3F70` | 118 | UnwindData |  |
| 3 | `??0CMMNotificationClient@@QEAA@AEBV0@@Z` | `0x3FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??4CMMNotificationClient@@QEAAAEAV0@AEBV0@@Z` | `0x4010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0CAudioEndpointVolumeCallback@@QEAA@PEAX@Z` | `0x4020` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??1CAudioEndpointVolumeCallback@@QEAA@XZ` | `0x4050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `?Release@CAudioEndpointVolumeCallback@@UEAAKXZ` | `0x4060` | 54 | UnwindData |  |
| 27 | `?QueryInterface@CAudioEndpointVolumeCallback@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x40A0` | 118 | UnwindData |  |
| 1 | `??0CAudioEndpointVolumeCallback@@QEAA@AEBV0@@Z` | `0x4120` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??4CAudioEndpointVolumeCallback@@QEAAAEAV0@AEBV0@@Z` | `0x4150` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `?__autoclassinit2@CAudioEndpointVolumeCallback@@QEAAX_K@Z` | `0x4180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `?__autoclassinit2@CSpkVol@@QEAAX_K@Z` | `0x4180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??4CSpkVol@@QEAAAEAV0@AEBV0@@Z` | `0x4190` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `?OnDefaultDeviceChanged@CMMNotificationClient@@UEAAJW4__MIDL___MIDL_itf_mmdeviceapi_0000_0000_0001@@W4__MIDL___MIDL_itf_mmdeviceapi_0000_0000_0002@@PEB_W@Z` | `0x45C0` | 73 | UnwindData |  |
| 22 | `?OnDeviceAdded@CMMNotificationClient@@UEAAJPEB_W@Z` | `0x4610` | 47 | UnwindData |  |
| 23 | `?OnDeviceRemoved@CMMNotificationClient@@UEAAJPEB_W@Z` | `0x4640` | 47 | UnwindData |  |
| 14 | `?AddDevice@CSpkVol@@QEAAJPEB_W@Z` | `0x4670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `?OnDeviceStateChanged@CMMNotificationClient@@UEAAJPEB_WK@Z` | `0x4670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?OnPropertyValueChanged@CMMNotificationClient@@UEAAJPEB_WU_tagpropertykey@@@Z` | `0x4670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `?RemoveDevice@CSpkVol@@QEAAJPEB_W@Z` | `0x4670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?OnNotify@CAudioEndpointVolumeCallback@@UEAAJPEAUAUDIO_VOLUME_NOTIFICATION_DATA@@@Z` | `0x4680` | 111 | UnwindData |  |
| 33 | `?ResetLocalData@CAudioEndpointVolumeCallback@@QEAAHPEAUIAudioEndpointVolume@@@Z` | `0x46F0` | 132 | UnwindData |  |
| 21 | `?OnDefaultDeviceChanged@CSpkVol@@QEAAHPEB_W@Z` | `0x4780` | 591 | UnwindData |  |
| 18 | `?GetMute@CSpkVol@@QEAAJPEAH@Z` | `0x49D0` | 386 | UnwindData |  |
| 35 | `?SetMute@CSpkVol@@QEAAJH@Z` | `0x4B60` | 349 | UnwindData |  |
| 17 | `?GetLevel@CSpkVol@@QEAAJPEAM@Z` | `0x4CC0` | 252 | UnwindData |  |
| 34 | `?SetLevel@CSpkVol@@QEAAJM@Z` | `0x4DC0` | 177 | UnwindData |  |
| 19 | `?Initialize@CSpkVol@@QEAAHXZ` | `0x4EC0` | 503 | UnwindData |  |
| 31 | `?Release@CSpkVol@@QEAAHXZ` | `0x50C0` | 289 | UnwindData |  |
| 5 | `??0CSpkVol@@QEAA@PEAX@Z` | `0x51F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??1CSpkVol@@QEAA@XZ` | `0x5210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `OpenSpeakerVolumeInterface` | `0x5230` | 39 | UnwindData |  |
| 38 | `CloseSpeakerVolumeInterface` | `0x5310` | 32 | UnwindData |  |
| 39 | `GetMuteState` | `0x5380` | 73 | UnwindData |  |
| 42 | `SetMuteState` | `0x5550` | 40 | UnwindData |  |
| 40 | `GetVolumeLevel` | `0x5580` | 135 | UnwindData |  |
| 43 | `SetVolumeLevel` | `0x5610` | 56 | UnwindData |  |
| 12 | `??_7CAudioEndpointVolumeCallback@@6B@` | `0x8EF8` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??_7CMMNotificationClient@@6B@` | `0x8F30` | 0 | Indeterminate |  |
