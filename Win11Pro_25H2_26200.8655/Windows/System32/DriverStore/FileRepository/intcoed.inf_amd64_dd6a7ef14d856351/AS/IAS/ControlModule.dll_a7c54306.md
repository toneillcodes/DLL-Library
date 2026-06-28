# Binary Specification: ControlModule.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\intcoed.inf_amd64_dd6a7ef14d856351\AS\IAS\ControlModule.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a7c54306ef8339449d7c41e0246088090ddc88ff3a6c6a5fce0aa83f06f10af5`
* **Total Exported Functions:** 168

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `??4IIntelWovControl@@QEAAAEAV0@AEBV0@@Z` | `0x8EC0` | 5,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `ACADetectorBuildArmingData` | `0xA610` | 133 | UnwindData |  |
| 47 | `ACADetectorGetCaps` | `0xA6A0` | 109 | UnwindData |  |
| 48 | `ACADetectorVerifyDetection` | `0xA710` | 190 | UnwindData |  |
| 55 | `CreateAcaDetectorDllClientInstance` | `0xA7D0` | 116 | UnwindData |  |
| 69 | `DisposeAcaDetectorDllClient` | `0xA850` | 119 | UnwindData |  |
| 82 | `GetAcaDetectorApiVersion` | `0xA8D0` | 108 | UnwindData |  |
| 90 | `GetLibraryVersion` | `0xA940` | 135 | UnwindData |  |
| 86 | `GetEndpoints` | `0xA9E0` | 100 | UnwindData |  |
| 113 | `KsProperty` | `0xFAE0` | 693 | UnwindData |  |
| 63 | `CreateSpeakerModelCreatorConfigInstance` | `0x129B0` | 83 | UnwindData |  |
| 74 | `DisposeSpeakerModelCreatorConfigInstance` | `0x12A10` | 119 | UnwindData |  |
| 108 | `InternalDataProcessing` | `0x12A90` | 85 | UnwindData |  |
| 144 | `SidSetCohort` | `0x12AF0` | 95 | UnwindData |  |
| 152 | `SidSetUbm` | `0x12B50` | 95 | UnwindData |  |
| 51 | `AddUtteranceData` | `0x12D50` | 116 | UnwindData |  |
| 64 | `CreateSpeakerModelCreatorInstance` | `0x12DD0` | 171 | UnwindData |  |
| 75 | `DisposeSpeakerModelCreatorInstance` | `0x12E80` | 123 | UnwindData |  |
| 156 | `TrainModel` | `0x12F00` | 109 | UnwindData |  |
| 1 | `??0HpalIoctlControl@@QEAA@XZ` | `0x12F70` | 45 | UnwindData |  |
| 7 | `??1HpalIoctlControl@@UEAA@XZ` | `0x12FA0` | 42 | UnwindData |  |
| 18 | `?GetBigParameter@HpalIoctlControl@@UEAAKKKPEAXAEA_K@Z` | `0x132C0` | 534 | UnwindData |  |
| 20 | `?GetDevicePath@HpalIoctlControl@@UEAAPEB_WXZ` | `0x134E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?GetStructParameter@HpalIoctlControl@@UEAAKKKPEAXK@Z` | `0x134F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `?GetTinyParameter@HpalIoctlControl@@UEAAKKKPEAX@Z` | `0x134F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `?SetTinyParameter@HpalIoctlControl@@UEAAKKKK_N@Z` | `0x134F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `?SetBigParameter@HpalIoctlControl@@UEAAKKKPEAX_K@Z` | `0x13500` | 499 | UnwindData |  |
| 5 | `??0IntelLpalListener@@QEAA@XZ` | `0x13880` | 111 | UnwindData |  |
| 93 | `GetRegKeyValueExport` | `0x13BB0` | 291 | UnwindData |  |
| 95 | `GetServiceRegistryStateKeyExport` | `0x13CE0` | 397 | UnwindData |  |
| 129 | `ReadInterfaceRegistryKeyExport` | `0x13E70` | 208 | UnwindData |  |
| 130 | `RegCloseKeyExport` | `0x13F40` | 1,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `AdjustSecurityPrivileges` | `0x146A0` | 605 | UnwindData |  |
| 53 | `CallNtPowerInformationExport` | `0x14900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `CloseHandleExport` | `0x14910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `CreateProcessAsUserWExport` | `0x14920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `DuplicateHandleExport` | `0x14930` | 147 | UnwindData |  |
| 92 | `GetProcessWorkingSetSizeExExport` | `0x149D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `GetServiceDirectoryExport` | `0x149E0` | 408 | UnwindData |  |
| 109 | `IsApiSetImplementedExport` | `0x14B80` | 1,089 | UnwindData |  |
| 112 | `IsPowerManagmentApiSetImplementedExport` | `0x14FD0` | 209 | UnwindData |  |
| 131 | `RegisterPowerSettingNotificationExport` | `0x150B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `RegisterServiceCtrlHandlerExWExport` | `0x150C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `SetDllDirectoryWExport` | `0x150D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `SetProcessWorkingSetSizeExExport` | `0x150E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `UnregisterPowerSettingNotificationExport` | `0x150F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `WTSGetActiveConsoleSessionIdExport` | `0x15100` | 36,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `SetLogMessageDelegate` | `0x1E100` | 220 | UnwindData |  |
| 87 | `GetEx` | `0x1FA90` | 195 | UnwindData |  |
| 56 | `CreateFarfieldDllClientInstance` | `0x28A30` | 118 | UnwindData |  |
| 70 | `DisposeFarfieldClient` | `0x28AB0` | 120 | UnwindData |  |
| 134 | `Reset` | `0x28B30` | 85 | UnwindData |  |
| 161 | `UpdateDvConfiguration` | `0x28B90` | 103 | UnwindData |  |
| 162 | `UpdateMicGeoConfiguration` | `0x28C00` | 103 | UnwindData |  |
| 163 | `UpdatePpConfiguration` | `0x28C70` | 103 | UnwindData |  |
| 164 | `UpdateReferenceWovConfiguration` | `0x28CE0` | 103 | UnwindData |  |
| 165 | `UpdateWovConfiguration` | `0x28D50` | 103 | UnwindData |  |
| 166 | `Verify` | `0x28DC0` | 138 | UnwindData |  |
| 4 | `??0IntelIOCTLControl@@QEAA@XZ` | `0x30590` | 1,537 | UnwindData |  |
| 9 | `??1IntelIOCTLControl@@UEAA@XZ` | `0x30C70` | 68 | UnwindData |  |
| 19 | `?GetBigParameter@IntelIOCTLControl@@UEAAKKKPEAXAEA_K@Z` | `0x31080` | 428 | UnwindData |  |
| 26 | `?GetStructParameter@IntelIOCTLControl@@UEAAKKKPEAXK@Z` | `0x31320` | 260 | UnwindData |  |
| 28 | `?GetTinyParameter@IntelIOCTLControl@@UEAAKKKPEAX@Z` | `0x31430` | 336 | UnwindData |  |
| 37 | `?SetBigParameter@IntelIOCTLControl@@UEAAKKKPEAX_K@Z` | `0x31C50` | 410 | UnwindData |  |
| 39 | `?SetTinyParameter@IntelIOCTLControl@@UEAAKKKK_N@Z` | `0x31DF0` | 285 | UnwindData |  |
| 57 | `CreateHpalIOCTLControlInstance` | `0x322A0` | 83 | UnwindData |  |
| 58 | `CreateIOCTLControlInstance` | `0x32300` | 100 | UnwindData |  |
| 71 | `DisposeIOCTLControl` | `0x32370` | 119 | UnwindData |  |
| 84 | `GetBigParameter` | `0x323F0` | 134 | UnwindData |  |
| 85 | `GetDevicePath` | `0x32480` | 191 | UnwindData |  |
| 97 | `GetStructParameter` | `0x32540` | 128 | UnwindData |  |
| 98 | `GetTinyParameter` | `0x325C0` | 117 | UnwindData |  |
| 136 | `SetBigParameter` | `0x32640` | 130 | UnwindData |  |
| 142 | `SetTinyParameter` | `0x326D0` | 129 | UnwindData |  |
| 60 | `CreateLpalListenerInstance` | `0x3C680` | 92 | UnwindData |  |
| 72 | `DisposeLpalListener` | `0x3C6E0` | 119 | UnwindData |  |
| 114 | `LCfg` | `0x3C760` | 257 | UnwindData |  |
| 115 | `LCloseAllSessions` | `0x3C870` | 92 | UnwindData |  |
| 116 | `LCreateStream` | `0x3C8D0` | 150 | UnwindData |  |
| 117 | `LDestroyStream` | `0x3C970` | 106 | UnwindData |  |
| 118 | `LGetBufferMetadata` | `0x3C9E0` | 106 | UnwindData |  |
| 119 | `LGetDetectionData` | `0x3CA50` | 106 | UnwindData |  |
| 120 | `LOpenStream` | `0x3CAC0` | 106 | UnwindData |  |
| 121 | `LQueryNotif` | `0x3CB30` | 106 | UnwindData |  |
| 122 | `LQuerySpeechMode` | `0x3CBA0` | 106 | UnwindData |  |
| 123 | `LRead` | `0x3CC10` | 106 | UnwindData |  |
| 124 | `LReset` | `0x3CC80` | 106 | UnwindData |  |
| 125 | `LStart` | `0x3CCF0` | 106 | UnwindData |  |
| 126 | `LStop` | `0x3CD60` | 106 | UnwindData |  |
| 127 | `LWaitHandle` | `0x3CDD0` | 107 | UnwindData |  |
| 2 | `??0IIntelWovControl@@QEAA@AEBV0@@Z` | `0x3E240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0IIntelWovControl@@QEAA@XZ` | `0x3E240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0IntelWovControl@@QEAA@XZ` | `0x3E250` | 57 | UnwindData |  |
| 8 | `??1IIntelWovControl@@UEAA@XZ` | `0x3E290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??1IntelWovControl@@UEAA@XZ` | `0x3E2A0` | 54 | UnwindData |  |
| 14 | `?ActivateDevice@IntelWovControl@@UEAAJPEB_W@Z` | `0x3E430` | 45 | UnwindData |  |
| 15 | `?AddDevice@IntelWovControl@@UEAAXPEB_W@Z` | `0x3E460` | 45 | UnwindData |  |
| 16 | `?CreateKsStream@IntelWovControl@@UEAAXK@Z` | `0x3E490` | 68 | UnwindData |  |
| 17 | `?GetActiveEndpointId@IntelWovControl@@UEAA?AV?$basic_string@_WU?$char_traits@_W@std@@V?$allocator@_W@2@@std@@XZ` | `0x3E4E0` | 79 | UnwindData |  |
| 21 | `?GetFirstLpCapableArrayEndpointId@IntelWovControl@@UEAA?AV?$basic_string@_WU?$char_traits@_W@std@@V?$allocator@_W@2@@std@@_N@Z` | `0x3E530` | 97 | UnwindData |  |
| 22 | `?GetKsStatus@IntelWovControl@@UEAA_NPEB_WAEA_N1AEAK22AEAG3PEAPEAVEndpointDeviceProxy@@@Z` | `0x3E5A0` | 151 | UnwindData |  |
| 23 | `?GetMicArray@IntelWovControl@@UEAA_NPEAPEAUKSAUDIO_MIC_ARRAY_GEOMETRY@@@Z` | `0x3E640` | 47 | UnwindData |  |
| 24 | `?GetSpeechDeviceId@IntelWovControl@@UEAA?AV?$basic_string@_WU?$char_traits@_W@std@@V?$allocator@_W@2@@std@@XZ` | `0x3E670` | 76 | UnwindData |  |
| 29 | `?InitializeKsControl@IntelWovControl@@UEAA_NXZ` | `0x3E6C0` | 33 | UnwindData |  |
| 30 | `?IsCaptureDevice@IntelWovControl@@UEAA_NPEB_W@Z` | `0x3E6F0` | 45 | UnwindData |  |
| 31 | `?IsLpCapableDevice@IntelWovControl@@UEAA_NPEB_W@Z` | `0x3E720` | 45 | UnwindData |  |
| 32 | `?LoadKsPipeline@IntelWovControl@@UEAAXKKGGW4eIntcSpeechMode@@_NKAEA_N@Z` | `0x3E750` | 133 | UnwindData |  |
| 33 | `?RegisterKsEventHandle@IntelWovControl@@UEAAXXZ` | `0x3E7E0` | 33 | UnwindData |  |
| 34 | `?RemoveDevice@IntelWovControl@@UEAAJPEB_WAEAH@Z` | `0x3E810` | 60 | UnwindData |  |
| 35 | `?RunStream@IntelWovControl@@UEAAXXZ` | `0x3E850` | 33 | UnwindData |  |
| 40 | `?StartStream@IntelWovControl@@UEAAXXZ` | `0x3E880` | 33 | UnwindData |  |
| 41 | `?StopKsStream@IntelWovControl@@UEAAXXZ` | `0x3E8B0` | 33 | UnwindData |  |
| 42 | `?UnloadKsControl@IntelWovControl@@UEAAXXZ` | `0x3E8E0` | 33 | UnwindData |  |
| 43 | `?UnloadPpClient@IntelWovControl@@UEAAXXZ` | `0x3E910` | 33 | UnwindData |  |
| 44 | `?UnregisterKsEventHandle@IntelWovControl@@UEAAXXZ` | `0x3E940` | 36 | UnwindData |  |
| 45 | `?WovConfigWaitHandle@IntelWovControl@@UEAAPEAXXZ` | `0x3E970` | 33 | UnwindData |  |
| 49 | `ActivateDevice` | `0x3EB00` | 113 | UnwindData |  |
| 50 | `AddDevice` | `0x3EB80` | 111 | UnwindData |  |
| 59 | `CreateKsStream` | `0x3EBF0` | 106 | UnwindData |  |
| 68 | `CreateWoVControlInstance` | `0x3EC60` | 83 | UnwindData |  |
| 79 | `DisposeWoVControl` | `0x3ECC0` | 119 | UnwindData |  |
| 83 | `GetActiveEndpointId` | `0x3ED40` | 245 | UnwindData |  |
| 88 | `GetFirstLpCapableArrayEndpointId` | `0x3EE40` | 240 | UnwindData |  |
| 89 | `GetKsStatus` | `0x3EF30` | 1,542 | UnwindData |  |
| 91 | `GetMicArray` | `0x3F540` | 397 | UnwindData |  |
| 96 | `GetSpeechDeviceId` | `0x3F6D0` | 242 | UnwindData |  |
| 99 | `InitializeKsControl` | `0x3F7D0` | 93 | UnwindData |  |
| 110 | `IsCaptureDevice` | `0x3F830` | 112 | UnwindData |  |
| 111 | `IsLpCapableDevice` | `0x3F8A0` | 112 | UnwindData |  |
| 128 | `LoadKsPipeline` | `0x3F910` | 182 | UnwindData |  |
| 133 | `RemoveDevice` | `0x3F9D0` | 113 | UnwindData |  |
| 135 | `RunStream` | `0x3FA50` | 92 | UnwindData |  |
| 153 | `StartStream` | `0x3FAB0` | 92 | UnwindData |  |
| 155 | `StopKsStream` | `0x3FB10` | 92 | UnwindData |  |
| 157 | `UnloadKsControl` | `0x3FB70` | 92 | UnwindData |  |
| 158 | `UnloadPpClient` | `0x3FBD0` | 92 | UnwindData |  |
| 159 | `UnregisterKsEventHandle` | `0x3FC30` | 92 | UnwindData |  |
| 168 | `WovConfigWaitHandle` | `0x3FC90` | 93 | UnwindData |  |
| 61 | `CreatePpDllClientInstance` | `0x40FF0` | 118 | UnwindData |  |
| 73 | `DisposePpDllClient` | `0x41070` | 119 | UnwindData |  |
| 100 | `IntelSstPreProcBurstProcess` | `0x410F0` | 119 | UnwindData |  |
| 101 | `IntelSstPreProcGetLatency` | `0x41170` | 109 | UnwindData |  |
| 102 | `IntelSstPreProcGetSize` | `0x411E0` | 109 | UnwindData |  |
| 103 | `IntelSstPreProcInitialize` | `0x41250` | 119 | UnwindData |  |
| 104 | `IntelSstPreProcProcess` | `0x412D0` | 119 | UnwindData |  |
| 105 | `IntelSstPreProcRelease` | `0x41350` | 109 | UnwindData |  |
| 106 | `IntelSstPreProcReset` | `0x413C0` | 109 | UnwindData |  |
| 107 | `IntelSstPreProcSetConfig` | `0x41430` | 119 | UnwindData |  |
| 65 | `CreateUtteranceCollectorConfigInstance` | `0x41730` | 83 | UnwindData |  |
| 76 | `DisposeUtteranceCollectorConfigInstance` | `0x41790` | 119 | UnwindData |  |
| 143 | `SidSetAcousticModel` | `0x41810` | 95 | UnwindData |  |
| 145 | `SidSetEndpointCompensationFrames` | `0x41870` | 90 | UnwindData |  |
| 146 | `SidSetKeyPhraseModel` | `0x418D0` | 95 | UnwindData |  |
| 147 | `SidSetKeyPhraseThreshold` | `0x41930` | 93 | UnwindData |  |
| 148 | `SidSetLogComponentMask` | `0x41990` | 92 | UnwindData |  |
| 149 | `SidSetLogLevel` | `0x419F0` | 92 | UnwindData |  |
| 150 | `SidSetStartpointCompensationFrames` | `0x41A50` | 90 | UnwindData |  |
| 151 | `SidSetTimeoutInFrames` | `0x41AB0` | 92 | UnwindData |  |
| 66 | `CreateUtteranceCollectorEventHandlerInstance` | `0x41D80` | 96 | UnwindData |  |
| 77 | `DisposeUtteranceCollectorEventHandlerInstance` | `0x41DE0` | 119 | UnwindData |  |
| 139 | `SetOnKeyPhraseDetectedDelegate` | `0x41E60` | 100 | UnwindData |  |
| 140 | `SetOnKeyPhraseTimeoutDelegate` | `0x41ED0` | 100 | UnwindData |  |
| 67 | `CreateUtteranceCollectorInstance` | `0x420A0` | 194 | UnwindData |  |
| 78 | `DisposeUtteranceCollectorInstance` | `0x42170` | 123 | UnwindData |  |
| 81 | `Feed` | `0x421F0` | 109 | UnwindData |  |
| 154 | `StartUtteranceEnrollment` | `0x42260` | 92 | UnwindData |  |
| 12 | `??_7IIntelWovControl@@6B@` | `0xA9048` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??_7IntelWovControl@@6B@` | `0xA90F8` | 0 | Indeterminate |  |
