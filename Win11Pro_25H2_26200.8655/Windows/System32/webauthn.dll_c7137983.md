# Binary Specification: webauthn.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\webauthn.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c7137983a19c4f8d9659dc620aea12eeaf613bb83c23c2ba1dec658e834dccac`
* **Total Exported Functions:** 153

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1005 | `CryptsvcDllCtrl` | `0x94A0` | 158 | UnwindData |  |
| 1093 | `WebAuthNCtapStopDeviceChangeNotify` | `0x11BC0` | 10,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `I_WebAuthNCtapEncodeMakeCredentialRpcRequest` | `0x14640` | 1,393 | UnwindData |  |
| 1056 | `WebAuthNAuthenticatorGetAssertion` | `0x159B0` | 2,024 | UnwindData |  |
| 1106 | `WebAuthNGetApiVersionNumber` | `0x161A0` | 609 | UnwindData |  |
| 1116 | `WebAuthNIsUserVerifyingPlatformAuthenticatorAvailable` | `0x16CA0` | 49 | UnwindData |  |
| 1143 | `WebAuthNWriteEventCleanedupLocalStore` | `0x299A0` | 91 | UnwindData |  |
| 1144 | `WebAuthNWriteEventCloudStoreOperationFailure` | `0x29A10` | 71 | UnwindData |  |
| 1145 | `WebAuthNWriteEventCloudStoreOperationSuccess` | `0x29A60` | 63 | UnwindData |  |
| 1146 | `WebAuthNWriteEventCreatedUserStorage` | `0x29AB0` | 46 | UnwindData |  |
| 1147 | `WebAuthNWriteEventDeletedTrustGroup` | `0x29AF0` | 91 | UnwindData |  |
| 1148 | `WebAuthNWriteEventKeyRotationFailure` | `0x29B60` | 50 | UnwindData |  |
| 1149 | `WebAuthNWriteEventKeyRotationSuccess` | `0x29BA0` | 50 | UnwindData |  |
| 1150 | `WebAuthNWriteEventLocalStoreOperationFailure` | `0x29BE0` | 71 | UnwindData |  |
| 1151 | `WebAuthNWriteEventLocalStoreOperationSuccess` | `0x29C30` | 63 | UnwindData |  |
| 1152 | `WebAuthNWriteEventSyncState` | `0x29C80` | 50 | UnwindData |  |
| 1153 | `WebAuthNWriteEventSyncTrustedGroupDeletion` | `0x29CC0` | 91 | UnwindData |  |
| 1007 | `I_WebAuthNCtapDecodeGetAssertionRpcResponse` | `0x33470` | 5,302 | UnwindData |  |
| 1009 | `I_WebAuthNCtapDecodeMakeCredentialRpcResponse` | `0x34930` | 6,093 | UnwindData |  |
| 1011 | `I_WebAuthNCtapEncodeGetAssertionRpcRequest` | `0x36110` | 1,163 | UnwindData |  |
| 1074 | `WebAuthNCtapManageFreeDisplayCredentials` | `0x37F40` | 71 | UnwindData |  |
| 1059 | `WebAuthNCtapChangeClientPin` | `0x42C20` | 435 | UnwindData |  |
| 1060 | `WebAuthNCtapChangeClientPinForSelectedDevice` | `0x42DE0` | 684 | UnwindData |  |
| 1061 | `WebAuthNCtapFreeSelectedDeviceInformation` | `0x430A0` | 20 | UnwindData |  |
| 1105 | `WebAuthNFreeUserEntityList` | `0x430A0` | 20 | UnwindData |  |
| 1036 | `WebAuthNPluginFreeUserVerificationResponse` | `0x430A0` | 20 | UnwindData |  |
| 1062 | `WebAuthNCtapGetAssertion` | `0x430C0` | 1,951 | UnwindData |  |
| 1063 | `WebAuthNCtapGetSupportedTransports` | `0x43870` | 663 | UnwindData |  |
| 1064 | `WebAuthNCtapGetWnfLocalizedString` | `0x43B10` | 418 | UnwindData |  |
| 1065 | `WebAuthNCtapIsStopSendCommandError` | `0x43CC0` | 176 | UnwindData |  |
| 1066 | `WebAuthNCtapMakeCredential` | `0x43D80` | 1,576 | UnwindData |  |
| 1067 | `WebAuthNCtapManageAuthenticatePin` | `0x443B0` | 365 | UnwindData |  |
| 1068 | `WebAuthNCtapManageCancelEnrollFingerprint` | `0x44530` | 207 | UnwindData |  |
| 1069 | `WebAuthNCtapManageChangePin` | `0x44610` | 493 | UnwindData |  |
| 1070 | `WebAuthNCtapManageClose` | `0x44810` | 151 | UnwindData |  |
| 1071 | `WebAuthNCtapManageDeleteCredential` | `0x448B0` | 235 | UnwindData |  |
| 1072 | `WebAuthNCtapManageEnableEnterpriseAttestation` | `0x449B0` | 124 | UnwindData |  |
| 1073 | `WebAuthNCtapManageEnrollFingerprint` | `0x44A40` | 596 | UnwindData |  |
| 1075 | `WebAuthNCtapManageGetDisplayCredentials` | `0x44CA0` | 1,480 | UnwindData |  |
| 1076 | `WebAuthNCtapManageGetLargeBlobs` | `0x45270` | 317 | UnwindData |  |
| 1077 | `WebAuthNCtapManageRemoveFingerprints` | `0x453C0` | 329 | UnwindData |  |
| 1078 | `WebAuthNCtapManageResetDevice` | `0x45510` | 575 | UnwindData |  |
| 1079 | `WebAuthNCtapManageSelect` | `0x45760` | 283 | UnwindData |  |
| 1080 | `WebAuthNCtapManageSetAlwaysUv` | `0x45890` | 140 | UnwindData |  |
| 1081 | `WebAuthNCtapManageSetLargeBlobs` | `0x45930` | 172 | UnwindData |  |
| 1082 | `WebAuthNCtapManageSetMinPinLength` | `0x459F0` | 181 | UnwindData |  |
| 1083 | `WebAuthNCtapManageSetPin` | `0x45AB0` | 360 | UnwindData |  |
| 1084 | `WebAuthNCtapParseAuthenticatorData` | `0x45C20` | 184 | UnwindData |  |
| 1085 | `WebAuthNCtapResetDevice` | `0x45CE0` | 147 | UnwindData |  |
| 1086 | `WebAuthNCtapRpcGetAssertionUserList` | `0x45D80` | 844 | UnwindData |  |
| 1087 | `WebAuthNCtapRpcGetCborCommand` | `0x460E0` | 286 | UnwindData |  |
| 1088 | `WebAuthNCtapRpcRenderQrCode` | `0x46210` | 475 | UnwindData |  |
| 1089 | `WebAuthNCtapRpcSelectGetAssertion` | `0x46400` | 584 | UnwindData |  |
| 1090 | `WebAuthNCtapSendCommand` | `0x46650` | 1,890 | UnwindData |  |
| 1091 | `WebAuthNCtapSetClientPin` | `0x46DC0` | 344 | UnwindData |  |
| 1092 | `WebAuthNCtapStartDeviceChangeNotify` | `0x46F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1094 | `WebAuthNCtapVerifyGetAssertion` | `0x46F30` | 567 | UnwindData |  |
| 1101 | `WebAuthNFreeCredentialAttestation` | `0x47170` | 96 | UnwindData |  |
| 1110 | `WebAuthNGetCredentialIdFromAuthenticatorData` | `0x471E0` | 187 | UnwindData |  |
| 1111 | `WebAuthNGetErrorName` | `0x472B0` | 40 | UnwindData |  |
| 1115 | `WebAuthNGetW3CExceptionDOMError` | `0x472E0` | 34 | UnwindData |  |
| 1014 | `EXPERIMENTAL_WebAuthNIsUserVerifyingNativePlatformAuthenticatorAvailable` | `0x4BC60` | 63 | UnwindData |  |
| 1057 | `WebAuthNAuthenticatorMakeCredential` | `0x4BD60` | 2,731 | UnwindData |  |
| 1058 | `WebAuthNCancelCurrentOperation` | `0x4C820` | 17 | UnwindData |  |
| 1099 | `WebAuthNFreeAssertion` | `0x4C840` | 94 | UnwindData |  |
| 1100 | `WebAuthNFreeAuthenticatorList` | `0x4C8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1102 | `WebAuthNFreeDecodedAccountInformation` | `0x4C8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1048 | `WebAuthNFreeDecodedGetAssertionRequest` | `0x4C8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1051 | `WebAuthNFreeDecodedMakeCredentialRequest` | `0x4C8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1103 | `WebAuthNFreeEncodedAccountInformation` | `0x4C8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `WebAuthNFreePlatformCredentialList` | `0x4C8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1045 | `WebAuthNPluginFreeAddAuthenticatorResponse` | `0x4C8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1127 | `WebAuthNSyncFreeSyncStatus` | `0x4C8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1107 | `WebAuthNGetAuthenticatorList` | `0x4C8C0` | 121 | UnwindData |  |
| 1108 | `WebAuthNGetCancellationId` | `0x4C940` | 86 | UnwindData |  |
| 1109 | `WebAuthNGetCoseAlgorithmIdentifier` | `0x4C9A0` | 75 | UnwindData |  |
| 1095 | `WebAuthNDecodeAccountInformation` | `0x62A80` | 142 | UnwindData |  |
| 1096 | `WebAuthNDeletePlatformCredential` | `0x62B20` | 434 | UnwindData |  |
| 1097 | `WebAuthNDeletePlatformCredentialServer` | `0x62CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1098 | `WebAuthNEncodeAccountInformation` | `0x62CF0` | 147 | UnwindData |  |
| 1112 | `WebAuthNGetPlatformCredentialList` | `0x62D90` | 1,079 | UnwindData |  |
| 1113 | `WebAuthNGetPlatformCredentialListServer` | `0x631D0` | 4,843 | UnwindData |  |
| 1114 | `WebAuthNGetPlatformCredentialListSettings` | `0x644D0` | 141 | UnwindData |  |
| 1132 | `WebAuthNSyncIsFirstPartyProviderSupported` | `0x64570` | 61 | UnwindData |  |
| 1135 | `WebAuthNSyncIsThirdPartyProviderSupported` | `0x645C0` | 64 | UnwindData |  |
| 1136 | `WebAuthNSyncOTSApi` | `0x65CC0` | 1,049 | UnwindData |  |
| 1140 | `WebAuthNSyncRunSettingsOTS` | `0x660E0` | 21 | UnwindData |  |
| 1125 | `WebAuthNSyncAddTrustedDevice` | `0x6AF90` | 138 | UnwindData |  |
| 1126 | `WebAuthNSyncCheckEnableSaveLocalDevice` | `0x6B020` | 201 | UnwindData |  |
| 1128 | `WebAuthNSyncFreeTrustedDeviceList` | `0x6B0F0` | 80 | UnwindData |  |
| 1129 | `WebAuthNSyncGetSyncStatus` | `0x6B150` | 619 | UnwindData |  |
| 1130 | `WebAuthNSyncGetTrustedDeviceList` | `0x6B3D0` | 1,468 | UnwindData |  |
| 1131 | `WebAuthNSyncInvalidateCredentialCache` | `0x6B9A0` | 43 | UnwindData |  |
| 1133 | `WebAuthNSyncIsSaveLocalDeviceEnabled` | `0x6B9E0` | 304 | UnwindData |  |
| 1134 | `WebAuthNSyncIsSyncEnabled` | `0x6BB20` | 188 | UnwindData |  |
| 1137 | `WebAuthNSyncRemoveTrustedDevice` | `0x6BBF0` | 130 | UnwindData |  |
| 1138 | `WebAuthNSyncRenameTrustedDevice` | `0x6BC80` | 216 | UnwindData |  |
| 1139 | `WebAuthNSyncResetAccount` | `0x6BD60` | 130 | UnwindData |  |
| 1141 | `WebAuthNSyncToggleSaveLocalDevice` | `0x6BDF0` | 197 | UnwindData |  |
| 1142 | `WebAuthNSyncToggleSync` | `0x6BEC0` | 261 | UnwindData |  |
| 1053 | `VirtualChannelGetInstance` | `0x6D4C0` | 152 | UnwindData |  |
| 1123 | `WebAuthNReportPasskeyHeartbeat` | `0x6F350` | 1,080 | UnwindData |  |
| 1124 | `WebAuthNReportPasskeyHeartbeatServer` | `0x6F790` | 2,232 | UnwindData |  |
| 1015 | `EXPERIMENTAL_WebAuthNDecodeGetAssertionRequest` | `0x91FB0` | 103 | UnwindData |  |
| 1018 | `EXPERIMENTAL_WebAuthNDecodeMakeCredentialRequest` | `0x92020` | 103 | UnwindData |  |
| 1016 | `EXPERIMENTAL_WebAuthNEncodeGetAssertionResponse` | `0x92090` | 105 | UnwindData |  |
| 1017 | `EXPERIMENTAL_WebAuthNFreeDecodedGetAssertionRequest` | `0x92100` | 40 | UnwindData |  |
| 1020 | `EXPERIMENTAL_WebAuthNFreeDecodedMakeCredentialRequest` | `0x92100` | 40 | UnwindData |  |
| 1004 | `EXPERIMENTAL_WebAuthNPluginFreeAddAuthenticatorResponse` | `0x92100` | 40 | UnwindData |  |
| 1013 | `EXPERIMENTAL_WebAuthNPluginFreePerformUvResponse` | `0x92100` | 40 | UnwindData |  |
| 1019 | `EXPERIMENTAL_WebAuthNEncodeMakeCredentialResponse` | `0x96350` | 105 | UnwindData |  |
| 1001 | `EXPERIMENTAL_WebAuthNPluginAddAuthenticator` | `0x963C0` | 1,425 | UnwindData |  |
| 1006 | `EXPERIMENTAL_WebAuthNPluginAuthenticatorAddCredentials` | `0x96960` | 1,188 | UnwindData |  |
| 1027 | `EXPERIMENTAL_WebAuthNPluginAuthenticatorFreeCredentialDetailsList` | `0x96E10` | 219 | UnwindData |  |
| 1022 | `EXPERIMENTAL_WebAuthNPluginAuthenticatorGetAllCredentials` | `0x96F00` | 1,318 | UnwindData |  |
| 1010 | `EXPERIMENTAL_WebAuthNPluginAuthenticatorRemoveAllCredentials` | `0x97430` | 622 | UnwindData |  |
| 1008 | `EXPERIMENTAL_WebAuthNPluginAuthenticatorRemoveCredentials` | `0x976B0` | 1,018 | UnwindData |  |
| 1026 | `EXPERIMENTAL_WebAuthNPluginFreeGetOperationSigningPublicKeyResponse` | `0x97AB0` | 40 | UnwindData |  |
| 1021 | `EXPERIMENTAL_WebAuthNPluginGetAuthenticatorState` | `0x97AE0` | 268 | UnwindData |  |
| 1025 | `EXPERIMENTAL_WebAuthNPluginGetOperationSigningPublicKey` | `0x97C00` | 1,071 | UnwindData |  |
| 1012 | `EXPERIMENTAL_WebAuthNPluginPerformUv` | `0x98040` | 1,515 | UnwindData |  |
| 1040 | `EXPERIMENTAL_WebAuthNPluginRegisterStatusChangeCallback` | `0x98640` | 121 | UnwindData |  |
| 1002 | `EXPERIMENTAL_WebAuthNPluginRemoveAuthenticator` | `0x986C0` | 633 | UnwindData |  |
| 1041 | `EXPERIMENTAL_WebAuthNPluginUnregisterStatusChangeCallback` | `0x98940` | 77 | UnwindData |  |
| 1003 | `EXPERIMENTAL_WebAuthNPluginUpdateAuthenticatorDetails` | `0x989A0` | 807 | UnwindData |  |
| 1054 | `WebAuthNAuthenticatorDBFreeInfo` | `0x98D60` | 125 | UnwindData |  |
| 1055 | `WebAuthNAuthenticatorDBGetInfo` | `0x98DF0` | 297 | UnwindData |  |
| 1046 | `WebAuthNDecodeGetAssertionRequest` | `0x98F20` | 167 | UnwindData |  |
| 1049 | `WebAuthNDecodeMakeCredentialRequest` | `0x98FD0` | 167 | UnwindData |  |
| 1047 | `WebAuthNEncodeGetAssertionResponse` | `0x99080` | 239 | UnwindData |  |
| 1050 | `WebAuthNEncodeMakeCredentialResponse` | `0x99180` | 238 | UnwindData |  |
| 1023 | `WebAuthNPluginAddAuthenticator` | `0x99280` | 1,417 | UnwindData |  |
| 1117 | `WebAuthNPluginAddAuthenticator2` | `0x99810` | 1,372 | UnwindData |  |
| 1030 | `WebAuthNPluginAuthenticatorAddCredentials` | `0x99D80` | 1,805 | UnwindData |  |
| 1034 | `WebAuthNPluginAuthenticatorFreeCredentialDetailsArray` | `0x9A4A0` | 179 | UnwindData |  |
| 1033 | `WebAuthNPluginAuthenticatorGetAllCredentials` | `0x9A560` | 1,875 | UnwindData |  |
| 1032 | `WebAuthNPluginAuthenticatorRemoveAllCredentials` | `0x9ACC0` | 857 | UnwindData |  |
| 1031 | `WebAuthNPluginAuthenticatorRemoveCredentials` | `0x9B020` | 1,324 | UnwindData |  |
| 1118 | `WebAuthNPluginFreeAuthenticatorList` | `0x9B560` | 254 | UnwindData |  |
| 1042 | `WebAuthNPluginFreePublicKeyResponse` | `0x9B670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1119 | `WebAuthNPluginGetAuthenticatorList` | `0x9B680` | 2,644 | UnwindData |  |
| 1028 | `WebAuthNPluginGetAuthenticatorState` | `0x9C0E0` | 730 | UnwindData |  |
| 1039 | `WebAuthNPluginGetOperationSigningPublicKey` | `0x9C3C0` | 1,397 | UnwindData |  |
| 1037 | `WebAuthNPluginGetUserVerificationCount` | `0x9C940` | 1,310 | UnwindData |  |
| 1038 | `WebAuthNPluginGetUserVerificationPublicKey` | `0x9CE70` | 1,335 | UnwindData |  |
| 1035 | `WebAuthNPluginPerformUserVerification` | `0x9D3B0` | 1,753 | UnwindData |  |
| 1120 | `WebAuthNPluginPerformUserVerification2` | `0x9DA90` | 1,595 | UnwindData |  |
| 1043 | `WebAuthNPluginRegisterStatusChangeCallback` | `0x9E0E0` | 1,633 | UnwindData |  |
| 1029 | `WebAuthNPluginRemoveAuthenticator` | `0x9E750` | 835 | UnwindData |  |
| 1121 | `WebAuthNPluginSetAuthenticatorState` | `0x9EAA0` | 1,177 | UnwindData |  |
| 1044 | `WebAuthNPluginUnregisterStatusChangeCallback` | `0x9EF40` | 396 | UnwindData |  |
| 1024 | `WebAuthNPluginUpdateAuthenticatorDetails` | `0x9F0E0` | 1,772 | UnwindData |  |
| 1122 | `WebAuthNPluginUpdateAuthenticatorDetails2` | `0x9F7E0` | 1,368 | UnwindData |  |
