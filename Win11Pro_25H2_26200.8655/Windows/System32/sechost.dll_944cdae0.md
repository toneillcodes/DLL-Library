# Binary Specification: sechost.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sechost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `944cdae0366f98115c1a7725cfce00ee261f238510a670d98a8d552bdf2943e2`
* **Total Exported Functions:** 246

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1222 | `RegisterTraceGuidsA` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.EtwRegisterTraceGuidsA` |
| 1096 | `EnableTraceEx2` | `0x86E0` | 2,564 | UnwindData |  |
| 1033 | `ControlTraceA` | `0x91C0` | 1,961 | UnwindData |  |
| 1238 | `StartTraceW` | `0x9970` | 1,912 | UnwindData |  |
| 1204 | `QueryAllTracesW` | `0xA890` | 386 | UnwindData |  |
| 1034 | `ControlTraceW` | `0xAA20` | 2,759 | UnwindData |  |
| 1235 | `StartServiceCtrlDispatcherW` | `0xBE60` | 277 | UnwindData |  |
| 1138 | `I_ScSendPnPMessage` | `0xC630` | 331 | UnwindData |  |
| 1190 | `OpenSCManagerA` | `0xC790` | 413 | UnwindData |  |
| 1028 | `CloseServiceHandle` | `0xCC20` | 143 | UnwindData |  |
| 1191 | `OpenSCManagerW` | `0xD260` | 971 | UnwindData |  |
| 1216 | `QueryUserServiceName` | `0xD820` | 399 | UnwindData |  |
| 1231 | `SetServiceStatus` | `0xE7A0` | 404 | UnwindData |  |
| 1037 | `ConvertSidToStringSidW` | `0xEAC0` | 319 | UnwindData |  |
| 1036 | `ConvertSecurityDescriptorToStringSecurityDescriptorW` | `0xED80` | 214 | UnwindData |  |
| 1042 | `ConvertStringSidToSidW` | `0x132D0` | 173 | UnwindData |  |
| 1146 | `LocalGetSidForString` | `0x13A90` | 336 | UnwindData |  |
| 1144 | `LocalGetConditionForString` | `0x13BF0` | 2,376 | UnwindData |  |
| 1115 | `GetOperandValue` | `0x14540` | 1,700 | UnwindData |  |
| 1143 | `IsValueSizeFixed` | `0x15060` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `FreeOperandValue` | `0x150B0` | 61 | UnwindData |  |
| 1101 | `EnumerateTraceGuidsEx` | `0x162F0` | 944 | UnwindData |  |
| 1169 | `LsaLookupGetDomainInfo` | `0x168C0` | 146 | UnwindData |  |
| 1175 | `LsaLookupTranslateNames` | `0x16960` | 82 | UnwindData |  |
| 1152 | `LookupAccountNameLocalW` | `0x169C0` | 43 | UnwindData |  |
| 1176 | `LsaLookupTranslateSids` | `0x16F60` | 50 | UnwindData |  |
| 1153 | `LookupAccountSidLocalA` | `0x17110` | 570 | UnwindData |  |
| 1154 | `LookupAccountSidLocalW` | `0x17350` | 43 | UnwindData |  |
| 1172 | `LsaLookupOpenLocalPolicy` | `0x17890` | 143 | UnwindData |  |
| 1167 | `LsaLookupClose` | `0x17930` | 136 | UnwindData |  |
| 1099 | `EnumServicesStatusExW` | `0x17FF0` | 646 | UnwindData |  |
| 1207 | `QueryServiceConfig2W` | `0x18280` | 1,288 | UnwindData |  |
| 1041 | `ConvertStringSecurityDescriptorToSecurityDescriptorW` | `0x197A0` | 90 | UnwindData |  |
| 1076 | `CredReadW` | `0x1A0B0` | 240 | UnwindData |  |
| 1067 | `CredProfileLoadedEx` | `0x1A1B0` | 98 | UnwindData |  |
| 1086 | `CredWriteW` | `0x1A220` | 140 | UnwindData |  |
| 1053 | `CredEnumerateW` | `0x1A2F0` | 319 | UnwindData |  |
| 1088 | `CredpConvertOneCredentialSize` | `0x1A6A0` | 437 | UnwindData |  |
| 1087 | `CredpConvertCredential` | `0x1B080` | 189 | UnwindData |  |
| 1148 | `LocalGetStringForRelativeAttribute` | `0x1BA60` | 2,201 | UnwindData |  |
| 1117 | `GetOperatorIndexByToken` | `0x1C380` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1119 | `GetPrintableOperandValue` | `0x1C480` | 1,544 | UnwindData |  |
| 1209 | `QueryServiceConfigW` | `0x1CA90` | 358 | UnwindData |  |
| 1127 | `I_QueryTagInformation` | `0x1CC20` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1245 | `WaitServiceState` | `0x1CEF0` | 599 | UnwindData |  |
| 1240 | `SubscribeServiceChangeNotifications` | `0x1D150` | 65 | UnwindData |  |
| 1132 | `I_ScQueryServiceConfig` | `0x1D290` | 182 | UnwindData |  |
| 1193 | `OpenServiceW` | `0x1D350` | 118 | UnwindData |  |
| 1213 | `QueryServiceStatusEx` | `0x1D690` | 157 | UnwindData |  |
| 1113 | `GetIdentityProviderInfoByGUID` | `0x1DD30` | 183 | UnwindData |  |
| 1100 | `EnumerateIdentityProviders` | `0x1DE60` | 227 | UnwindData |  |
| 1030 | `ControlService` | `0x1E2D0` | 102 | UnwindData |  |
| 1215 | `QueryTransientObjectSecurityDescriptor` | `0x1E340` | 414 | UnwindData |  |
| 1107 | `FreeTransientObjectSecurityDescriptor` | `0x1EA40` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1242 | `TraceQueryInformation` | `0x1EC20` | 1,614 | UnwindData |  |
| 1022 | `CapabilityCheck` | `0x1F3F0` | 429 | UnwindData |  |
| 1162 | `LsaICLookupNames` | `0x1F5B0` | 2,091 | UnwindData |  |
| 1212 | `QueryServiceStatus` | `0x20240` | 97 | UnwindData |  |
| 1244 | `UnsubscribeServiceChangeNotifications` | `0x203E0` | 45 | UnwindData |  |
| 1161 | `LsaFreeMemory` | `0x20420` | 24 | UnwindData |  |
| 1168 | `LsaLookupFreeMemory` | `0x20420` | 24 | UnwindData |  |
| 1178 | `LsaOpenPolicy` | `0x21160` | 555 | UnwindData |  |
| 1112 | `GetEmbeddedImageMitigationPolicy` | `0x216B0` | 344 | UnwindData |  |
| 1062 | `CredIsProtectedW` | `0x21AB0` | 208 | UnwindData |  |
| 1079 | `CredUnmarshalCredentialW` | `0x21B90` | 665 | UnwindData |  |
| 1236 | `StartServiceW` | `0x21E30` | 102 | UnwindData |  |
| 1156 | `LsaClose` | `0x21EA0` | 109 | UnwindData |  |
| 1199 | `ProcessTrace` | `0x220F0` | 1,170 | UnwindData |  |
| 1133 | `I_ScRegisterDeviceNotification` | `0x22610` | 937 | UnwindData |  |
| 1141 | `I_ScValidatePnPService` | `0x22B50` | 279 | UnwindData |  |
| 1177 | `LsaLookupUserAccountType` | `0x23050` | 196 | UnwindData |  |
| 1223 | `ReleaseIdentityProviderEnumContext` | `0x23120` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `ControlServiceExW` | `0x23480` | 330 | UnwindData |  |
| 1180 | `LsaQueryInformationPolicy` | `0x235D0` | 355 | UnwindData |  |
| 1140 | `I_ScUnregisterDeviceNotification` | `0x23C70` | 165 | UnwindData |  |
| 1029 | `CloseTrace` | `0x240E0` | 309 | UnwindData |  |
| 1122 | `GetServiceKeyNameW` | `0x24370` | 197 | UnwindData |  |
| 1198 | `OpenTraceW` | `0x24880` | 954 | UnwindData |  |
| 1192 | `OpenServiceA` | `0x250C0` | 116 | UnwindData |  |
| 1114 | `GetIdentityProviderInfoByName` | `0x25140` | 227 | UnwindData |  |
| 1187 | `NotifyServiceStatusChange` | `0x256A0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1189 | `NotifyServiceStatusChangeW` | `0x256A0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1124 | `GetServiceRegistryStateKey` | `0x25850` | 102 | UnwindData |  |
| 1188 | `NotifyServiceStatusChangeA` | `0x25940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `LsaLookupSids` | `0x25960` | 38 | UnwindData |  |
| 1020 | `BuildSecurityDescriptorForSharingAccess` | `0x25B50` | 23 | UnwindData |  |
| 1021 | `BuildSecurityDescriptorForSharingAccessEx` | `0x25B70` | 874 | UnwindData |  |
| 1104 | `EventAccessRemove` | `0x25F10` | 782 | UnwindData |  |
| 1131 | `I_ScPnPGetServiceName` | `0x26230` | 73 | UnwindData |  |
| 1164 | `LsaICLookupSids` | `0x26280` | 1,113 | UnwindData |  |
| 1009 | `AuditFree` | `0x266E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `CredFree` | `0x266E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `I_RegisterSvchostNotificationCallback` | `0x26720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `RpcClientCapabilityCheck` | `0x26740` | 283 | UnwindData |  |
| 1090 | `CredpDecodeCredential` | `0x269B0` | 69 | UnwindData |  |
| 1170 | `LsaLookupManageSidNameMapping` | `0x26A00` | 247 | UnwindData |  |
| 1151 | `LookupAccountNameLocalA` | `0x26F00` | 369 | UnwindData |  |
| 1220 | `RegisterServiceCtrlHandlerExW` | `0x27460` | 6,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1147 | `LocalGetStringForCondition` | `0x28E80` | 54 | UnwindData |  |
| 1109 | `GetDefaultIdentityProvider` | `0x2C790` | 94 | UnwindData |  |
| 1035 | `ConvertSDToStringSDRootDomainW` | `0x2F0F0` | 115 | UnwindData |  |
| 1038 | `ConvertStringSDToSDDomainA` | `0x2F170` | 316 | UnwindData |  |
| 1039 | `ConvertStringSDToSDDomainW` | `0x2F2C0` | 198 | UnwindData |  |
| 1040 | `ConvertStringSDToSDRootDomainW` | `0x2F390` | 105 | UnwindData |  |
| 1093 | `DecodeAttributeName` | `0x2F9A0` | 509 | UnwindData |  |
| 1097 | `EncodeAttributeName` | `0x2FBB0` | 310 | UnwindData |  |
| 1108 | `GetCharFromDigit` | `0x2FD50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1110 | `GetDigitFromChar` | `0x2FD70` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1116 | `GetOperatorCodeAtIndex` | `0x2FE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1118 | `GetOperatorUnaryAtIndex` | `0x2FEA0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1142 | `IsArrayType` | `0x30000` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `LocalGetReferencedTokenTypesForCondition` | `0x300D0` | 77 | UnwindData |  |
| 1023 | `CapabilityCheckForSingleSessionSku` | `0x47D40` | 102 | UnwindData |  |
| 1149 | `LocalRpcBindingCreateWithSecurity` | `0x47F90` | 419 | UnwindData |  |
| 1150 | `LocalRpcBindingSetAuthInfoEx` | `0x48140` | 259 | UnwindData |  |
| 1228 | `SetLocalRpcServerInterfaceSecurity` | `0x48250` | 218 | UnwindData |  |
| 1229 | `SetLocalRpcServerProtseqSecurity` | `0x48330` | 117 | UnwindData |  |
| 1003 | `I_ScSetServiceBitsA` | `0x484A0` | 29 | UnwindData |  |
| 1004 | `I_ScSetServiceBitsW` | `0x484D0` | 139 | UnwindData |  |
| 1024 | `ChangeServiceConfig2A` | `0x48860` | 440 | UnwindData |  |
| 1025 | `ChangeServiceConfig2W` | `0x48A20` | 191 | UnwindData |  |
| 1026 | `ChangeServiceConfigA` | `0x48AF0` | 701 | UnwindData |  |
| 1027 | `ChangeServiceConfigW` | `0x48DC0` | 399 | UnwindData |  |
| 1031 | `ControlServiceExA` | `0x48F60` | 323 | UnwindData |  |
| 1045 | `CreateServiceA` | `0x490B0` | 1,740 | UnwindData |  |
| 1046 | `CreateServiceEx` | `0x49790` | 976 | UnwindData |  |
| 1047 | `CreateServiceW` | `0x49B70` | 950 | UnwindData |  |
| 1095 | `DeleteService` | `0x49F30` | 94 | UnwindData |  |
| 1098 | `EnumDependentServicesW` | `0x49FA0` | 425 | UnwindData |  |
| 1120 | `GetServiceDirectory` | `0x4A150` | 113 | UnwindData |  |
| 1121 | `GetServiceDisplayNameW` | `0x4A1D0` | 197 | UnwindData |  |
| 1123 | `GetServiceProcessToken` | `0x4A2A0` | 97 | UnwindData |  |
| 1125 | `GetSharedServiceDirectory` | `0x4A310` | 120 | UnwindData |  |
| 1126 | `GetSharedServiceRegistryStateKey` | `0x4A390` | 108 | UnwindData |  |
| 1129 | `I_ScBroadcastServiceControlMessage` | `0x4A410` | 201 | UnwindData |  |
| 1139 | `I_ScSendTSMessage` | `0x4A410` | 201 | UnwindData |  |
| 1134 | `I_ScRegisterPreshutdownRestart` | `0x4A4E0` | 168 | UnwindData |  |
| 1135 | `I_ScReparseServiceDatabase` | `0x4A590` | 151 | UnwindData |  |
| 1205 | `QueryLocalUserServiceName` | `0x4A630` | 824 | UnwindData |  |
| 1206 | `QueryServiceConfig2A` | `0x4A970` | 1,152 | UnwindData |  |
| 1208 | `QueryServiceConfigA` | `0x4AE00` | 269 | UnwindData |  |
| 1211 | `QueryServiceObjectSecurity` | `0x4AF20` | 183 | UnwindData |  |
| 1217 | `QueryUserServiceNameForContext` | `0x4AFE0` | 146 | UnwindData |  |
| 1225 | `ReparseServiceConfig` | `0x4B080` | 97 | UnwindData |  |
| 1227 | `ScSendSynchronousPowerMessage` | `0x4B0F0` | 212 | UnwindData |  |
| 1230 | `SetServiceObjectSecurity` | `0x4B1D0` | 323 | UnwindData |  |
| 1233 | `StartServiceA` | `0x4B320` | 102 | UnwindData |  |
| 1130 | `I_ScIsSecurityProcess` | `0x4B770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `QueryServiceDynamicInformation` | `0x4B780` | 144 | UnwindData |  |
| 1218 | `RegisterServiceCtrlHandlerA` | `0x4B820` | 100 | UnwindData |  |
| 1219 | `RegisterServiceCtrlHandlerExA` | `0x4B890` | 115 | UnwindData |  |
| 1221 | `RegisterServiceCtrlHandlerW` | `0x4B910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `StartServiceCtrlDispatcherA` | `0x4B930` | 309 | UnwindData |  |
| 1136 | `I_ScRpcBindA` | `0x4C510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `I_ScRpcBindW` | `0x4C520` | 31 | UnwindData |  |
| 1000 | *Ordinal Only* | `0x4F550` | 112 | UnwindData |  |
| 1194 | `OpenTraceFromBufferStream` | `0x4F5D0` | 428 | UnwindData |  |
| 1195 | `OpenTraceFromFile` | `0x4F790` | 498 | UnwindData |  |
| 1196 | `OpenTraceFromRealTimeLogger` | `0x4F990` | 26 | UnwindData |  |
| 1197 | `OpenTraceFromRealTimeLoggerWithAllocationOptions` | `0x4F9B0` | 744 | UnwindData |  |
| 1200 | `ProcessTraceAddBufferToBufferStream` | `0x4FCA0` | 290 | UnwindData |  |
| 1201 | `ProcessTraceBufferDecrementReference` | `0x4FDD0` | 253 | UnwindData |  |
| 1202 | `ProcessTraceBufferIncrementReference` | `0x4FEE0` | 165 | UnwindData |  |
| 1214 | `QueryTraceProcessingHandle` | `0x4FF90` | 898 | UnwindData |  |
| 1224 | `RemoveTraceCallback` | `0x50320` | 434 | UnwindData |  |
| 1232 | `SetTraceCallback` | `0x504E0` | 546 | UnwindData |  |
| 1001 | *Ordinal Only* | `0x50710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | *Ordinal Only* | `0x50720` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1102 | `EventAccessControl` | `0x50B50` | 506 | UnwindData |  |
| 1103 | `EventAccessQuery` | `0x50D50` | 798 | UnwindData |  |
| 1203 | `QueryAllTracesA` | `0x51080` | 149 | UnwindData |  |
| 1237 | `StartTraceA` | `0x51120` | 1,753 | UnwindData |  |
| 1239 | `StopTraceW` | `0x51800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1241 | `TraceConfigureLastBranchRecord` | `0x51820` | 400 | UnwindData |  |
| 1243 | `TraceSetInformation` | `0x519C0` | 3,090 | UnwindData |  |
| 1155 | `LsaAddAccountRights` | `0x59320` | 134 | UnwindData |  |
| 1159 | `LsaEnumerateAccountRights` | `0x593B0` | 199 | UnwindData |  |
| 1160 | `LsaEnumerateAccountsWithUserRight` | `0x59480` | 187 | UnwindData |  |
| 1182 | `LsaRemoveAccountRights` | `0x59550` | 148 | UnwindData |  |
| 1158 | `LsaDelete` | `0x595F0` | 120 | UnwindData |  |
| 1163 | `LsaICLookupNamesWithCreds` | `0x59670` | 464 | UnwindData |  |
| 1165 | `LsaICLookupSidsWithCreds` | `0x59850` | 549 | UnwindData |  |
| 1166 | `LsaIOpenPolicyWithCreds` | `0x59BB0` | 233 | UnwindData |  |
| 1171 | `LsaLookupNames2` | `0x59CA0` | 100 | UnwindData |  |
| 1174 | `LsaLookupSids2` | `0x59D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1184 | `LsaSetInformationPolicy` | `0x59D20` | 287 | UnwindData |  |
| 1157 | `LsaCreateSecret` | `0x5A020` | 382 | UnwindData |  |
| 1179 | `LsaOpenSecret` | `0x5A1B0` | 381 | UnwindData |  |
| 1181 | `LsaQuerySecret` | `0x5A340` | 164 | UnwindData |  |
| 1183 | `LsaRetrievePrivateData` | `0x5A780` | 260 | UnwindData |  |
| 1185 | `LsaSetSecret` | `0x5AB10` | 118 | UnwindData |  |
| 1186 | `LsaStorePrivateData` | `0x5AD40` | 165 | UnwindData |  |
| 1005 | `AuditComputeEffectivePolicyBySid` | `0x5C000` | 397 | UnwindData |  |
| 1006 | `AuditEnumerateCategories` | `0x5C1A0` | 298 | UnwindData |  |
| 1007 | `AuditEnumeratePerUserPolicy` | `0x5C2D0` | 103 | UnwindData |  |
| 1008 | `AuditEnumerateSubCategories` | `0x5C340` | 329 | UnwindData |  |
| 1010 | `AuditLookupCategoryNameW` | `0x5C490` | 336 | UnwindData |  |
| 1011 | `AuditLookupSubCategoryNameW` | `0x5C5F0` | 336 | UnwindData |  |
| 1012 | `AuditQueryGlobalSaclW` | `0x5C750` | 94 | UnwindData |  |
| 1013 | `AuditQueryPerUserPolicy` | `0x5C7C0` | 100 | UnwindData |  |
| 1014 | `AuditQuerySecurity` | `0x5C830` | 178 | UnwindData |  |
| 1015 | `AuditQuerySystemPolicy` | `0x5C8F0` | 93 | UnwindData |  |
| 1016 | `AuditSetGlobalSaclW` | `0x5C960` | 94 | UnwindData |  |
| 1017 | `AuditSetPerUserPolicy` | `0x5C9D0` | 86 | UnwindData |  |
| 1018 | `AuditSetSecurity` | `0x5CA30` | 300 | UnwindData |  |
| 1019 | `AuditSetSystemPolicy` | `0x5CB70` | 73 | UnwindData |  |
| 1048 | `CredBackupCredentials` | `0x5CE00` | 374 | UnwindData |  |
| 1049 | `CredDeleteA` | `0x5CF80` | 154 | UnwindData |  |
| 1050 | `CredDeleteW` | `0x5D020` | 154 | UnwindData |  |
| 1052 | `CredEnumerateA` | `0x5D0C0` | 266 | UnwindData |  |
| 1054 | `CredFindBestCredentialA` | `0x5D1D0` | 239 | UnwindData |  |
| 1055 | `CredFindBestCredentialW` | `0x5D2D0` | 240 | UnwindData |  |
| 1057 | `CredGetSessionTypes` | `0x5D3D0` | 103 | UnwindData |  |
| 1058 | `CredGetTargetInfoA` | `0x5D440` | 217 | UnwindData |  |
| 1059 | `CredGetTargetInfoW` | `0x5D520` | 217 | UnwindData |  |
| 1066 | `CredProfileLoaded` | `0x5D600` | 94 | UnwindData |  |
| 1068 | `CredProfileUnloaded` | `0x5D670` | 94 | UnwindData |  |
| 1072 | `CredReadA` | `0x5D6E0` | 239 | UnwindData |  |
| 1073 | `CredReadByTokenHandle` | `0x5D7E0` | 300 | UnwindData |  |
| 1074 | `CredReadDomainCredentialsA` | `0x5D920` | 266 | UnwindData |  |
| 1075 | `CredReadDomainCredentialsW` | `0x5DA30` | 278 | UnwindData |  |
| 1077 | `CredRestoreCredentials` | `0x5DB50` | 339 | UnwindData |  |
| 1083 | `CredWriteA` | `0x5DCB0` | 140 | UnwindData |  |
| 1084 | `CredWriteDomainCredentialsA` | `0x5DD50` | 207 | UnwindData |  |
| 1085 | `CredWriteDomainCredentialsW` | `0x5DE30` | 205 | UnwindData |  |
| 1051 | `CredEncryptAndMarshalBinaryBlob` | `0x5DF10` | 40 | UnwindData |  |
| 1060 | `CredIsMarshaledCredentialW` | `0x5DF40` | 61 | UnwindData |  |
| 1061 | `CredIsProtectedA` | `0x5DF90` | 141 | UnwindData |  |
| 1063 | `CredMarshalCredentialA` | `0x5E030` | 106 | UnwindData |  |
| 1064 | `CredMarshalCredentialW` | `0x5E0A0` | 477 | UnwindData |  |
| 1069 | `CredProtectA` | `0x5E290` | 372 | UnwindData |  |
| 1070 | `CredProtectEx` | `0x5E410` | 380 | UnwindData |  |
| 1071 | `CredProtectW` | `0x5E5A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `CredUnmarshalCredentialA` | `0x5E5C0` | 159 | UnwindData |  |
| 1080 | `CredUnprotectA` | `0x5E670` | 398 | UnwindData |  |
| 1081 | `CredUnprotectEx` | `0x5E810` | 304 | UnwindData |  |
| 1082 | `CredUnprotectW` | `0x5E950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `CredpConvertTargetInfo` | `0x5E970` | 592 | UnwindData |  |
| 1091 | `CredpEncodeCredential` | `0x5EEE0` | 127 | UnwindData |  |
| 1092 | `CredpEncodeSecret` | `0x5EF70` | 44 | UnwindData |  |
| 1065 | `CredParseUserNameWithType` | `0x5F9A0` | 410 | UnwindData |  |
| 1105 | `FreeContainer` | `0x60450` | 69 | UnwindData |  |
| 1111 | `GetEmbeddedContainerIsolationPolicy` | `0x604A0` | 324 | UnwindData |  |
| 1043 | `CreateIsolatedProcess` | `0x69C00` | 157 | UnwindData |  |
| 1044 | `CreateIsolationContainer` | `0x69CB0` | 114 | UnwindData |  |
| 1094 | `DeleteIsolationContainer` | `0x69D30` | 494 | UnwindData |  |
