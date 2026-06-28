# Binary Specification: webauthn.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\webauthn.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `98206b874e2cc2c5e8f0e992b23acb4e2295e5db4c2a6c7b30a4f59110405a1e`
* **Total Exported Functions:** 150

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1106 | `WebAuthNGetApiVersionNumber` | `0x7E10` | 319 | UnwindData |  |
| 1005 | `CryptsvcDllCtrl` | `0x82F0` | 158 | UnwindData |  |
| 1093 | `WebAuthNCtapStopDeviceChangeNotify` | `0x10C70` | 10,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `I_WebAuthNCtapEncodeMakeCredentialRpcRequest` | `0x134E0` | 1,488 | UnwindData |  |
| 1056 | `WebAuthNAuthenticatorGetAssertion` | `0x15710` | 112 | UnwindData |  |
| 1116 | `WebAuthNIsUserVerifyingPlatformAuthenticatorAvailable` | `0x16860` | 2,452 | UnwindData |  |
| 1140 | `WebAuthNWriteEventCleanedupLocalStore` | `0x2B640` | 91 | UnwindData |  |
| 1141 | `WebAuthNWriteEventCloudStoreOperationFailure` | `0x2B6B0` | 71 | UnwindData |  |
| 1142 | `WebAuthNWriteEventCloudStoreOperationSuccess` | `0x2B700` | 63 | UnwindData |  |
| 1143 | `WebAuthNWriteEventCreatedUserStorage` | `0x2B750` | 46 | UnwindData |  |
| 1144 | `WebAuthNWriteEventDeletedTrustGroup` | `0x2B790` | 91 | UnwindData |  |
| 1145 | `WebAuthNWriteEventKeyRotationFailure` | `0x2B800` | 50 | UnwindData |  |
| 1146 | `WebAuthNWriteEventKeyRotationSuccess` | `0x2B840` | 50 | UnwindData |  |
| 1147 | `WebAuthNWriteEventLocalStoreOperationFailure` | `0x2B880` | 71 | UnwindData |  |
| 1148 | `WebAuthNWriteEventLocalStoreOperationSuccess` | `0x2B8D0` | 63 | UnwindData |  |
| 1149 | `WebAuthNWriteEventSyncState` | `0x2B920` | 50 | UnwindData |  |
| 1150 | `WebAuthNWriteEventSyncTrustedGroupDeletion` | `0x2B960` | 91 | UnwindData |  |
| 1007 | `I_WebAuthNCtapDecodeGetAssertionRpcResponse` | `0x36790` | 5,440 | UnwindData |  |
| 1009 | `I_WebAuthNCtapDecodeMakeCredentialRpcResponse` | `0x37CE0` | 6,248 | UnwindData |  |
| 1011 | `I_WebAuthNCtapEncodeGetAssertionRpcRequest` | `0x39550` | 1,218 | UnwindData |  |
| 1074 | `WebAuthNCtapManageFreeDisplayCredentials` | `0x3AEB0` | 71 | UnwindData |  |
| 1059 | `WebAuthNCtapChangeClientPin` | `0x46F10` | 462 | UnwindData |  |
| 1060 | `WebAuthNCtapChangeClientPinForSelectedDevice` | `0x470F0` | 702 | UnwindData |  |
| 1061 | `WebAuthNCtapFreeSelectedDeviceInformation` | `0x473C0` | 20 | UnwindData |  |
| 1105 | `WebAuthNFreeUserEntityList` | `0x473C0` | 20 | UnwindData |  |
| 1062 | `WebAuthNCtapGetAssertion` | `0x473E0` | 1,989 | UnwindData |  |
| 1063 | `WebAuthNCtapGetSupportedTransports` | `0x47BB0` | 691 | UnwindData |  |
| 1064 | `WebAuthNCtapGetWnfLocalizedString` | `0x47E70` | 636 | UnwindData |  |
| 1065 | `WebAuthNCtapIsStopSendCommandError` | `0x48100` | 97 | UnwindData |  |
| 1066 | `WebAuthNCtapMakeCredential` | `0x48170` | 1,635 | UnwindData |  |
| 1067 | `WebAuthNCtapManageAuthenticatePin` | `0x487E0` | 374 | UnwindData |  |
| 1068 | `WebAuthNCtapManageCancelEnrollFingerprint` | `0x48960` | 220 | UnwindData |  |
| 1069 | `WebAuthNCtapManageChangePin` | `0x48A50` | 511 | UnwindData |  |
| 1070 | `WebAuthNCtapManageClose` | `0x48C60` | 151 | UnwindData |  |
| 1071 | `WebAuthNCtapManageDeleteCredential` | `0x48D00` | 265 | UnwindData |  |
| 1072 | `WebAuthNCtapManageEnableEnterpriseAttestation` | `0x48E10` | 133 | UnwindData |  |
| 1073 | `WebAuthNCtapManageEnrollFingerprint` | `0x48EA0` | 619 | UnwindData |  |
| 1075 | `WebAuthNCtapManageGetDisplayCredentials` | `0x49120` | 1,551 | UnwindData |  |
| 1076 | `WebAuthNCtapManageGetLargeBlobs` | `0x49740` | 354 | UnwindData |  |
| 1077 | `WebAuthNCtapManageRemoveFingerprints` | `0x498B0` | 371 | UnwindData |  |
| 1078 | `WebAuthNCtapManageResetDevice` | `0x49A30` | 611 | UnwindData |  |
| 1079 | `WebAuthNCtapManageSelect` | `0x49CA0` | 325 | UnwindData |  |
| 1080 | `WebAuthNCtapManageSetAlwaysUv` | `0x49DF0` | 149 | UnwindData |  |
| 1081 | `WebAuthNCtapManageSetLargeBlobs` | `0x49E90` | 189 | UnwindData |  |
| 1082 | `WebAuthNCtapManageSetMinPinLength` | `0x49F60` | 190 | UnwindData |  |
| 1083 | `WebAuthNCtapManageSetPin` | `0x4A030` | 392 | UnwindData |  |
| 1084 | `WebAuthNCtapParseAuthenticatorData` | `0x4A1C0` | 193 | UnwindData |  |
| 1085 | `WebAuthNCtapResetDevice` | `0x4A290` | 147 | UnwindData |  |
| 1086 | `WebAuthNCtapRpcGetAssertionUserList` | `0x4A330` | 853 | UnwindData |  |
| 1087 | `WebAuthNCtapRpcGetCborCommand` | `0x4A690` | 286 | UnwindData |  |
| 1088 | `WebAuthNCtapRpcRenderQrCode` | `0x4A7C0` | 429 | UnwindData |  |
| 1089 | `WebAuthNCtapRpcSelectGetAssertion` | `0x4A980` | 610 | UnwindData |  |
| 1090 | `WebAuthNCtapSendCommand` | `0x4ABF0` | 1,583 | UnwindData |  |
| 1091 | `WebAuthNCtapSetClientPin` | `0x4B230` | 362 | UnwindData |  |
| 1092 | `WebAuthNCtapStartDeviceChangeNotify` | `0x4B3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1094 | `WebAuthNCtapVerifyGetAssertion` | `0x4B3B0` | 625 | UnwindData |  |
| 1101 | `WebAuthNFreeCredentialAttestation` | `0x4B630` | 128 | UnwindData |  |
| 1110 | `WebAuthNGetCredentialIdFromAuthenticatorData` | `0x4B6C0` | 187 | UnwindData |  |
| 1111 | `WebAuthNGetErrorName` | `0x4B790` | 40 | UnwindData |  |
| 1115 | `WebAuthNGetW3CExceptionDOMError` | `0x4B7C0` | 34 | UnwindData |  |
| 1014 | `EXPERIMENTAL_WebAuthNIsUserVerifyingNativePlatformAuthenticatorAvailable` | `0x51B70` | 63 | UnwindData |  |
| 1057 | `WebAuthNAuthenticatorMakeCredential` | `0x51C70` | 141 | UnwindData |  |
| 1058 | `WebAuthNCancelCurrentOperation` | `0x51D10` | 17 | UnwindData |  |
| 1099 | `WebAuthNFreeAssertion` | `0x51D30` | 110 | UnwindData |  |
| 1100 | `WebAuthNFreeAuthenticatorList` | `0x51DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1102 | `WebAuthNFreeDecodedAccountInformation` | `0x51DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1103 | `WebAuthNFreeEncodedAccountInformation` | `0x51DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `WebAuthNFreePlatformCredentialList` | `0x51DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1124 | `WebAuthNSyncFreeSyncStatus` | `0x51DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1107 | `WebAuthNGetAuthenticatorList` | `0x51DC0` | 167 | UnwindData |  |
| 1108 | `WebAuthNGetCancellationId` | `0x51E70` | 95 | UnwindData |  |
| 1109 | `WebAuthNGetCoseAlgorithmIdentifier` | `0x51EE0` | 85 | UnwindData |  |
| 1095 | `WebAuthNDecodeAccountInformation` | `0x66420` | 142 | UnwindData |  |
| 1096 | `WebAuthNDeletePlatformCredential` | `0x664C0` | 469 | UnwindData |  |
| 1097 | `WebAuthNDeletePlatformCredentialServer` | `0x666A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1098 | `WebAuthNEncodeAccountInformation` | `0x666B0` | 147 | UnwindData |  |
| 1112 | `WebAuthNGetPlatformCredentialList` | `0x66750` | 922 | UnwindData |  |
| 1113 | `WebAuthNGetPlatformCredentialListServer` | `0x66AF0` | 1,995 | UnwindData |  |
| 1114 | `WebAuthNGetPlatformCredentialListSettings` | `0x672D0` | 21 | UnwindData |  |
| 1129 | `WebAuthNSyncIsFirstPartyProviderSupported` | `0x672F0` | 61 | UnwindData |  |
| 1132 | `WebAuthNSyncIsThirdPartyProviderSupported` | `0x67340` | 92 | UnwindData |  |
| 1133 | `WebAuthNSyncOTSApi` | `0x68940` | 1,049 | UnwindData |  |
| 1137 | `WebAuthNSyncRunSettingsOTS` | `0x68D60` | 21 | UnwindData |  |
| 1122 | `WebAuthNSyncAddTrustedDevice` | `0x6DC10` | 138 | UnwindData |  |
| 1123 | `WebAuthNSyncCheckEnableSaveLocalDevice` | `0x6DCA0` | 217 | UnwindData |  |
| 1125 | `WebAuthNSyncFreeTrustedDeviceList` | `0x6DD80` | 80 | UnwindData |  |
| 1126 | `WebAuthNSyncGetSyncStatus` | `0x6DDE0` | 619 | UnwindData |  |
| 1127 | `WebAuthNSyncGetTrustedDeviceList` | `0x6E060` | 1,469 | UnwindData |  |
| 1128 | `WebAuthNSyncInvalidateCredentialCache` | `0x6E630` | 43 | UnwindData |  |
| 1130 | `WebAuthNSyncIsSaveLocalDeviceEnabled` | `0x6E670` | 370 | UnwindData |  |
| 1131 | `WebAuthNSyncIsSyncEnabled` | `0x6E7F0` | 188 | UnwindData |  |
| 1134 | `WebAuthNSyncRemoveTrustedDevice` | `0x6E8C0` | 130 | UnwindData |  |
| 1135 | `WebAuthNSyncRenameTrustedDevice` | `0x6E950` | 216 | UnwindData |  |
| 1136 | `WebAuthNSyncResetAccount` | `0x6EA30` | 130 | UnwindData |  |
| 1138 | `WebAuthNSyncToggleSaveLocalDevice` | `0x6EAC0` | 197 | UnwindData |  |
| 1139 | `WebAuthNSyncToggleSync` | `0x6EB90` | 261 | UnwindData |  |
| 1053 | `VirtualChannelGetInstance` | `0x70120` | 152 | UnwindData |  |
| 1120 | `WebAuthNReportPasskeyHeartbeat` | `0x71DC0` | 1,023 | UnwindData |  |
| 1121 | `WebAuthNReportPasskeyHeartbeatServer` | `0x721D0` | 1,983 | UnwindData |  |
| 1015 | `EXPERIMENTAL_WebAuthNDecodeGetAssertionRequest` | `0x94260` | 103 | UnwindData |  |
| 1018 | `EXPERIMENTAL_WebAuthNDecodeMakeCredentialRequest` | `0x942D0` | 103 | UnwindData |  |
| 1016 | `EXPERIMENTAL_WebAuthNEncodeGetAssertionResponse` | `0x94340` | 105 | UnwindData |  |
| 1017 | `EXPERIMENTAL_WebAuthNFreeDecodedGetAssertionRequest` | `0x943B0` | 40 | UnwindData |  |
| 1020 | `EXPERIMENTAL_WebAuthNFreeDecodedMakeCredentialRequest` | `0x943B0` | 40 | UnwindData |  |
| 1019 | `EXPERIMENTAL_WebAuthNEncodeMakeCredentialResponse` | `0x98730` | 105 | UnwindData |  |
| 1001 | `EXPERIMENTAL_WebAuthNPluginAddAuthenticator` | `0x987A0` | 1,111 | UnwindData |  |
| 1006 | `EXPERIMENTAL_WebAuthNPluginAuthenticatorAddCredentials` | `0x98C00` | 1,020 | UnwindData |  |
| 1027 | `EXPERIMENTAL_WebAuthNPluginAuthenticatorFreeCredentialDetailsList` | `0x99010` | 219 | UnwindData |  |
| 1022 | `EXPERIMENTAL_WebAuthNPluginAuthenticatorGetAllCredentials` | `0x99100` | 1,244 | UnwindData |  |
| 1010 | `EXPERIMENTAL_WebAuthNPluginAuthenticatorRemoveAllCredentials` | `0x995F0` | 553 | UnwindData |  |
| 1008 | `EXPERIMENTAL_WebAuthNPluginAuthenticatorRemoveCredentials` | `0x99820` | 941 | UnwindData |  |
| 1004 | `EXPERIMENTAL_WebAuthNPluginFreeAddAuthenticatorResponse` | `0x99BE0` | 40 | UnwindData |  |
| 1013 | `EXPERIMENTAL_WebAuthNPluginFreePerformUvResponse` | `0x99BE0` | 40 | UnwindData |  |
| 1048 | `WebAuthNFreeDecodedGetAssertionRequest` | `0x99BE0` | 40 | UnwindData |  |
| 1051 | `WebAuthNFreeDecodedMakeCredentialRequest` | `0x99BE0` | 40 | UnwindData |  |
| 1045 | `WebAuthNPluginFreeAddAuthenticatorResponse` | `0x99BE0` | 40 | UnwindData |  |
| 1026 | `EXPERIMENTAL_WebAuthNPluginFreeGetOperationSigningPublicKeyResponse` | `0x99C10` | 40 | UnwindData |  |
| 1042 | `WebAuthNPluginFreePublicKeyResponse` | `0x99C10` | 40 | UnwindData |  |
| 1021 | `EXPERIMENTAL_WebAuthNPluginGetAuthenticatorState` | `0x99C40` | 275 | UnwindData |  |
| 1025 | `EXPERIMENTAL_WebAuthNPluginGetOperationSigningPublicKey` | `0x99D60` | 753 | UnwindData |  |
| 1012 | `EXPERIMENTAL_WebAuthNPluginPerformUv` | `0x9A060` | 1,085 | UnwindData |  |
| 1040 | `EXPERIMENTAL_WebAuthNPluginRegisterStatusChangeCallback` | `0x9A4B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `EXPERIMENTAL_WebAuthNPluginRemoveAuthenticator` | `0x9A4C0` | 564 | UnwindData |  |
| 1041 | `EXPERIMENTAL_WebAuthNPluginUnregisterStatusChangeCallback` | `0x9A700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `EXPERIMENTAL_WebAuthNPluginUpdateAuthenticatorDetails` | `0x9A710` | 731 | UnwindData |  |
| 1054 | `WebAuthNAuthenticatorDBFreeInfo` | `0x9AA80` | 77 | UnwindData |  |
| 1055 | `WebAuthNAuthenticatorDBGetInfo` | `0x9AAE0` | 330 | UnwindData |  |
| 1046 | `WebAuthNDecodeGetAssertionRequest` | `0x9AC30` | 243 | UnwindData |  |
| 1049 | `WebAuthNDecodeMakeCredentialRequest` | `0x9AD30` | 243 | UnwindData |  |
| 1047 | `WebAuthNEncodeGetAssertionResponse` | `0x9AE30` | 296 | UnwindData |  |
| 1050 | `WebAuthNEncodeMakeCredentialResponse` | `0x9AF60` | 290 | UnwindData |  |
| 1023 | `WebAuthNPluginAddAuthenticator` | `0x9B090` | 1,258 | UnwindData |  |
| 1030 | `WebAuthNPluginAuthenticatorAddCredentials` | `0x9B580` | 1,543 | UnwindData |  |
| 1034 | `WebAuthNPluginAuthenticatorFreeCredentialDetailsArray` | `0x9BB90` | 199 | UnwindData |  |
| 1033 | `WebAuthNPluginAuthenticatorGetAllCredentials` | `0x9BC60` | 1,808 | UnwindData |  |
| 1032 | `WebAuthNPluginAuthenticatorRemoveAllCredentials` | `0x9C380` | 789 | UnwindData |  |
| 1031 | `WebAuthNPluginAuthenticatorRemoveCredentials` | `0x9C6A0` | 1,261 | UnwindData |  |
| 1117 | `WebAuthNPluginFreeAuthenticatorList` | `0x9CBA0` | 254 | UnwindData |  |
| 1036 | `WebAuthNPluginFreeUserVerificationResponse` | `0x9CCB0` | 45 | UnwindData |  |
| 1118 | `WebAuthNPluginGetAuthenticatorList` | `0x9CCF0` | 2,615 | UnwindData |  |
| 1028 | `WebAuthNPluginGetAuthenticatorState` | `0x9D730` | 525 | UnwindData |  |
| 1039 | `WebAuthNPluginGetOperationSigningPublicKey` | `0x9D950` | 1,117 | UnwindData |  |
| 1037 | `WebAuthNPluginGetUserVerificationCount` | `0x9DDC0` | 975 | UnwindData |  |
| 1038 | `WebAuthNPluginGetUserVerificationPublicKey` | `0x9E1A0` | 997 | UnwindData |  |
| 1035 | `WebAuthNPluginPerformUserVerification` | `0x9E590` | 1,430 | UnwindData |  |
| 1043 | `WebAuthNPluginRegisterStatusChangeCallback` | `0x9EB30` | 1,491 | UnwindData |  |
| 1029 | `WebAuthNPluginRemoveAuthenticator` | `0x9F110` | 796 | UnwindData |  |
| 1119 | `WebAuthNPluginSetAuthenticatorState` | `0x9F440` | 988 | UnwindData |  |
| 1044 | `WebAuthNPluginUnregisterStatusChangeCallback` | `0x9F830` | 299 | UnwindData |  |
| 1024 | `WebAuthNPluginUpdateAuthenticatorDetails` | `0x9F970` | 1,199 | UnwindData |  |
