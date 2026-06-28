# Binary Specification: spkvol.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\lenovofnandfunctionkeys.inf_amd64_fa50a878363b0cec\spkvol.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3f831d984f8292e8eff1a5750ef540486a8dbf370e521f761176938244bcaacc`
* **Total Exported Functions:** 43

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `??0CMMNotificationClient@@QEAA@XZ` | `0x3E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??1CMMNotificationClient@@QEAA@XZ` | `0x3E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `?AddRef@CAudioEndpointVolumeCallback@@UEAAKXZ` | `0x3E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `?AddRef@CMMNotificationClient@@UEAAKXZ` | `0x3E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `?Release@CMMNotificationClient@@UEAAKXZ` | `0x3E50` | 54 | UnwindData |  |
| 28 | `?QueryInterface@CMMNotificationClient@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x3E90` | 111 | UnwindData |  |
| 3 | `??0CMMNotificationClient@@QEAA@AEBV0@@Z` | `0x3F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??4CMMNotificationClient@@QEAAAEAV0@AEBV0@@Z` | `0x3F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0CAudioEndpointVolumeCallback@@QEAA@PEAX@Z` | `0x3F30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??1CAudioEndpointVolumeCallback@@QEAA@XZ` | `0x3F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `?Release@CAudioEndpointVolumeCallback@@UEAAKXZ` | `0x3F70` | 54 | UnwindData |  |
| 27 | `?QueryInterface@CAudioEndpointVolumeCallback@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x3FB0` | 111 | UnwindData |  |
| 1 | `??0CAudioEndpointVolumeCallback@@QEAA@AEBV0@@Z` | `0x4020` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??4CAudioEndpointVolumeCallback@@QEAAAEAV0@AEBV0@@Z` | `0x4050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `?__autoclassinit2@CAudioEndpointVolumeCallback@@QEAAX_K@Z` | `0x4080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `?__autoclassinit2@CSpkVol@@QEAAX_K@Z` | `0x4080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??4CSpkVol@@QEAAAEAV0@AEBV0@@Z` | `0x4090` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `?OnDefaultDeviceChanged@CMMNotificationClient@@UEAAJW4__MIDL___MIDL_itf_mmdeviceapi_0000_0000_0001@@W4__MIDL___MIDL_itf_mmdeviceapi_0000_0000_0002@@PEB_W@Z` | `0x4490` | 73 | UnwindData |  |
| 22 | `?OnDeviceAdded@CMMNotificationClient@@UEAAJPEB_W@Z` | `0x44E0` | 47 | UnwindData |  |
| 23 | `?OnDeviceRemoved@CMMNotificationClient@@UEAAJPEB_W@Z` | `0x4510` | 47 | UnwindData |  |
| 14 | `?AddDevice@CSpkVol@@QEAAJPEB_W@Z` | `0x4540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `?OnDeviceStateChanged@CMMNotificationClient@@UEAAJPEB_WK@Z` | `0x4540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?OnPropertyValueChanged@CMMNotificationClient@@UEAAJPEB_WU_tagpropertykey@@@Z` | `0x4540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `?RemoveDevice@CSpkVol@@QEAAJPEB_W@Z` | `0x4540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?OnNotify@CAudioEndpointVolumeCallback@@UEAAJPEAUAUDIO_VOLUME_NOTIFICATION_DATA@@@Z` | `0x4550` | 111 | UnwindData |  |
| 33 | `?ResetLocalData@CAudioEndpointVolumeCallback@@QEAAHPEAUIAudioEndpointVolume@@@Z` | `0x45C0` | 111 | UnwindData |  |
| 21 | `?OnDefaultDeviceChanged@CSpkVol@@QEAAHPEB_W@Z` | `0x4630` | 530 | UnwindData |  |
| 18 | `?GetMute@CSpkVol@@QEAAJPEAH@Z` | `0x4850` | 365 | UnwindData |  |
| 35 | `?SetMute@CSpkVol@@QEAAJH@Z` | `0x49C0` | 318 | UnwindData |  |
| 17 | `?GetLevel@CSpkVol@@QEAAJPEAM@Z` | `0x4B00` | 231 | UnwindData |  |
| 34 | `?SetLevel@CSpkVol@@QEAAJM@Z` | `0x4BF0` | 170 | UnwindData |  |
| 19 | `?Initialize@CSpkVol@@QEAAHXZ` | `0x4CD0` | 454 | UnwindData |  |
| 31 | `?Release@CSpkVol@@QEAAHXZ` | `0x4EA0` | 229 | UnwindData |  |
| 5 | `??0CSpkVol@@QEAA@PEAX@Z` | `0x4F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??1CSpkVol@@QEAA@XZ` | `0x4FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `OpenSpeakerVolumeInterface` | `0x4FD0` | 39 | UnwindData |  |
| 38 | `CloseSpeakerVolumeInterface` | `0x50B0` | 32 | UnwindData |  |
| 39 | `GetMuteState` | `0x5120` | 73 | UnwindData |  |
| 42 | `SetMuteState` | `0x52E0` | 40 | UnwindData |  |
| 40 | `GetVolumeLevel` | `0x5310` | 127 | UnwindData |  |
| 43 | `SetVolumeLevel` | `0x5390` | 56 | UnwindData |  |
| 12 | `??_7CAudioEndpointVolumeCallback@@6B@` | `0x7DD8` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??_7CMMNotificationClient@@6B@` | `0x7E10` | 0 | Indeterminate |  |
