# Binary Specification: crypt32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\crypt32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0f549c9c035ec2dfd39a2dcf6fd8f13dab8515ac748759b3583dcdb155ffe011`
* **Total Exported Functions:** 307

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1209 | `CryptProtectMemory` | `0x0` | - | Forwarded | Forwarded to: `DPAPI.CryptProtectMemory` |
| 1239 | `CryptUnprotectMemory` | `0x0` | - | Forwarded | Forwarded to: `DPAPI.CryptUnprotectMemory` |
| 1243 | `CryptUpdateProtectedState` | `0x0` | - | Forwarded | Forwarded to: `DPAPI.CryptUpdateProtectedState` |
| 1256 | `I_CertProtectFunction` | `0x3680` | 188 | UnwindData |  |
| 1082 | `CertFreeCertificateChainEngine` | `0x5C60` | 38 | UnwindData |  |
| 1043 | `CertControlStore` | `0x64C0` | 465 | UnwindData |  |
| 1257 | `I_CertSrvProtectFunction` | `0x69F0` | 516 | UnwindData |  |
| 1058 | `CertDuplicateStore` | `0x7410` | 7,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1254 | `I_CertFinishSslHandshake` | `0x9220` | 444 | UnwindData |  |
| 1255 | `I_CertProcessSslHandshake` | `0x93F0` | 1,125 | UnwindData |  |
| 1294 | `I_CryptTouchLruEntry` | `0x9D50` | 109 | UnwindData |  |
| 1089 | `CertGetCertificateChain` | `0xA8B0` | 1,282 | UnwindData |  |
| 1099 | `CertGetSubjectCertificateFromStore` | `0xB0D0` | 105 | UnwindData |  |
| 1251 | `CryptVerifyTimeStampSignature` | `0xB140` | 84 | UnwindData |  |
| 1191 | `CryptMemFree` | `0xB710` | 13 | UnwindData |  |
| 1275 | `I_CryptFreeLruCache` | `0xC0F0` | 37 | UnwindData |  |
| 1194 | `CryptMsgClose` | `0xC220` | 910 | UnwindData |  |
| 1079 | `CertFreeCRLContext` | `0xCED0` | 33 | UnwindData |  |
| 1080 | `CertFreeCTLContext` | `0xCED0` | 33 | UnwindData |  |
| 1084 | `CertFreeCertificateContext` | `0xCED0` | 33 | UnwindData |  |
| 1104 | `CertIsWeakHash` | `0xCF00` | 683 | UnwindData |  |
| 1265 | `I_CryptCreateLruCache` | `0xE3C0` | 264 | UnwindData |  |
| 1291 | `I_CryptReleaseLruEntry` | `0xF220` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1278 | `I_CryptGetAsn1Encoder` | `0x10120` | 244 | UnwindData |  |
| 1201 | `CryptMsgGetParam` | `0x10940` | 5,740 | UnwindData |  |
| 1277 | `I_CryptGetAsn1Decoder` | `0x125A0` | 174 | UnwindData |  |
| 1205 | `CryptMsgUpdate` | `0x128B0` | 1,541 | UnwindData |  |
| 1202 | `CryptMsgOpenToDecode` | `0x12EC0` | 316 | UnwindData |  |
| 1178 | `CryptHashCertificate2` | `0x13FF0` | 1,164 | UnwindData |  |
| 1054 | `CertDuplicateCRLContext` | `0x14920` | 20,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `CertDuplicateCertificateContext` | `0x14920` | 20,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `CryptMsgControl` | `0x19840` | 504 | UnwindData |  |
| 1049 | `CertCreateContext` | `0x19A40` | 637 | UnwindData |  |
| 1232 | `CryptSignCertificate` | `0x226F0` | 737 | UnwindData |  |
| 1177 | `CryptHashCertificate` | `0x229E0` | 594 | UnwindData |  |
| 1230 | `CryptSignAndEncodeCertificate` | `0x22C40` | 430 | UnwindData |  |
| 1245 | `CryptVerifyCertificateSignatureEx` | `0x22E00` | 1,533 | UnwindData |  |
| 1154 | `CryptEncodeObject` | `0x23930` | 39 | UnwindData |  |
| 1155 | `CryptEncodeObjectEx` | `0x23960` | 685 | UnwindData |  |
| 1132 | `CertStrToNameW` | `0x24470` | 2,379 | UnwindData |  |
| 1180 | `CryptHashPublicKeyInfo` | `0x25170` | 206 | UnwindData |  |
| 1130 | `CertSetStoreProperty` | `0x2AA20` | 119 | UnwindData |  |
| 1172 | `CryptGetKeyIdentifierProperty` | `0x2AC60` | 273 | UnwindData |  |
| 1228 | `CryptSetKeyIdentifierProperty` | `0x2B180` | 480 | UnwindData |  |
| 1051 | `CertDeleteCRLFromStore` | `0x2C590` | 17,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `CertDeleteCTLFromStore` | `0x2C590` | 17,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1053 | `CertDeleteCertificateFromStore` | `0x2C590` | 17,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `I_CryptReadTrustedPublisherDWORDValueFromRegistry` | `0x30990` | 496 | UnwindData |  |
| 1286 | `I_CryptInsertLruEntry` | `0x344D0` | 214 | UnwindData |  |
| 1266 | `I_CryptCreateLruEntry` | `0x34670` | 298 | UnwindData |  |
| 1069 | `CertFindAttribute` | `0x34900` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `CertAddCertificateLinkToStore` | `0x34D50` | 95 | UnwindData |  |
| 1055 | `CertDuplicateCTLContext` | `0x35620` | 30 | UnwindData |  |
| 1072 | `CertFindCertificateInCRL` | `0x35F00` | 362 | UnwindData |  |
| 1077 | `CertFindSubjectInCTL` | `0x361B0` | 551 | UnwindData |  |
| 1066 | `CertEnumSubjectInSortedCTL` | `0x36470` | 372 | UnwindData |  |
| 1078 | `CertFindSubjectInSortedCTL` | `0x36740` | 679 | UnwindData |  |
| 1107 | `CertOIDToAlgId` | `0x36F50` | 72 | UnwindData |  |
| 1127 | `CertSetCertificateContextPropertiesFromCTLEntry` | `0x3A780` | 596 | UnwindData |  |
| 1293 | `I_CryptSetTls` | `0x3B9D0` | 202 | UnwindData |  |
| 1125 | `CertSetCRLContextProperty` | `0x3BD50` | 33 | UnwindData |  |
| 1126 | `CertSetCTLContextProperty` | `0x3BD50` | 33 | UnwindData |  |
| 1128 | `CertSetCertificateContextProperty` | `0x3BD50` | 33 | UnwindData |  |
| 1253 | `I_CertDiagControl` | `0x3BD80` | 1,613 | UnwindData |  |
| 1139 | `CertVerifyRevocation` | `0x3E9B0` | 470 | UnwindData |  |
| 1138 | `CertVerifyCertificateChainPolicy` | `0x3FF60` | 828 | UnwindData |  |
| 1274 | `I_CryptFlushLruCache` | `0x43070` | 288 | UnwindData |  |
| 1028 | `CertAddEncodedCertificateToStore` | `0x43470` | 108 | UnwindData |  |
| 1158 | `CryptEnumOIDFunction` | `0x434F0` | 1,688 | UnwindData |  |
| 1095 | `CertGetNameStringW` | `0x441D0` | 2,648 | UnwindData |  |
| 1034 | `CertAddSerializedElementToStore` | `0x45190` | 147 | UnwindData |  |
| 1064 | `CertEnumCertificatesInStore` | `0x45F40` | 80 | UnwindData |  |
| 1090 | `CertGetCertificateContextProperty` | `0x47B20` | 37 | UnwindData |  |
| 1285 | `I_CryptGetTls` | `0x49000` | 221 | UnwindData |  |
| 1106 | `CertNameToStrW` | `0x4C250` | 238 | UnwindData |  |
| 1166 | `CryptFindOIDInfo` | `0x4CEE0` | 115 | UnwindData |  |
| 1150 | `CryptDecodeObject` | `0x4D720` | 52 | UnwindData |  |
| 1151 | `CryptDecodeObjectEx` | `0x4D7E0` | 2,903 | UnwindData |  |
| 1175 | `CryptGetOIDFunctionAddress` | `0x50780` | 63 | UnwindData |  |
| 1096 | `CertGetPublicKeyLength` | `0x50CC0` | 1,566 | UnwindData |  |
| 1279 | `I_CryptGetDefaultCryptProv` | `0x512F0` | 348 | UnwindData |  |
| 1184 | `CryptImportPublicKeyInfoEx` | `0x51460` | 1,691 | UnwindData |  |
| 1168 | `CryptFreeOIDFunctionAddress` | `0x51B10` | 31 | UnwindData |  |
| 1109 | `CertOpenStore` | `0x52210` | 77 | UnwindData |  |
| 1183 | `CryptImportPublicKeyInfo` | `0x53230` | 1,211 | UnwindData |  |
| 1038 | `CertCloseStore` | `0x54410` | 62 | UnwindData |  |
| 1117 | `CertRemoveStoreFromCollection` | `0x57FC0` | 133 | UnwindData |  |
| 1035 | `CertAddStoreToCollection` | `0x58110` | 402 | UnwindData |  |
| 1103 | `CertIsValidCRLForCertificate` | `0x5B570` | 979 | UnwindData |  |
| 1092 | `CertGetIntendedKeyUsage` | `0x5C480` | 447 | UnwindData |  |
| 1075 | `CertFindExtension` | `0x5C650` | 3,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1161 | `CryptExportPublicKeyInfo` | `0x5D590` | 44 | UnwindData |  |
| 1162 | `CryptExportPublicKeyInfoEx` | `0x5DB30` | 217 | UnwindData |  |
| 1042 | `CertComparePublicKeyInfo` | `0x5E270` | 462 | UnwindData |  |
| 1212 | `CryptRegisterOIDFunction` | `0x5EAD0` | 236 | UnwindData |  |
| 1159 | `CryptEnumOIDInfo` | `0x5EE00` | 268 | UnwindData |  |
| 1229 | `CryptSetOIDFunctionValue` | `0x5EF60` | 272 | UnwindData |  |
| 1145 | `CryptBinaryToStringW` | `0x5F080` | 320 | UnwindData |  |
| 1144 | `CryptBinaryToStringA` | `0x5F1D0` | 942 | UnwindData |  |
| 1241 | `CryptUnregisterOIDFunction` | `0x610F0` | 282 | UnwindData |  |
| 1176 | `CryptGetOIDFunctionValue` | `0x61210` | 246 | UnwindData |  |
| 1222 | `CryptSIPRemoveProvider` | `0x61310` | 280 | UnwindData |  |
| 1299 | `I_PFXDecrypt` | `0x61470` | 1,073 | UnwindData |  |
| 1300 | `I_PFXHMAC` | `0x62D90` | 564 | UnwindData |  |
| 1301 | `PFXExportCertStore` | `0x63180` | 335 | UnwindData |  |
| 1303 | `PFXExportCertStoreEx` | `0x632E0` | 541 | UnwindData |  |
| 2000 | *Ordinal Only* | `0x63B20` | 136 | UnwindData |  |
| 1207 | `CryptMsgVerifyCountersignatureEncodedEx` | `0x67200` | 794 | UnwindData |  |
| 1225 | `CryptSIPRetrieveSubjectGuidForCatalogFile` | `0x68B30` | 718 | UnwindData |  |
| 1305 | `PFXIsPFXBlob` | `0x692E0` | 58 | UnwindData |  |
| 1224 | `CryptSIPRetrieveSubjectGuid` | `0x6A380` | 1,237 | UnwindData |  |
| 1226 | `CryptSIPVerifyIndirectData` | `0x6A9D0` | 222 | UnwindData |  |
| 1216 | `CryptSIPCreateIndirectData` | `0x6AAC0` | 214 | UnwindData |  |
| 1217 | `CryptSIPGetCaps` | `0x6AC40` | 222 | UnwindData |  |
| 1220 | `CryptSIPLoad` | `0x6AD30` | 239 | UnwindData |  |
| 1219 | `CryptSIPGetSignedDataMsg` | `0x6AE30` | 232 | UnwindData |  |
| 1210 | `CryptQueryObject` | `0x6B160` | 1,947 | UnwindData |  |
| 1236 | `CryptStringToBinaryW` | `0x6BA30` | 117 | UnwindData |  |
| 1235 | `CryptStringToBinaryA` | `0x6C1C0` | 68 | UnwindData |  |
| 1171 | `CryptGetDefaultOIDFunctionAddress` | `0x6D620` | 271 | UnwindData |  |
| 1188 | `CryptInstallOIDFunctionAddress` | `0x6DF70` | 95 | UnwindData |  |
| 1186 | `CryptInitOIDFunctionSet` | `0x6DFE0` | 215 | UnwindData |  |
| 1287 | `I_CryptInstallAsn1Module` | `0x6E990` | 105 | UnwindData |  |
| 1264 | `I_CryptAllocTlsEx` | `0x6F690` | 237 | UnwindData |  |
| 1267 | `I_CryptDetachTls` | `0x6F7A0` | 120 | UnwindData |  |
| 1276 | `I_CryptFreeTls` | `0x703F0` | 415 | UnwindData |  |
| 1156 | `CryptEncryptMessage` | `0x72FE0` | 263 | UnwindData |  |
| 1203 | `CryptMsgOpenToEncode` | `0x733C0` | 260 | UnwindData |  |
| 1193 | `CryptMsgCalculateEncodedLength` | `0x73DD0` | 350 | UnwindData |  |
| 1233 | `CryptSignMessage` | `0x74110` | 271 | UnwindData |  |
| 1153 | `CryptDecryptMessage` | `0x757C0` | 104 | UnwindData |  |
| 1249 | `CryptVerifyMessageSignature` | `0x75830` | 110 | UnwindData |  |
| 1073 | `CertFindCertificateInStore` | `0x76400` | 142 | UnwindData |  |
| 1098 | `CertGetStoreProperty` | `0x76AE0` | 200 | UnwindData |  |
| 1143 | `CryptAcquireCertificatePrivateKey` | `0x76D40` | 1,051 | UnwindData |  |
| 1113 | `CertRDNValueToStrW` | `0x80380` | 268 | UnwindData |  |
| 1020 | `CertAddCRLContextToStore` | `0x84730` | 127 | UnwindData |  |
| 1022 | `CertAddCTLContextToStore` | `0x84730` | 127 | UnwindData |  |
| 1024 | `CertAddCertificateContextToStore` | `0x84730` | 127 | UnwindData |  |
| 1258 | `I_CertSyncStore` | `0x84910` | 21 | UnwindData |  |
| 1200 | `CryptMsgGetAndVerifySigner` | `0x871F0` | 303 | UnwindData |  |
| 1100 | `CertGetValidUsages` | `0x87BA0` | 2,012 | UnwindData |  |
| 1091 | `CertGetEnhancedKeyUsage` | `0x885C0` | 1,037 | UnwindData |  |
| 1271 | `I_CryptFindLruEntry` | `0x8AE00` | 180 | UnwindData |  |
| 1121 | `CertSelectCertificateChains` | `0x8C7E0` | 189 | UnwindData |  |
| 1039 | `CertCompareCertificate` | `0x8D4E0` | 269 | UnwindData |  |
| 1140 | `CertVerifySubjectCertificateContext` | `0x8DA40` | 61 | UnwindData |  |
| 1093 | `CertGetIssuerCertificateFromStore` | `0x8DA90` | 266 | UnwindData |  |
| 1040 | `CertCompareCertificateName` | `0x8DBA0` | 52 | UnwindData |  |
| 1141 | `CertVerifyTimeValidity` | `0x8DD90` | 189 | UnwindData |  |
| 1087 | `CertGetCRLFromStore` | `0x8DF60` | 282 | UnwindData |  |
| 1270 | `I_CryptEnumMatchingLruEntries` | `0x8F680` | 4,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1181 | `CryptHashToBeSigned` | `0x90700` | 537 | UnwindData |  |
| 1114 | `CertRegisterPhysicalStore` | `0x95E80` | 670 | UnwindData |  |
| 1067 | `CertEnumSystemStore` | `0x96490` | 1,249 | UnwindData |  |
| 1133 | `CertUnregisterPhysicalStore` | `0x96B00` | 267 | UnwindData |  |
| 1238 | `CryptUnprotectData` | `0x96CB0` | 1,190 | UnwindData |  |
| 1041 | `CertCompareIntegerBlob` | `0x97F00` | 179 | UnwindData |  |
| 1170 | `CryptGetDefaultOIDDllList` | `0x9A310` | 181 | UnwindData |  |
| 1190 | `CryptMemAlloc` | `0x9AA50` | 60 | UnwindData |  |
| 1252 | `I_CertChainEngineIsDisallowedCertificate` | `0x9B150` | 564 | UnwindData |  |
| 1062 | `CertEnumCTLsInStore` | `0x9BA50` | 83 | UnwindData |  |
| 1048 | `CertCreateCertificateContext` | `0x9C1A0` | 73 | UnwindData |  |
| 1001 | *Ordinal Only* | `0x9C1F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1120 | `CertSaveStore` | `0x9C230` | 224 | UnwindData |  |
| 1060 | `CertEnumCRLsInStore` | `0x9C560` | 83 | UnwindData |  |
| 1208 | `CryptProtectData` | `0x9CD00` | 731 | UnwindData |  |
| 1070 | `CertFindCRLInStore` | `0x9D8B0` | 116 | UnwindData |  |
| 1056 | `CertDuplicateCertificateChain` | `0x9DE70` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1105 | `CertNameToStrA` | `0x9DF80` | 145 | UnwindData |  |
| 1094 | `CertGetNameStringA` | `0x9E020` | 183 | UnwindData |  |
| 1298 | `I_CryptWalkAllLruCacheEntries` | `0x9E570` | 120 | UnwindData |  |
| 1185 | `CryptImportPublicKeyInfoEx2` | `0x9F420` | 850 | UnwindData |  |
| 1026 | `CertAddEncodedCRLToStore` | `0xA0120` | 109 | UnwindData |  |
| 1044 | `CertCreateCRLContext` | `0xA0430` | 74 | UnwindData |  |
| 1086 | `CertGetCRLContextProperty` | `0xA0B70` | 33 | UnwindData |  |
| 1088 | `CertGetCTLContextProperty` | `0xA0B70` | 33 | UnwindData |  |
| 1167 | `CryptFormatObject` | `0xA1220` | 293 | UnwindData |  |
| 1045 | `CertCreateCTLContext` | `0xA1350` | 74 | UnwindData |  |
| 1027 | `CertAddEncodedCTLToStore` | `0xA13A0` | 109 | UnwindData |  |
| 1081 | `CertFreeCertificateChain` | `0xA16B0` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `CryptMsgDuplicate` | `0xA2110` | 5,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1282 | `I_CryptGetLruEntryData` | `0xA3730` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1261 | `I_CryptAddRefLruEntry` | `0xA3840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1259 | `I_CertUpdateStore` | `0xA3850` | 216 | UnwindData |  |
| 1263 | `I_CryptAllocTls` | `0xA46D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `CertSerializeCRLStoreElement` | `0xA46E0` | 3,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1123 | `CertSerializeCTLStoreElement` | `0xA46E0` | 3,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1124 | `CertSerializeCertificateStoreElement` | `0xA46E0` | 3,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1272 | `I_CryptFindLruEntryData` | `0xA5500` | 41 | UnwindData |  |
| 1292 | `I_CryptRemoveLruEntry` | `0xA5AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1059 | `CertEnumCRLContextProperties` | `0xA5AE0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `CertEnumCTLContextProperties` | `0xA5AE0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1063 | `CertEnumCertificateContextProperties` | `0xA5AE0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1111 | `CertOpenSystemStoreW` | `0xA5CC0` | 109 | UnwindData |  |
| 1102 | `CertIsStrongHashToSign` | `0xA65D0` | 50 | UnwindData |  |
| 1110 | `CertOpenSystemStoreA` | `0xA6DE0` | 109 | UnwindData |  |
| 1295 | `I_CryptUninstallAsn1Module` | `0xA9470` | 7,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `CertFindChainInStore` | `0xAB0C0` | 277 | UnwindData |  |
| 1108 | `CertOpenServerOcspResponse` | `0xAB570` | 352 | UnwindData |  |
| 1244 | `CryptVerifyCertificateSignature` | `0xABC40` | 66 | UnwindData |  |
| 1165 | `CryptFindLocalizedName` | `0xACED0` | 171 | UnwindData |  |
| 1173 | `CryptGetMessageCertificates` | `0xAD010` | 56 | UnwindData |  |
| 1142 | `CertVerifyValidityNesting` | `0xADBF0` | 95 | UnwindData |  |
| 1047 | `CertCreateCertificateChainEngine` | `0xAE080` | 8,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `PFXImportCertStore` | `0xB0000` | 32 | UnwindData |  |
| 1019 | `I_PFXImportCertStoreEx` | `0xB0030` | 1,602 | UnwindData |  |
| 1129 | `CertSetEnhancedKeyUsage` | `0xB3980` | 119 | UnwindData |  |
| 1068 | `CertEnumSystemStoreLocation` | `0xB3CD0` | 228 | UnwindData |  |
| 1192 | `CryptMemRealloc` | `0xB3E40` | 3,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1101 | `CertIsRDNAttrsInCertificateName` | `0xB4B70` | 529 | UnwindData |  |
| 1083 | `CertFreeCertificateChainList` | `0xB60F0` | 5,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1163 | `CryptExportPublicKeyInfoFromBCryptKeyHandle` | `0xB7720` | 72 | UnwindData |  |
| 1050 | `CertCreateSelfSignCertificate` | `0xB7980` | 2,483 | UnwindData |  |
| 1011 | *Ordinal Only* | `0xC0CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | *Ordinal Only* | `0xC0D10` | 57 | UnwindData |  |
| 1008 | *Ordinal Only* | `0xC0D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | *Ordinal Only* | `0xC0D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | *Ordinal Only* | `0xC0D90` | 57 | UnwindData |  |
| 1009 | *Ordinal Only* | `0xC0DD0` | 36 | UnwindData |  |
| 1010 | *Ordinal Only* | `0xC0E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | *Ordinal Only* | `0xC0E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | *Ordinal Only* | `0xC0E40` | 36 | UnwindData |  |
| 1281 | `I_CryptGetFileVersion` | `0xC12C0` | 228 | UnwindData |  |
| 1002 | *Ordinal Only* | `0xC13C0` | 34,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `CertAddCRLLinkToStore` | `0xC9AD0` | 89 | UnwindData |  |
| 1023 | `CertAddCTLLinkToStore` | `0xC9AD0` | 89 | UnwindData |  |
| 1046 | `CertCreateCTLEntryFromCertificateContextProperties` | `0xC9B30` | 1,263 | UnwindData |  |
| 1071 | `CertFindCTLInStore` | `0xCA030` | 87 | UnwindData |  |
| 1157 | `CryptEnumKeyIdentifierProperties` | `0xCA090` | 217 | UnwindData |  |
| 1029 | `CertAddEncodedCertificateToSystemStoreA` | `0xCA170` | 114 | UnwindData |  |
| 1030 | `CertAddEncodedCertificateToSystemStoreW` | `0xCA1F0` | 114 | UnwindData |  |
| 1031 | `CertAddEnhancedKeyUsageIdentifier` | `0xCA650` | 429 | UnwindData |  |
| 1116 | `CertRemoveEnhancedKeyUsageIdentifier` | `0xCA810` | 254 | UnwindData |  |
| 1032 | `CertAddRefServerOcspResponse` | `0xCBC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1033 | `CertAddRefServerOcspResponseContext` | `0xCBC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `CertCloseServerOcspResponse` | `0xCBC50` | 97 | UnwindData |  |
| 1085 | `CertFreeServerOcspResponseContext` | `0xCBCC0` | 50 | UnwindData |  |
| 1097 | `CertGetServerOcspResponseContext` | `0xCBD00` | 223 | UnwindData |  |
| 1036 | `CertAlgIdToOID` | `0xCC2F0` | 61 | UnwindData |  |
| 1076 | `CertFindRDNAttr` | `0xCC340` | 102 | UnwindData |  |
| 1135 | `CertVerifyCRLRevocation` | `0xCC3B0` | 131 | UnwindData |  |
| 1136 | `CertVerifyCRLTimeValidity` | `0xCC440` | 196 | UnwindData |  |
| 1164 | `CryptFindCertificateKeyProvInfo` | `0xCC510` | 271 | UnwindData |  |
| 1065 | `CertEnumPhysicalStore` | `0xCEB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1115 | `CertRegisterSystemStore` | `0xCEB90` | 250 | UnwindData |  |
| 1134 | `CertUnregisterSystemStore` | `0xCEC90` | 402 | UnwindData |  |
| 1112 | `CertRDNValueToStrA` | `0xCEF70` | 204 | UnwindData |  |
| 1131 | `CertStrToNameA` | `0xCF050` | 393 | UnwindData |  |
| 1148 | `CryptCreateKeyIdentifierFromCSP` | `0xCFA10` | 141 | UnwindData |  |
| 1119 | `CertRetrieveLogoOrBiometricInfo` | `0xD0070` | 1,053 | UnwindData |  |
| 1137 | `CertVerifyCTLUsage` | `0xD08C0` | 270 | UnwindData |  |
| 1146 | `CryptCloseAsyncHandle` | `0xD1220` | 29 | UnwindData |  |
| 1227 | `CryptSetAsyncParam` | `0xD1220` | 29 | UnwindData |  |
| 1290 | `I_CryptRegisterSmartCardStore` | `0xD1220` | 29 | UnwindData |  |
| 1297 | `I_CryptUnregisterSmartCardStore` | `0xD1220` | 29 | UnwindData |  |
| 1147 | `CryptCreateAsyncHandle` | `0xD1250` | 33 | UnwindData |  |
| 1169 | `CryptGetAsyncParam` | `0xD1280` | 47 | UnwindData |  |
| 1149 | `CryptDecodeMessage` | `0xD1850` | 144 | UnwindData |  |
| 1152 | `CryptDecryptAndVerifyMessageSignature` | `0xD18F0` | 540 | UnwindData |  |
| 1174 | `CryptGetMessageSignerCount` | `0xD1B20` | 169 | UnwindData |  |
| 1179 | `CryptHashMessage` | `0xD1BD0` | 624 | UnwindData |  |
| 1231 | `CryptSignAndEncryptMessage` | `0xD1E50` | 338 | UnwindData |  |
| 1234 | `CryptSignMessageWithKey` | `0xD1FB0` | 648 | UnwindData |  |
| 1246 | `CryptVerifyDetachedMessageHash` | `0xD2240` | 76 | UnwindData |  |
| 1247 | `CryptVerifyDetachedMessageSignature` | `0xD22A0` | 116 | UnwindData |  |
| 1248 | `CryptVerifyMessageHash` | `0xD2320` | 71 | UnwindData |  |
| 1250 | `CryptVerifyMessageSignatureWithKey` | `0xD2370` | 442 | UnwindData |  |
| 1211 | `CryptRegisterDefaultOIDFunction` | `0xDB210` | 763 | UnwindData |  |
| 1240 | `CryptUnregisterDefaultOIDFunction` | `0xDB520` | 680 | UnwindData |  |
| 1213 | `CryptRegisterOIDInfo` | `0xDB9E0` | 504 | UnwindData |  |
| 1242 | `CryptUnregisterOIDInfo` | `0xDBBE0` | 73 | UnwindData |  |
| 1187 | `CryptInstallDefaultContext` | `0xE4430` | 519 | UnwindData |  |
| 1237 | `CryptUninstallDefaultContext` | `0xE4640` | 370 | UnwindData |  |
| 1280 | `I_CryptGetDefaultCryptProvForEncrypt` | `0xE47C0` | 379 | UnwindData |  |
| 1260 | `I_CertWnfEnableFlushCache` | `0xE8080` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1262 | `I_CryptAddSmartCardCertToStore` | `0xE80B0` | 269 | UnwindData |  |
| 1273 | `I_CryptFindSmartCardCertInStore` | `0xE81D0` | 554 | UnwindData |  |
| 1284 | `I_CryptGetOssGlobal` | `0xE8400` | 29 | UnwindData |  |
| 1288 | `I_CryptInstallOssGlobal` | `0xE8400` | 29 | UnwindData |  |
| 1296 | `I_CryptUninstallOssGlobal` | `0xE8400` | 29 | UnwindData |  |
| 1118 | `CertResyncCertificateChainEngine` | `0xF9520` | 205 | UnwindData |  |
| 1268 | `I_CryptDisableLruOfEntries` | `0xF9F80` | 30 | UnwindData |  |
| 1269 | `I_CryptEnableLruOfEntries` | `0xF9FB0` | 77 | UnwindData |  |
| 1283 | `I_CryptGetLruEntryIdentifier` | `0xFA010` | 13,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `CryptObjectLocatorFree` | `0xFD660` | 59 | UnwindData |  |
| 1013 | `CryptObjectLocatorGet` | `0xFD6B0` | 56 | UnwindData |  |
| 1014 | `CryptObjectLocatorGetContent` | `0xFD6F0` | 167 | UnwindData |  |
| 1015 | `CryptObjectLocatorGetUpdated` | `0xFD7A0` | 59 | UnwindData |  |
| 1016 | `CryptObjectLocatorInitialize` | `0xFD7F0` | 877 | UnwindData |  |
| 1017 | `CryptObjectLocatorIsChanged` | `0xFDB70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `CryptObjectLocatorRelease` | `0xFDBA0` | 249 | UnwindData |  |
| 1302 | `PFXExportCertStore2` | `0xFEB40` | 26 | UnwindData |  |
| 1306 | `PFXVerifyPassword` | `0xFEB60` | 47 | UnwindData |  |
| 1160 | `CryptExportPKCS8` | `0xFF3E0` | 82 | UnwindData |  |
| 1182 | `CryptImportPKCS8` | `0xFF440` | 1,197 | UnwindData |  |
| 1189 | `CryptLoadSip` | `0x1099F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `CryptSIPAddProvider` | `0x109A00` | 458 | UnwindData |  |
| 1218 | `CryptSIPGetSealedDigest` | `0x109BD0` | 234 | UnwindData |  |
| 1221 | `CryptSIPPutSignedDataMsg` | `0x109CC0` | 232 | UnwindData |  |
| 1223 | `CryptSIPRemoveSignedDataMsg` | `0x109DB0` | 208 | UnwindData |  |
| 1214 | `CryptRetrieveTimeStamp` | `0x109E90` | 844 | UnwindData |  |
| 1196 | `CryptMsgCountersign` | `0x10FFB0` | 381 | UnwindData |  |
| 1197 | `CryptMsgCountersignEncoded` | `0x110140` | 897 | UnwindData |  |
| 1206 | `CryptMsgVerifyCountersignatureEncoded` | `0x1104D0` | 75 | UnwindData |  |
| 1199 | `CryptMsgEncodeAndSignCTL` | `0x110530` | 244 | UnwindData |  |
| 1204 | `CryptMsgSignCTL` | `0x110630` | 233 | UnwindData |  |
