# Binary Specification: sechost.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sechost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `32881e3ea52060a84c1e9cd8faa728acf96d1d1229e518a267fbe0bf6b7e8469`
* **Total Exported Functions:** 246

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1222 | `RegisterTraceGuidsA` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwRegisterTraceGuidsA` |
| 1096 | `EnableTraceEx2` | `0x93C0` | 2,564 | UnwindData |  |
| 1033 | `ControlTraceA` | `0x9EA0` | 1,961 | UnwindData |  |
| 1238 | `StartTraceW` | `0xA650` | 1,912 | UnwindData |  |
| 1204 | `QueryAllTracesW` | `0xB570` | 386 | UnwindData |  |
| 1034 | `ControlTraceW` | `0xB700` | 2,759 | UnwindData |  |
| 1235 | `StartServiceCtrlDispatcherW` | `0xCB40` | 277 | UnwindData |  |
| 1138 | `I_ScSendPnPMessage` | `0xD310` | 331 | UnwindData |  |
| 1190 | `OpenSCManagerA` | `0xD470` | 413 | UnwindData |  |
| 1028 | `CloseServiceHandle` | `0xD900` | 143 | UnwindData |  |
| 1191 | `OpenSCManagerW` | `0xDF40` | 971 | UnwindData |  |
| 1216 | `QueryUserServiceName` | `0xE500` | 399 | UnwindData |  |
| 1231 | `SetServiceStatus` | `0xF480` | 404 | UnwindData |  |
| 1037 | `ConvertSidToStringSidW` | `0xF7A0` | 319 | UnwindData |  |
| 1036 | `ConvertSecurityDescriptorToStringSecurityDescriptorW` | `0xFA60` | 214 | UnwindData |  |
| 1042 | `ConvertStringSidToSidW` | `0x13FB0` | 173 | UnwindData |  |
| 1146 | `LocalGetSidForString` | `0x14770` | 336 | UnwindData |  |
| 1144 | `LocalGetConditionForString` | `0x148D0` | 2,376 | UnwindData |  |
| 1115 | `GetOperandValue` | `0x15220` | 1,700 | UnwindData |  |
| 1143 | `IsValueSizeFixed` | `0x15D40` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `FreeOperandValue` | `0x15D90` | 61 | UnwindData |  |
| 1101 | `EnumerateTraceGuidsEx` | `0x16E60` | 944 | UnwindData |  |
| 1169 | `LsaLookupGetDomainInfo` | `0x17430` | 146 | UnwindData |  |
| 1175 | `LsaLookupTranslateNames` | `0x174D0` | 82 | UnwindData |  |
| 1152 | `LookupAccountNameLocalW` | `0x17530` | 43 | UnwindData |  |
| 1176 | `LsaLookupTranslateSids` | `0x17AD0` | 50 | UnwindData |  |
| 1153 | `LookupAccountSidLocalA` | `0x17C80` | 570 | UnwindData |  |
| 1154 | `LookupAccountSidLocalW` | `0x17EC0` | 43 | UnwindData |  |
| 1172 | `LsaLookupOpenLocalPolicy` | `0x18400` | 143 | UnwindData |  |
| 1167 | `LsaLookupClose` | `0x184A0` | 136 | UnwindData |  |
| 1099 | `EnumServicesStatusExW` | `0x18B60` | 646 | UnwindData |  |
| 1207 | `QueryServiceConfig2W` | `0x18DF0` | 1,288 | UnwindData |  |
| 1041 | `ConvertStringSecurityDescriptorToSecurityDescriptorW` | `0x1A1A0` | 90 | UnwindData |  |
| 1076 | `CredReadW` | `0x1AA60` | 240 | UnwindData |  |
| 1067 | `CredProfileLoadedEx` | `0x1AB60` | 98 | UnwindData |  |
| 1086 | `CredWriteW` | `0x1ABD0` | 140 | UnwindData |  |
| 1053 | `CredEnumerateW` | `0x1ACA0` | 319 | UnwindData |  |
| 1088 | `CredpConvertOneCredentialSize` | `0x1B050` | 437 | UnwindData |  |
| 1087 | `CredpConvertCredential` | `0x1BA30` | 189 | UnwindData |  |
| 1148 | `LocalGetStringForRelativeAttribute` | `0x1C410` | 2,201 | UnwindData |  |
| 1117 | `GetOperatorIndexByToken` | `0x1CD30` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1119 | `GetPrintableOperandValue` | `0x1CE30` | 1,544 | UnwindData |  |
| 1209 | `QueryServiceConfigW` | `0x1D440` | 358 | UnwindData |  |
| 1127 | `I_QueryTagInformation` | `0x1D5D0` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1245 | `WaitServiceState` | `0x1D8A0` | 599 | UnwindData |  |
| 1240 | `SubscribeServiceChangeNotifications` | `0x1DB00` | 65 | UnwindData |  |
| 1132 | `I_ScQueryServiceConfig` | `0x1DC40` | 182 | UnwindData |  |
| 1193 | `OpenServiceW` | `0x1DD00` | 118 | UnwindData |  |
| 1213 | `QueryServiceStatusEx` | `0x1E040` | 157 | UnwindData |  |
| 1113 | `GetIdentityProviderInfoByGUID` | `0x1E6E0` | 183 | UnwindData |  |
| 1100 | `EnumerateIdentityProviders` | `0x1E810` | 227 | UnwindData |  |
| 1030 | `ControlService` | `0x1EC80` | 102 | UnwindData |  |
| 1215 | `QueryTransientObjectSecurityDescriptor` | `0x1ECF0` | 414 | UnwindData |  |
| 1107 | `FreeTransientObjectSecurityDescriptor` | `0x1F3F0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1242 | `TraceQueryInformation` | `0x1F5D0` | 1,614 | UnwindData |  |
| 1022 | `CapabilityCheck` | `0x1FDA0` | 429 | UnwindData |  |
| 1162 | `LsaICLookupNames` | `0x1FF60` | 2,091 | UnwindData |  |
| 1212 | `QueryServiceStatus` | `0x20BF0` | 97 | UnwindData |  |
| 1244 | `UnsubscribeServiceChangeNotifications` | `0x20D90` | 45 | UnwindData |  |
| 1161 | `LsaFreeMemory` | `0x20DD0` | 24 | UnwindData |  |
| 1168 | `LsaLookupFreeMemory` | `0x20DD0` | 24 | UnwindData |  |
| 1178 | `LsaOpenPolicy` | `0x21B70` | 555 | UnwindData |  |
| 1112 | `GetEmbeddedImageMitigationPolicy` | `0x220C0` | 344 | UnwindData |  |
| 1062 | `CredIsProtectedW` | `0x22790` | 208 | UnwindData |  |
| 1079 | `CredUnmarshalCredentialW` | `0x22870` | 665 | UnwindData |  |
| 1236 | `StartServiceW` | `0x22B10` | 102 | UnwindData |  |
| 1156 | `LsaClose` | `0x22B80` | 109 | UnwindData |  |
| 1199 | `ProcessTrace` | `0x22DD0` | 1,170 | UnwindData |  |
| 1133 | `I_ScRegisterDeviceNotification` | `0x232F0` | 937 | UnwindData |  |
| 1141 | `I_ScValidatePnPService` | `0x23830` | 279 | UnwindData |  |
| 1177 | `LsaLookupUserAccountType` | `0x23D30` | 196 | UnwindData |  |
| 1223 | `ReleaseIdentityProviderEnumContext` | `0x23E00` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `ControlServiceExW` | `0x24160` | 330 | UnwindData |  |
| 1180 | `LsaQueryInformationPolicy` | `0x242B0` | 355 | UnwindData |  |
| 1140 | `I_ScUnregisterDeviceNotification` | `0x24950` | 165 | UnwindData |  |
| 1029 | `CloseTrace` | `0x24DC0` | 309 | UnwindData |  |
| 1122 | `GetServiceKeyNameW` | `0x25050` | 197 | UnwindData |  |
| 1198 | `OpenTraceW` | `0x25560` | 954 | UnwindData |  |
| 1192 | `OpenServiceA` | `0x25D40` | 116 | UnwindData |  |
| 1114 | `GetIdentityProviderInfoByName` | `0x25DC0` | 227 | UnwindData |  |
| 1187 | `NotifyServiceStatusChange` | `0x26320` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1189 | `NotifyServiceStatusChangeW` | `0x26320` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1124 | `GetServiceRegistryStateKey` | `0x264D0` | 102 | UnwindData |  |
| 1188 | `NotifyServiceStatusChangeA` | `0x26600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `LsaLookupSids` | `0x26620` | 38 | UnwindData |  |
| 1020 | `BuildSecurityDescriptorForSharingAccess` | `0x26810` | 23 | UnwindData |  |
| 1021 | `BuildSecurityDescriptorForSharingAccessEx` | `0x26830` | 874 | UnwindData |  |
| 1104 | `EventAccessRemove` | `0x26BD0` | 782 | UnwindData |  |
| 1131 | `I_ScPnPGetServiceName` | `0x26EF0` | 73 | UnwindData |  |
| 1164 | `LsaICLookupSids` | `0x26F40` | 1,113 | UnwindData |  |
| 1009 | `AuditFree` | `0x273A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `CredFree` | `0x273A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `I_RegisterSvchostNotificationCallback` | `0x273E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `RpcClientCapabilityCheck` | `0x27400` | 283 | UnwindData |  |
| 1090 | `CredpDecodeCredential` | `0x27670` | 69 | UnwindData |  |
| 1170 | `LsaLookupManageSidNameMapping` | `0x276C0` | 247 | UnwindData |  |
| 1151 | `LookupAccountNameLocalA` | `0x27BC0` | 369 | UnwindData |  |
| 1220 | `RegisterServiceCtrlHandlerExW` | `0x28120` | 4,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1147 | `LocalGetStringForCondition` | `0x29290` | 54 | UnwindData |  |
| 1109 | `GetDefaultIdentityProvider` | `0x2CB50` | 94 | UnwindData |  |
| 1035 | `ConvertSDToStringSDRootDomainW` | `0x2F4B0` | 115 | UnwindData |  |
| 1038 | `ConvertStringSDToSDDomainA` | `0x2F530` | 316 | UnwindData |  |
| 1039 | `ConvertStringSDToSDDomainW` | `0x2F680` | 198 | UnwindData |  |
| 1040 | `ConvertStringSDToSDRootDomainW` | `0x2F750` | 105 | UnwindData |  |
| 1093 | `DecodeAttributeName` | `0x2FD60` | 509 | UnwindData |  |
| 1097 | `EncodeAttributeName` | `0x2FF70` | 310 | UnwindData |  |
| 1108 | `GetCharFromDigit` | `0x30110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1110 | `GetDigitFromChar` | `0x30130` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1116 | `GetOperatorCodeAtIndex` | `0x30240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1118 | `GetOperatorUnaryAtIndex` | `0x30260` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1142 | `IsArrayType` | `0x303C0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `LocalGetReferencedTokenTypesForCondition` | `0x30490` | 77 | UnwindData |  |
| 1023 | `CapabilityCheckForSingleSessionSku` | `0x48100` | 102 | UnwindData |  |
| 1149 | `LocalRpcBindingCreateWithSecurity` | `0x48350` | 419 | UnwindData |  |
| 1150 | `LocalRpcBindingSetAuthInfoEx` | `0x48500` | 259 | UnwindData |  |
| 1228 | `SetLocalRpcServerInterfaceSecurity` | `0x48610` | 218 | UnwindData |  |
| 1229 | `SetLocalRpcServerProtseqSecurity` | `0x486F0` | 117 | UnwindData |  |
| 1003 | `I_ScSetServiceBitsA` | `0x48860` | 29 | UnwindData |  |
| 1004 | `I_ScSetServiceBitsW` | `0x48890` | 139 | UnwindData |  |
| 1024 | `ChangeServiceConfig2A` | `0x48C20` | 440 | UnwindData |  |
| 1025 | `ChangeServiceConfig2W` | `0x48DE0` | 191 | UnwindData |  |
| 1026 | `ChangeServiceConfigA` | `0x48EB0` | 701 | UnwindData |  |
| 1027 | `ChangeServiceConfigW` | `0x49180` | 399 | UnwindData |  |
| 1031 | `ControlServiceExA` | `0x49320` | 323 | UnwindData |  |
| 1045 | `CreateServiceA` | `0x49470` | 1,740 | UnwindData |  |
| 1046 | `CreateServiceEx` | `0x49B50` | 976 | UnwindData |  |
| 1047 | `CreateServiceW` | `0x49F30` | 950 | UnwindData |  |
| 1095 | `DeleteService` | `0x4A2F0` | 94 | UnwindData |  |
| 1098 | `EnumDependentServicesW` | `0x4A360` | 425 | UnwindData |  |
| 1120 | `GetServiceDirectory` | `0x4A510` | 113 | UnwindData |  |
| 1121 | `GetServiceDisplayNameW` | `0x4A590` | 197 | UnwindData |  |
| 1123 | `GetServiceProcessToken` | `0x4A660` | 97 | UnwindData |  |
| 1125 | `GetSharedServiceDirectory` | `0x4A6D0` | 120 | UnwindData |  |
| 1126 | `GetSharedServiceRegistryStateKey` | `0x4A750` | 108 | UnwindData |  |
| 1129 | `I_ScBroadcastServiceControlMessage` | `0x4A7D0` | 201 | UnwindData |  |
| 1139 | `I_ScSendTSMessage` | `0x4A7D0` | 201 | UnwindData |  |
| 1134 | `I_ScRegisterPreshutdownRestart` | `0x4A8A0` | 168 | UnwindData |  |
| 1135 | `I_ScReparseServiceDatabase` | `0x4A950` | 151 | UnwindData |  |
| 1205 | `QueryLocalUserServiceName` | `0x4A9F0` | 824 | UnwindData |  |
| 1206 | `QueryServiceConfig2A` | `0x4AD30` | 1,152 | UnwindData |  |
| 1208 | `QueryServiceConfigA` | `0x4B1C0` | 269 | UnwindData |  |
| 1211 | `QueryServiceObjectSecurity` | `0x4B2E0` | 183 | UnwindData |  |
| 1217 | `QueryUserServiceNameForContext` | `0x4B3A0` | 146 | UnwindData |  |
| 1225 | `ReparseServiceConfig` | `0x4B440` | 97 | UnwindData |  |
| 1227 | `ScSendSynchronousPowerMessage` | `0x4B4B0` | 212 | UnwindData |  |
| 1230 | `SetServiceObjectSecurity` | `0x4B590` | 323 | UnwindData |  |
| 1233 | `StartServiceA` | `0x4B6E0` | 102 | UnwindData |  |
| 1130 | `I_ScIsSecurityProcess` | `0x4BB30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `QueryServiceDynamicInformation` | `0x4BB40` | 144 | UnwindData |  |
| 1218 | `RegisterServiceCtrlHandlerA` | `0x4BBE0` | 100 | UnwindData |  |
| 1219 | `RegisterServiceCtrlHandlerExA` | `0x4BC50` | 115 | UnwindData |  |
| 1221 | `RegisterServiceCtrlHandlerW` | `0x4BCD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `StartServiceCtrlDispatcherA` | `0x4BCF0` | 309 | UnwindData |  |
| 1136 | `I_ScRpcBindA` | `0x4C8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `I_ScRpcBindW` | `0x4C8E0` | 31 | UnwindData |  |
| 1000 | *Ordinal Only* | `0x4F910` | 112 | UnwindData |  |
| 1194 | `OpenTraceFromBufferStream` | `0x4F990` | 428 | UnwindData |  |
| 1195 | `OpenTraceFromFile` | `0x4FB50` | 498 | UnwindData |  |
| 1196 | `OpenTraceFromRealTimeLogger` | `0x4FD50` | 26 | UnwindData |  |
| 1197 | `OpenTraceFromRealTimeLoggerWithAllocationOptions` | `0x4FD70` | 744 | UnwindData |  |
| 1200 | `ProcessTraceAddBufferToBufferStream` | `0x50060` | 290 | UnwindData |  |
| 1201 | `ProcessTraceBufferDecrementReference` | `0x50190` | 253 | UnwindData |  |
| 1202 | `ProcessTraceBufferIncrementReference` | `0x502A0` | 165 | UnwindData |  |
| 1214 | `QueryTraceProcessingHandle` | `0x50350` | 898 | UnwindData |  |
| 1224 | `RemoveTraceCallback` | `0x506E0` | 434 | UnwindData |  |
| 1232 | `SetTraceCallback` | `0x508A0` | 546 | UnwindData |  |
| 1001 | *Ordinal Only* | `0x50AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | *Ordinal Only* | `0x50AE0` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1102 | `EventAccessControl` | `0x50F10` | 506 | UnwindData |  |
| 1103 | `EventAccessQuery` | `0x51110` | 798 | UnwindData |  |
| 1203 | `QueryAllTracesA` | `0x51440` | 149 | UnwindData |  |
| 1237 | `StartTraceA` | `0x514E0` | 1,753 | UnwindData |  |
| 1239 | `StopTraceW` | `0x51BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1241 | `TraceConfigureLastBranchRecord` | `0x51BE0` | 400 | UnwindData |  |
| 1243 | `TraceSetInformation` | `0x51D80` | 3,090 | UnwindData |  |
| 1155 | `LsaAddAccountRights` | `0x56C40` | 134 | UnwindData |  |
| 1159 | `LsaEnumerateAccountRights` | `0x56CD0` | 199 | UnwindData |  |
| 1160 | `LsaEnumerateAccountsWithUserRight` | `0x56DA0` | 187 | UnwindData |  |
| 1182 | `LsaRemoveAccountRights` | `0x56E70` | 148 | UnwindData |  |
| 1158 | `LsaDelete` | `0x56F10` | 120 | UnwindData |  |
| 1163 | `LsaICLookupNamesWithCreds` | `0x56F90` | 464 | UnwindData |  |
| 1165 | `LsaICLookupSidsWithCreds` | `0x57170` | 549 | UnwindData |  |
| 1166 | `LsaIOpenPolicyWithCreds` | `0x574D0` | 233 | UnwindData |  |
| 1171 | `LsaLookupNames2` | `0x575C0` | 100 | UnwindData |  |
| 1174 | `LsaLookupSids2` | `0x57630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1184 | `LsaSetInformationPolicy` | `0x57640` | 287 | UnwindData |  |
| 1157 | `LsaCreateSecret` | `0x57940` | 382 | UnwindData |  |
| 1179 | `LsaOpenSecret` | `0x57AD0` | 381 | UnwindData |  |
| 1181 | `LsaQuerySecret` | `0x57C60` | 164 | UnwindData |  |
| 1183 | `LsaRetrievePrivateData` | `0x580A0` | 260 | UnwindData |  |
| 1185 | `LsaSetSecret` | `0x58430` | 118 | UnwindData |  |
| 1186 | `LsaStorePrivateData` | `0x58660` | 165 | UnwindData |  |
| 1005 | `AuditComputeEffectivePolicyBySid` | `0x59920` | 397 | UnwindData |  |
| 1006 | `AuditEnumerateCategories` | `0x59AC0` | 298 | UnwindData |  |
| 1007 | `AuditEnumeratePerUserPolicy` | `0x59BF0` | 103 | UnwindData |  |
| 1008 | `AuditEnumerateSubCategories` | `0x59C60` | 329 | UnwindData |  |
| 1010 | `AuditLookupCategoryNameW` | `0x59DB0` | 336 | UnwindData |  |
| 1011 | `AuditLookupSubCategoryNameW` | `0x59F10` | 336 | UnwindData |  |
| 1012 | `AuditQueryGlobalSaclW` | `0x5A070` | 94 | UnwindData |  |
| 1013 | `AuditQueryPerUserPolicy` | `0x5A0E0` | 100 | UnwindData |  |
| 1014 | `AuditQuerySecurity` | `0x5A150` | 178 | UnwindData |  |
| 1015 | `AuditQuerySystemPolicy` | `0x5A210` | 93 | UnwindData |  |
| 1016 | `AuditSetGlobalSaclW` | `0x5A280` | 94 | UnwindData |  |
| 1017 | `AuditSetPerUserPolicy` | `0x5A2F0` | 86 | UnwindData |  |
| 1018 | `AuditSetSecurity` | `0x5A350` | 300 | UnwindData |  |
| 1019 | `AuditSetSystemPolicy` | `0x5A490` | 73 | UnwindData |  |
| 1048 | `CredBackupCredentials` | `0x5A720` | 374 | UnwindData |  |
| 1049 | `CredDeleteA` | `0x5A8A0` | 154 | UnwindData |  |
| 1050 | `CredDeleteW` | `0x5A940` | 154 | UnwindData |  |
| 1052 | `CredEnumerateA` | `0x5A9E0` | 266 | UnwindData |  |
| 1054 | `CredFindBestCredentialA` | `0x5AAF0` | 239 | UnwindData |  |
| 1055 | `CredFindBestCredentialW` | `0x5ABF0` | 240 | UnwindData |  |
| 1057 | `CredGetSessionTypes` | `0x5ACF0` | 103 | UnwindData |  |
| 1058 | `CredGetTargetInfoA` | `0x5AD60` | 217 | UnwindData |  |
| 1059 | `CredGetTargetInfoW` | `0x5AE40` | 217 | UnwindData |  |
| 1066 | `CredProfileLoaded` | `0x5AF20` | 94 | UnwindData |  |
| 1068 | `CredProfileUnloaded` | `0x5AF90` | 94 | UnwindData |  |
| 1072 | `CredReadA` | `0x5B000` | 239 | UnwindData |  |
| 1073 | `CredReadByTokenHandle` | `0x5B100` | 300 | UnwindData |  |
| 1074 | `CredReadDomainCredentialsA` | `0x5B240` | 266 | UnwindData |  |
| 1075 | `CredReadDomainCredentialsW` | `0x5B350` | 278 | UnwindData |  |
| 1077 | `CredRestoreCredentials` | `0x5B470` | 339 | UnwindData |  |
| 1083 | `CredWriteA` | `0x5B5D0` | 140 | UnwindData |  |
| 1084 | `CredWriteDomainCredentialsA` | `0x5B670` | 207 | UnwindData |  |
| 1085 | `CredWriteDomainCredentialsW` | `0x5B750` | 205 | UnwindData |  |
| 1051 | `CredEncryptAndMarshalBinaryBlob` | `0x5B830` | 40 | UnwindData |  |
| 1060 | `CredIsMarshaledCredentialW` | `0x5B860` | 61 | UnwindData |  |
| 1061 | `CredIsProtectedA` | `0x5B8B0` | 141 | UnwindData |  |
| 1063 | `CredMarshalCredentialA` | `0x5B950` | 106 | UnwindData |  |
| 1064 | `CredMarshalCredentialW` | `0x5B9C0` | 477 | UnwindData |  |
| 1069 | `CredProtectA` | `0x5BBB0` | 372 | UnwindData |  |
| 1070 | `CredProtectEx` | `0x5BD30` | 380 | UnwindData |  |
| 1071 | `CredProtectW` | `0x5BEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `CredUnmarshalCredentialA` | `0x5BEE0` | 159 | UnwindData |  |
| 1080 | `CredUnprotectA` | `0x5BF90` | 398 | UnwindData |  |
| 1081 | `CredUnprotectEx` | `0x5C130` | 304 | UnwindData |  |
| 1082 | `CredUnprotectW` | `0x5C270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `CredpConvertTargetInfo` | `0x5C290` | 592 | UnwindData |  |
| 1091 | `CredpEncodeCredential` | `0x5C800` | 127 | UnwindData |  |
| 1092 | `CredpEncodeSecret` | `0x5C890` | 44 | UnwindData |  |
| 1065 | `CredParseUserNameWithType` | `0x5D2C0` | 410 | UnwindData |  |
| 1105 | `FreeContainer` | `0x5DD70` | 69 | UnwindData |  |
| 1111 | `GetEmbeddedContainerIsolationPolicy` | `0x5DDC0` | 324 | UnwindData |  |
| 1043 | `CreateIsolatedProcess` | `0x67520` | 157 | UnwindData |  |
| 1044 | `CreateIsolationContainer` | `0x675D0` | 114 | UnwindData |  |
| 1094 | `DeleteIsolationContainer` | `0x67650` | 494 | UnwindData |  |
