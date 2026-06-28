# Binary Specification: RpcServer.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\intcoed.inf_amd64_dd6a7ef14d856351\AS\IAS\RpcServer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `defa9208cb58e382479848583515e9447983811a67d934288c8aa24f541eb326`
* **Total Exported Functions:** 45

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `SetAcaProxyAcaDetectorGetCapsDelegate` | `0x1840` | 24 | UnwindData |  |
| 5 | `SetAcaProxyAcaRegisterNotificationHandleDelegate` | `0x1860` | 24 | UnwindData |  |
| 9 | `SetAcaProxyAcaUnregisterNotificationHandleDelegate` | `0x1880` | 24 | UnwindData |  |
| 7 | `SetAcaProxyAcaStartSoundDetectDelegate` | `0x18A0` | 24 | UnwindData |  |
| 8 | `SetAcaProxyAcaStopSoundDetectDelegate` | `0x18C0` | 24 | UnwindData |  |
| 6 | `SetAcaProxyAcaSetIpParamDelegate` | `0x18E0` | 24 | UnwindData |  |
| 4 | `SetAcaProxyAcaGetIpParamDelegate` | `0x1900` | 24 | UnwindData |  |
| 2 | `SetAcaProxyAcaContextQueryDelegate` | `0x1920` | 24 | UnwindData |  |
| 10 | `SetAcaProxyGetAcaApiVersionDelegate` | `0x1940` | 24 | UnwindData |  |
| 1 | `InitRpcLauncherDll` | `0x1C60` | 396 | UnwindData |  |
| 44 | `StartRpcServerDll` | `0x1DF0` | 66 | UnwindData |  |
| 45 | `StopRpcServerDll` | `0x1F90` | 121 | UnwindData |  |
| 21 | `SetIntelClientProxyCpQueryDelegate` | `0x3710` | 24 | UnwindData |  |
| 20 | `SetIntelClientProxyCpMicArrayQueryDelegate` | `0x3730` | 24 | UnwindData |  |
| 13 | `SetIntelClientProxyCpCreateStreamV1Delegate` | `0x3750` | 24 | UnwindData |  |
| 14 | `SetIntelClientProxyCpCreateStreamV2Delegate` | `0x3770` | 24 | UnwindData |  |
| 15 | `SetIntelClientProxyCpCreateStreamV3Delegate` | `0x3790` | 24 | UnwindData |  |
| 16 | `SetIntelClientProxyCpDestroyStreamDelegate` | `0x37B0` | 24 | UnwindData |  |
| 22 | `SetIntelClientProxyCpStartDelegate` | `0x37D0` | 24 | UnwindData |  |
| 23 | `SetIntelClientProxyCpStopDelegate` | `0x37F0` | 24 | UnwindData |  |
| 19 | `SetIntelClientProxyCpGetBufferDelegate` | `0x3810` | 24 | UnwindData |  |
| 17 | `SetIntelClientProxyCpEventQueryDelegate` | `0x3830` | 24 | UnwindData |  |
| 18 | `SetIntelClientProxyCpFarfieldSupportQueryDelegate` | `0x3850` | 24 | UnwindData |  |
| 12 | `SetIntelClientProxyCpAudioFormatQueryDelegate` | `0x3870` | 24 | UnwindData |  |
| 11 | `SetIntelClientProxyCpApiVersionQueryDelegate` | `0x3890` | 24 | UnwindData |  |
| 26 | `SetIntelMultiPaSetupProxyAssistantSubscribeDelegate` | `0x38B0` | 24 | UnwindData |  |
| 27 | `SetIntelMultiPaSetupProxyAssistantUnsubscribeDelegate` | `0x38D0` | 24 | UnwindData |  |
| 35 | `SetIntelMultiPaSetupProxyRegisterPdtDelegate` | `0x38F0` | 27 | UnwindData |  |
| 36 | `SetIntelMultiPaSetupProxyRegisterUdtDelegate` | `0x3910` | 27 | UnwindData |  |
| 25 | `SetIntelMultiPaSetupProxyAddSvDelegate` | `0x3930` | 27 | UnwindData |  |
| 42 | `SetIntelMultiPaSetupProxyUnregisterPdtDelegate` | `0x3950` | 27 | UnwindData |  |
| 43 | `SetIntelMultiPaSetupProxyUnregisterUdtDelegate` | `0x3970` | 27 | UnwindData |  |
| 39 | `SetIntelMultiPaSetupProxyRemoveSvDelegate` | `0x3990` | 27 | UnwindData |  |
| 32 | `SetIntelMultiPaSetupProxyQueryCapabilitiesDelegate` | `0x39B0` | 27 | UnwindData |  |
| 33 | `SetIntelMultiPaSetupProxyQueryCurrentLanguageDelegate` | `0x39D0` | 27 | UnwindData |  |
| 30 | `SetIntelMultiPaSetupProxyGetMultiPaApiVersionDelegate` | `0x39F0` | 27 | UnwindData |  |
| 40 | `SetIntelMultiPaSetupProxySetMultiPaParameterDelegate` | `0x3A10` | 27 | UnwindData |  |
| 31 | `SetIntelMultiPaSetupProxyGetMultiPaParameterDelegate` | `0x3A30` | 27 | UnwindData |  |
| 24 | `SetIntelMultiPaSetupProxyAddSidDelegate` | `0x3A50` | 27 | UnwindData |  |
| 38 | `SetIntelMultiPaSetupProxyRemoveSidDelegate` | `0x3A70` | 27 | UnwindData |  |
| 41 | `SetIntelMultiPaSetupProxyStartEnrollmentDelegate` | `0x3A90` | 27 | UnwindData |  |
| 29 | `SetIntelMultiPaSetupProxyFeedEnrollmentDataDelegate` | `0x3AB0` | 27 | UnwindData |  |
| 28 | `SetIntelMultiPaSetupProxyCompleteEnrollmentDelegate` | `0x3AD0` | 27 | UnwindData |  |
| 37 | `SetIntelMultiPaSetupProxyRemoveEnrollmentDelegate` | `0x3AF0` | 27 | UnwindData |  |
| 34 | `SetIntelMultiPaSetupProxyQueryEnrollmentConfigurationDelegate` | `0x3B10` | 27 | UnwindData |  |
