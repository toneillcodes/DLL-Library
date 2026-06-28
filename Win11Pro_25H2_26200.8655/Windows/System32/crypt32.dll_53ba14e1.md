# Binary Specification: crypt32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\crypt32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `53ba14e1c114f8a4a9a558a92840b9ad8dcbb7d3befba745a33c17df42f71320`
* **Total Exported Functions:** 307

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1209 | `CryptProtectMemory` | `0x0` | - | Forwarded | Forwarded to: `DPAPI.CryptProtectMemory` |
| 1239 | `CryptUnprotectMemory` | `0x0` | - | Forwarded | Forwarded to: `DPAPI.CryptUnprotectMemory` |
| 1243 | `CryptUpdateProtectedState` | `0x0` | - | Forwarded | Forwarded to: `DPAPI.CryptUpdateProtectedState` |
| 1256 | `I_CertProtectFunction` | `0x36A0` | 188 | UnwindData |  |
| 1082 | `CertFreeCertificateChainEngine` | `0x5C80` | 38 | UnwindData |  |
| 1043 | `CertControlStore` | `0x64E0` | 465 | UnwindData |  |
| 1257 | `I_CertSrvProtectFunction` | `0x6A10` | 516 | UnwindData |  |
| 1058 | `CertDuplicateStore` | `0x7430` | 7,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1254 | `I_CertFinishSslHandshake` | `0x9240` | 444 | UnwindData |  |
| 1255 | `I_CertProcessSslHandshake` | `0x9410` | 1,125 | UnwindData |  |
| 1294 | `I_CryptTouchLruEntry` | `0x9D70` | 109 | UnwindData |  |
| 1089 | `CertGetCertificateChain` | `0xA8D0` | 1,282 | UnwindData |  |
| 1099 | `CertGetSubjectCertificateFromStore` | `0xB0F0` | 105 | UnwindData |  |
| 1251 | `CryptVerifyTimeStampSignature` | `0xB160` | 84 | UnwindData |  |
| 1191 | `CryptMemFree` | `0xB730` | 13 | UnwindData |  |
| 1275 | `I_CryptFreeLruCache` | `0xC110` | 37 | UnwindData |  |
| 1194 | `CryptMsgClose` | `0xC240` | 910 | UnwindData |  |
| 1079 | `CertFreeCRLContext` | `0xCEF0` | 33 | UnwindData |  |
| 1080 | `CertFreeCTLContext` | `0xCEF0` | 33 | UnwindData |  |
| 1084 | `CertFreeCertificateContext` | `0xCEF0` | 33 | UnwindData |  |
| 1104 | `CertIsWeakHash` | `0xCF20` | 683 | UnwindData |  |
| 1265 | `I_CryptCreateLruCache` | `0xE3E0` | 264 | UnwindData |  |
| 1291 | `I_CryptReleaseLruEntry` | `0xF240` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1278 | `I_CryptGetAsn1Encoder` | `0x10140` | 244 | UnwindData |  |
| 1201 | `CryptMsgGetParam` | `0x10960` | 5,740 | UnwindData |  |
| 1277 | `I_CryptGetAsn1Decoder` | `0x125C0` | 174 | UnwindData |  |
| 1205 | `CryptMsgUpdate` | `0x128D0` | 1,541 | UnwindData |  |
| 1202 | `CryptMsgOpenToDecode` | `0x12EE0` | 316 | UnwindData |  |
| 1178 | `CryptHashCertificate2` | `0x14010` | 1,164 | UnwindData |  |
| 1054 | `CertDuplicateCRLContext` | `0x14940` | 20,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `CertDuplicateCertificateContext` | `0x14940` | 20,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `CryptMsgControl` | `0x19860` | 504 | UnwindData |  |
| 1049 | `CertCreateContext` | `0x19A60` | 637 | UnwindData |  |
| 1232 | `CryptSignCertificate` | `0x22710` | 737 | UnwindData |  |
| 1177 | `CryptHashCertificate` | `0x22A00` | 594 | UnwindData |  |
| 1230 | `CryptSignAndEncodeCertificate` | `0x22C60` | 430 | UnwindData |  |
| 1245 | `CryptVerifyCertificateSignatureEx` | `0x22E20` | 1,533 | UnwindData |  |
| 1154 | `CryptEncodeObject` | `0x23950` | 39 | UnwindData |  |
| 1155 | `CryptEncodeObjectEx` | `0x23980` | 685 | UnwindData |  |
| 1132 | `CertStrToNameW` | `0x24490` | 2,379 | UnwindData |  |
| 1180 | `CryptHashPublicKeyInfo` | `0x25190` | 206 | UnwindData |  |
| 1130 | `CertSetStoreProperty` | `0x2AA40` | 119 | UnwindData |  |
| 1172 | `CryptGetKeyIdentifierProperty` | `0x2AC80` | 273 | UnwindData |  |
| 1228 | `CryptSetKeyIdentifierProperty` | `0x2B1A0` | 480 | UnwindData |  |
| 1051 | `CertDeleteCRLFromStore` | `0x2C5B0` | 17,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `CertDeleteCTLFromStore` | `0x2C5B0` | 17,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1053 | `CertDeleteCertificateFromStore` | `0x2C5B0` | 17,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `I_CryptReadTrustedPublisherDWORDValueFromRegistry` | `0x309B0` | 496 | UnwindData |  |
| 1286 | `I_CryptInsertLruEntry` | `0x344F0` | 214 | UnwindData |  |
| 1266 | `I_CryptCreateLruEntry` | `0x34690` | 298 | UnwindData |  |
| 1069 | `CertFindAttribute` | `0x34920` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `CertAddCertificateLinkToStore` | `0x34D70` | 95 | UnwindData |  |
| 1055 | `CertDuplicateCTLContext` | `0x35640` | 30 | UnwindData |  |
| 1072 | `CertFindCertificateInCRL` | `0x35F20` | 362 | UnwindData |  |
| 1077 | `CertFindSubjectInCTL` | `0x361D0` | 551 | UnwindData |  |
| 1066 | `CertEnumSubjectInSortedCTL` | `0x36490` | 372 | UnwindData |  |
| 1078 | `CertFindSubjectInSortedCTL` | `0x36760` | 679 | UnwindData |  |
| 1107 | `CertOIDToAlgId` | `0x36F70` | 72 | UnwindData |  |
| 1127 | `CertSetCertificateContextPropertiesFromCTLEntry` | `0x3A7A0` | 596 | UnwindData |  |
| 1293 | `I_CryptSetTls` | `0x3B9F0` | 202 | UnwindData |  |
| 1125 | `CertSetCRLContextProperty` | `0x3BD70` | 33 | UnwindData |  |
| 1126 | `CertSetCTLContextProperty` | `0x3BD70` | 33 | UnwindData |  |
| 1128 | `CertSetCertificateContextProperty` | `0x3BD70` | 33 | UnwindData |  |
| 1253 | `I_CertDiagControl` | `0x3BDA0` | 1,613 | UnwindData |  |
| 1139 | `CertVerifyRevocation` | `0x3E9D0` | 470 | UnwindData |  |
| 1138 | `CertVerifyCertificateChainPolicy` | `0x3FF80` | 828 | UnwindData |  |
| 1274 | `I_CryptFlushLruCache` | `0x43090` | 288 | UnwindData |  |
| 1028 | `CertAddEncodedCertificateToStore` | `0x43490` | 108 | UnwindData |  |
| 1158 | `CryptEnumOIDFunction` | `0x43510` | 1,688 | UnwindData |  |
| 1095 | `CertGetNameStringW` | `0x441F0` | 2,648 | UnwindData |  |
| 1034 | `CertAddSerializedElementToStore` | `0x451B0` | 147 | UnwindData |  |
| 1064 | `CertEnumCertificatesInStore` | `0x45F60` | 80 | UnwindData |  |
| 1090 | `CertGetCertificateContextProperty` | `0x47B40` | 37 | UnwindData |  |
| 1285 | `I_CryptGetTls` | `0x49020` | 221 | UnwindData |  |
| 1106 | `CertNameToStrW` | `0x4C270` | 238 | UnwindData |  |
| 1166 | `CryptFindOIDInfo` | `0x4CF00` | 115 | UnwindData |  |
| 1150 | `CryptDecodeObject` | `0x4D740` | 52 | UnwindData |  |
| 1151 | `CryptDecodeObjectEx` | `0x4D800` | 2,903 | UnwindData |  |
| 1175 | `CryptGetOIDFunctionAddress` | `0x507A0` | 63 | UnwindData |  |
| 1096 | `CertGetPublicKeyLength` | `0x50CE0` | 1,566 | UnwindData |  |
| 1279 | `I_CryptGetDefaultCryptProv` | `0x51310` | 348 | UnwindData |  |
| 1184 | `CryptImportPublicKeyInfoEx` | `0x51480` | 1,691 | UnwindData |  |
| 1168 | `CryptFreeOIDFunctionAddress` | `0x51B30` | 31 | UnwindData |  |
| 1109 | `CertOpenStore` | `0x52230` | 77 | UnwindData |  |
| 1183 | `CryptImportPublicKeyInfo` | `0x53250` | 1,211 | UnwindData |  |
| 1038 | `CertCloseStore` | `0x54430` | 62 | UnwindData |  |
| 1117 | `CertRemoveStoreFromCollection` | `0x57FE0` | 133 | UnwindData |  |
| 1035 | `CertAddStoreToCollection` | `0x58130` | 402 | UnwindData |  |
| 1103 | `CertIsValidCRLForCertificate` | `0x5B590` | 979 | UnwindData |  |
| 1092 | `CertGetIntendedKeyUsage` | `0x5C4A0` | 447 | UnwindData |  |
| 1075 | `CertFindExtension` | `0x5C670` | 3,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1161 | `CryptExportPublicKeyInfo` | `0x5D5B0` | 44 | UnwindData |  |
| 1162 | `CryptExportPublicKeyInfoEx` | `0x5DB50` | 217 | UnwindData |  |
| 1042 | `CertComparePublicKeyInfo` | `0x5E290` | 462 | UnwindData |  |
| 1212 | `CryptRegisterOIDFunction` | `0x5EAF0` | 236 | UnwindData |  |
| 1159 | `CryptEnumOIDInfo` | `0x5EE20` | 268 | UnwindData |  |
| 1229 | `CryptSetOIDFunctionValue` | `0x5EF80` | 272 | UnwindData |  |
| 1145 | `CryptBinaryToStringW` | `0x5F0A0` | 320 | UnwindData |  |
| 1144 | `CryptBinaryToStringA` | `0x5F1F0` | 942 | UnwindData |  |
| 1241 | `CryptUnregisterOIDFunction` | `0x61110` | 282 | UnwindData |  |
| 1176 | `CryptGetOIDFunctionValue` | `0x61230` | 246 | UnwindData |  |
| 1222 | `CryptSIPRemoveProvider` | `0x61330` | 280 | UnwindData |  |
| 1299 | `I_PFXDecrypt` | `0x61490` | 1,073 | UnwindData |  |
| 1300 | `I_PFXHMAC` | `0x62DB0` | 564 | UnwindData |  |
| 1301 | `PFXExportCertStore` | `0x631A0` | 335 | UnwindData |  |
| 1303 | `PFXExportCertStoreEx` | `0x63300` | 541 | UnwindData |  |
| 2000 | *Ordinal Only* | `0x63B40` | 136 | UnwindData |  |
| 1207 | `CryptMsgVerifyCountersignatureEncodedEx` | `0x67220` | 794 | UnwindData |  |
| 1225 | `CryptSIPRetrieveSubjectGuidForCatalogFile` | `0x68B50` | 718 | UnwindData |  |
| 1305 | `PFXIsPFXBlob` | `0x69300` | 58 | UnwindData |  |
| 1224 | `CryptSIPRetrieveSubjectGuid` | `0x6A3A0` | 1,237 | UnwindData |  |
| 1226 | `CryptSIPVerifyIndirectData` | `0x6A9F0` | 222 | UnwindData |  |
| 1216 | `CryptSIPCreateIndirectData` | `0x6AAE0` | 214 | UnwindData |  |
| 1217 | `CryptSIPGetCaps` | `0x6AC60` | 222 | UnwindData |  |
| 1220 | `CryptSIPLoad` | `0x6AD50` | 239 | UnwindData |  |
| 1219 | `CryptSIPGetSignedDataMsg` | `0x6AE50` | 232 | UnwindData |  |
| 1210 | `CryptQueryObject` | `0x6B180` | 1,947 | UnwindData |  |
| 1236 | `CryptStringToBinaryW` | `0x6BA50` | 117 | UnwindData |  |
| 1235 | `CryptStringToBinaryA` | `0x6C1E0` | 68 | UnwindData |  |
| 1171 | `CryptGetDefaultOIDFunctionAddress` | `0x6D640` | 271 | UnwindData |  |
| 1188 | `CryptInstallOIDFunctionAddress` | `0x6DF90` | 95 | UnwindData |  |
| 1186 | `CryptInitOIDFunctionSet` | `0x6E000` | 215 | UnwindData |  |
| 1287 | `I_CryptInstallAsn1Module` | `0x6E9B0` | 105 | UnwindData |  |
| 1264 | `I_CryptAllocTlsEx` | `0x6F6B0` | 237 | UnwindData |  |
| 1267 | `I_CryptDetachTls` | `0x6F7C0` | 120 | UnwindData |  |
| 1276 | `I_CryptFreeTls` | `0x70410` | 415 | UnwindData |  |
| 1156 | `CryptEncryptMessage` | `0x73000` | 263 | UnwindData |  |
| 1203 | `CryptMsgOpenToEncode` | `0x733E0` | 260 | UnwindData |  |
| 1193 | `CryptMsgCalculateEncodedLength` | `0x73DF0` | 350 | UnwindData |  |
| 1233 | `CryptSignMessage` | `0x74130` | 271 | UnwindData |  |
| 1153 | `CryptDecryptMessage` | `0x757E0` | 104 | UnwindData |  |
| 1249 | `CryptVerifyMessageSignature` | `0x75850` | 110 | UnwindData |  |
| 1073 | `CertFindCertificateInStore` | `0x76420` | 142 | UnwindData |  |
| 1098 | `CertGetStoreProperty` | `0x76B00` | 200 | UnwindData |  |
| 1143 | `CryptAcquireCertificatePrivateKey` | `0x76D60` | 1,051 | UnwindData |  |
| 1113 | `CertRDNValueToStrW` | `0x803A0` | 268 | UnwindData |  |
| 1020 | `CertAddCRLContextToStore` | `0x84750` | 127 | UnwindData |  |
| 1022 | `CertAddCTLContextToStore` | `0x84750` | 127 | UnwindData |  |
| 1024 | `CertAddCertificateContextToStore` | `0x84750` | 127 | UnwindData |  |
| 1258 | `I_CertSyncStore` | `0x84930` | 21 | UnwindData |  |
| 1200 | `CryptMsgGetAndVerifySigner` | `0x87210` | 303 | UnwindData |  |
| 1100 | `CertGetValidUsages` | `0x87BC0` | 2,012 | UnwindData |  |
| 1091 | `CertGetEnhancedKeyUsage` | `0x885E0` | 1,037 | UnwindData |  |
| 1271 | `I_CryptFindLruEntry` | `0x8AE20` | 180 | UnwindData |  |
| 1121 | `CertSelectCertificateChains` | `0x8C800` | 189 | UnwindData |  |
| 1039 | `CertCompareCertificate` | `0x8D500` | 269 | UnwindData |  |
| 1140 | `CertVerifySubjectCertificateContext` | `0x8DA60` | 61 | UnwindData |  |
| 1093 | `CertGetIssuerCertificateFromStore` | `0x8DAB0` | 266 | UnwindData |  |
| 1040 | `CertCompareCertificateName` | `0x8DBC0` | 52 | UnwindData |  |
| 1141 | `CertVerifyTimeValidity` | `0x8DDB0` | 189 | UnwindData |  |
| 1087 | `CertGetCRLFromStore` | `0x8DF80` | 282 | UnwindData |  |
| 1270 | `I_CryptEnumMatchingLruEntries` | `0x8F6A0` | 4,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1181 | `CryptHashToBeSigned` | `0x90720` | 537 | UnwindData |  |
| 1114 | `CertRegisterPhysicalStore` | `0x95EA0` | 670 | UnwindData |  |
| 1067 | `CertEnumSystemStore` | `0x964B0` | 1,249 | UnwindData |  |
| 1133 | `CertUnregisterPhysicalStore` | `0x96B20` | 267 | UnwindData |  |
| 1238 | `CryptUnprotectData` | `0x96CD0` | 1,190 | UnwindData |  |
| 1041 | `CertCompareIntegerBlob` | `0x97F20` | 179 | UnwindData |  |
| 1170 | `CryptGetDefaultOIDDllList` | `0x9A330` | 181 | UnwindData |  |
| 1190 | `CryptMemAlloc` | `0x9AA70` | 60 | UnwindData |  |
| 1252 | `I_CertChainEngineIsDisallowedCertificate` | `0x9B170` | 564 | UnwindData |  |
| 1062 | `CertEnumCTLsInStore` | `0x9BA70` | 83 | UnwindData |  |
| 1048 | `CertCreateCertificateContext` | `0x9C1C0` | 73 | UnwindData |  |
| 1001 | *Ordinal Only* | `0x9C210` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1120 | `CertSaveStore` | `0x9C250` | 224 | UnwindData |  |
| 1060 | `CertEnumCRLsInStore` | `0x9C580` | 83 | UnwindData |  |
| 1208 | `CryptProtectData` | `0x9CD20` | 731 | UnwindData |  |
| 1070 | `CertFindCRLInStore` | `0x9D8D0` | 116 | UnwindData |  |
| 1056 | `CertDuplicateCertificateChain` | `0x9DE90` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1105 | `CertNameToStrA` | `0x9DFA0` | 145 | UnwindData |  |
| 1094 | `CertGetNameStringA` | `0x9E040` | 183 | UnwindData |  |
| 1298 | `I_CryptWalkAllLruCacheEntries` | `0x9E590` | 120 | UnwindData |  |
| 1185 | `CryptImportPublicKeyInfoEx2` | `0x9F440` | 850 | UnwindData |  |
| 1026 | `CertAddEncodedCRLToStore` | `0xA01E0` | 109 | UnwindData |  |
| 1044 | `CertCreateCRLContext` | `0xA04F0` | 74 | UnwindData |  |
| 1086 | `CertGetCRLContextProperty` | `0xA0C30` | 33 | UnwindData |  |
| 1088 | `CertGetCTLContextProperty` | `0xA0C30` | 33 | UnwindData |  |
| 1167 | `CryptFormatObject` | `0xA12E0` | 293 | UnwindData |  |
| 1045 | `CertCreateCTLContext` | `0xA1410` | 74 | UnwindData |  |
| 1027 | `CertAddEncodedCTLToStore` | `0xA1460` | 109 | UnwindData |  |
| 1081 | `CertFreeCertificateChain` | `0xA1770` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `CryptMsgDuplicate` | `0xA21D0` | 5,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1282 | `I_CryptGetLruEntryData` | `0xA37F0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1261 | `I_CryptAddRefLruEntry` | `0xA3900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1259 | `I_CertUpdateStore` | `0xA3910` | 216 | UnwindData |  |
| 1263 | `I_CryptAllocTls` | `0xA4790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `CertSerializeCRLStoreElement` | `0xA47A0` | 3,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1123 | `CertSerializeCTLStoreElement` | `0xA47A0` | 3,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1124 | `CertSerializeCertificateStoreElement` | `0xA47A0` | 3,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1272 | `I_CryptFindLruEntryData` | `0xA55C0` | 41 | UnwindData |  |
| 1292 | `I_CryptRemoveLruEntry` | `0xA5B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1059 | `CertEnumCRLContextProperties` | `0xA5BA0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `CertEnumCTLContextProperties` | `0xA5BA0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1063 | `CertEnumCertificateContextProperties` | `0xA5BA0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1111 | `CertOpenSystemStoreW` | `0xA5D80` | 109 | UnwindData |  |
| 1102 | `CertIsStrongHashToSign` | `0xA6690` | 50 | UnwindData |  |
| 1110 | `CertOpenSystemStoreA` | `0xA6EA0` | 109 | UnwindData |  |
| 1295 | `I_CryptUninstallAsn1Module` | `0xA9530` | 7,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `CertFindChainInStore` | `0xAB180` | 277 | UnwindData |  |
| 1108 | `CertOpenServerOcspResponse` | `0xAB630` | 352 | UnwindData |  |
| 1244 | `CryptVerifyCertificateSignature` | `0xABD00` | 66 | UnwindData |  |
| 1165 | `CryptFindLocalizedName` | `0xACF90` | 171 | UnwindData |  |
| 1173 | `CryptGetMessageCertificates` | `0xAD0D0` | 56 | UnwindData |  |
| 1142 | `CertVerifyValidityNesting` | `0xADCB0` | 95 | UnwindData |  |
| 1047 | `CertCreateCertificateChainEngine` | `0xAE140` | 8,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `PFXImportCertStore` | `0xB00C0` | 32 | UnwindData |  |
| 1019 | `I_PFXImportCertStoreEx` | `0xB00F0` | 1,602 | UnwindData |  |
| 1129 | `CertSetEnhancedKeyUsage` | `0xB3A40` | 119 | UnwindData |  |
| 1068 | `CertEnumSystemStoreLocation` | `0xB3D90` | 228 | UnwindData |  |
| 1192 | `CryptMemRealloc` | `0xB3F00` | 3,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1101 | `CertIsRDNAttrsInCertificateName` | `0xB4C30` | 529 | UnwindData |  |
| 1083 | `CertFreeCertificateChainList` | `0xB6140` | 5,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1163 | `CryptExportPublicKeyInfoFromBCryptKeyHandle` | `0xB7770` | 72 | UnwindData |  |
| 1050 | `CertCreateSelfSignCertificate` | `0xB79D0` | 2,483 | UnwindData |  |
| 1011 | *Ordinal Only* | `0xC0E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | *Ordinal Only* | `0xC0E50` | 57 | UnwindData |  |
| 1008 | *Ordinal Only* | `0xC0E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | *Ordinal Only* | `0xC0EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | *Ordinal Only* | `0xC0ED0` | 57 | UnwindData |  |
| 1009 | *Ordinal Only* | `0xC0F10` | 36 | UnwindData |  |
| 1010 | *Ordinal Only* | `0xC0F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | *Ordinal Only* | `0xC0F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | *Ordinal Only* | `0xC0F80` | 36 | UnwindData |  |
| 1281 | `I_CryptGetFileVersion` | `0xC1400` | 228 | UnwindData |  |
| 1002 | *Ordinal Only* | `0xC1500` | 34,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `CertAddCRLLinkToStore` | `0xC9C50` | 89 | UnwindData |  |
| 1023 | `CertAddCTLLinkToStore` | `0xC9C50` | 89 | UnwindData |  |
| 1046 | `CertCreateCTLEntryFromCertificateContextProperties` | `0xC9CB0` | 1,263 | UnwindData |  |
| 1071 | `CertFindCTLInStore` | `0xCA1B0` | 87 | UnwindData |  |
| 1157 | `CryptEnumKeyIdentifierProperties` | `0xCA210` | 217 | UnwindData |  |
| 1029 | `CertAddEncodedCertificateToSystemStoreA` | `0xCA2F0` | 114 | UnwindData |  |
| 1030 | `CertAddEncodedCertificateToSystemStoreW` | `0xCA370` | 114 | UnwindData |  |
| 1031 | `CertAddEnhancedKeyUsageIdentifier` | `0xCA7D0` | 429 | UnwindData |  |
| 1116 | `CertRemoveEnhancedKeyUsageIdentifier` | `0xCA990` | 254 | UnwindData |  |
| 1032 | `CertAddRefServerOcspResponse` | `0xCBD90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1033 | `CertAddRefServerOcspResponseContext` | `0xCBDB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `CertCloseServerOcspResponse` | `0xCBDD0` | 97 | UnwindData |  |
| 1085 | `CertFreeServerOcspResponseContext` | `0xCBE40` | 50 | UnwindData |  |
| 1097 | `CertGetServerOcspResponseContext` | `0xCBE80` | 223 | UnwindData |  |
| 1036 | `CertAlgIdToOID` | `0xCC470` | 61 | UnwindData |  |
| 1076 | `CertFindRDNAttr` | `0xCC4C0` | 102 | UnwindData |  |
| 1135 | `CertVerifyCRLRevocation` | `0xCC530` | 131 | UnwindData |  |
| 1136 | `CertVerifyCRLTimeValidity` | `0xCC5C0` | 196 | UnwindData |  |
| 1164 | `CryptFindCertificateKeyProvInfo` | `0xCC690` | 271 | UnwindData |  |
| 1065 | `CertEnumPhysicalStore` | `0xCECF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1115 | `CertRegisterSystemStore` | `0xCED10` | 250 | UnwindData |  |
| 1134 | `CertUnregisterSystemStore` | `0xCEE10` | 402 | UnwindData |  |
| 1112 | `CertRDNValueToStrA` | `0xCF0F0` | 204 | UnwindData |  |
| 1131 | `CertStrToNameA` | `0xCF1D0` | 393 | UnwindData |  |
| 1148 | `CryptCreateKeyIdentifierFromCSP` | `0xCFB90` | 141 | UnwindData |  |
| 1119 | `CertRetrieveLogoOrBiometricInfo` | `0xD01F0` | 1,053 | UnwindData |  |
| 1137 | `CertVerifyCTLUsage` | `0xD0A40` | 270 | UnwindData |  |
| 1146 | `CryptCloseAsyncHandle` | `0xD13A0` | 29 | UnwindData |  |
| 1227 | `CryptSetAsyncParam` | `0xD13A0` | 29 | UnwindData |  |
| 1290 | `I_CryptRegisterSmartCardStore` | `0xD13A0` | 29 | UnwindData |  |
| 1297 | `I_CryptUnregisterSmartCardStore` | `0xD13A0` | 29 | UnwindData |  |
| 1147 | `CryptCreateAsyncHandle` | `0xD13D0` | 33 | UnwindData |  |
| 1169 | `CryptGetAsyncParam` | `0xD1400` | 47 | UnwindData |  |
| 1149 | `CryptDecodeMessage` | `0xD19D0` | 144 | UnwindData |  |
| 1152 | `CryptDecryptAndVerifyMessageSignature` | `0xD1A70` | 540 | UnwindData |  |
| 1174 | `CryptGetMessageSignerCount` | `0xD1CA0` | 169 | UnwindData |  |
| 1179 | `CryptHashMessage` | `0xD1D50` | 624 | UnwindData |  |
| 1231 | `CryptSignAndEncryptMessage` | `0xD1FD0` | 338 | UnwindData |  |
| 1234 | `CryptSignMessageWithKey` | `0xD2130` | 648 | UnwindData |  |
| 1246 | `CryptVerifyDetachedMessageHash` | `0xD23C0` | 76 | UnwindData |  |
| 1247 | `CryptVerifyDetachedMessageSignature` | `0xD2420` | 116 | UnwindData |  |
| 1248 | `CryptVerifyMessageHash` | `0xD24A0` | 71 | UnwindData |  |
| 1250 | `CryptVerifyMessageSignatureWithKey` | `0xD24F0` | 442 | UnwindData |  |
| 1211 | `CryptRegisterDefaultOIDFunction` | `0xDB390` | 763 | UnwindData |  |
| 1240 | `CryptUnregisterDefaultOIDFunction` | `0xDB6A0` | 680 | UnwindData |  |
| 1213 | `CryptRegisterOIDInfo` | `0xDBB60` | 504 | UnwindData |  |
| 1242 | `CryptUnregisterOIDInfo` | `0xDBD60` | 73 | UnwindData |  |
| 1187 | `CryptInstallDefaultContext` | `0xE45B0` | 519 | UnwindData |  |
| 1237 | `CryptUninstallDefaultContext` | `0xE47C0` | 370 | UnwindData |  |
| 1280 | `I_CryptGetDefaultCryptProvForEncrypt` | `0xE4940` | 379 | UnwindData |  |
| 1260 | `I_CertWnfEnableFlushCache` | `0xE8210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1262 | `I_CryptAddSmartCardCertToStore` | `0xE8240` | 269 | UnwindData |  |
| 1273 | `I_CryptFindSmartCardCertInStore` | `0xE8360` | 554 | UnwindData |  |
| 1284 | `I_CryptGetOssGlobal` | `0xE8590` | 29 | UnwindData |  |
| 1288 | `I_CryptInstallOssGlobal` | `0xE8590` | 29 | UnwindData |  |
| 1296 | `I_CryptUninstallOssGlobal` | `0xE8590` | 29 | UnwindData |  |
| 1118 | `CertResyncCertificateChainEngine` | `0xF9720` | 205 | UnwindData |  |
| 1268 | `I_CryptDisableLruOfEntries` | `0xFA180` | 30 | UnwindData |  |
| 1269 | `I_CryptEnableLruOfEntries` | `0xFA1B0` | 77 | UnwindData |  |
| 1283 | `I_CryptGetLruEntryIdentifier` | `0xFA210` | 13,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `CryptObjectLocatorFree` | `0xFD820` | 59 | UnwindData |  |
| 1013 | `CryptObjectLocatorGet` | `0xFD870` | 56 | UnwindData |  |
| 1014 | `CryptObjectLocatorGetContent` | `0xFD8B0` | 167 | UnwindData |  |
| 1015 | `CryptObjectLocatorGetUpdated` | `0xFD960` | 59 | UnwindData |  |
| 1016 | `CryptObjectLocatorInitialize` | `0xFD9B0` | 877 | UnwindData |  |
| 1017 | `CryptObjectLocatorIsChanged` | `0xFDD30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `CryptObjectLocatorRelease` | `0xFDD60` | 249 | UnwindData |  |
| 1302 | `PFXExportCertStore2` | `0xFED00` | 26 | UnwindData |  |
| 1306 | `PFXVerifyPassword` | `0xFED20` | 47 | UnwindData |  |
| 1160 | `CryptExportPKCS8` | `0xFF5A0` | 82 | UnwindData |  |
| 1182 | `CryptImportPKCS8` | `0xFF600` | 1,197 | UnwindData |  |
| 1189 | `CryptLoadSip` | `0x109BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `CryptSIPAddProvider` | `0x109BC0` | 458 | UnwindData |  |
| 1218 | `CryptSIPGetSealedDigest` | `0x109D90` | 234 | UnwindData |  |
| 1221 | `CryptSIPPutSignedDataMsg` | `0x109E80` | 232 | UnwindData |  |
| 1223 | `CryptSIPRemoveSignedDataMsg` | `0x109F70` | 208 | UnwindData |  |
| 1214 | `CryptRetrieveTimeStamp` | `0x10A050` | 844 | UnwindData |  |
| 1196 | `CryptMsgCountersign` | `0x110170` | 381 | UnwindData |  |
| 1197 | `CryptMsgCountersignEncoded` | `0x110300` | 897 | UnwindData |  |
| 1206 | `CryptMsgVerifyCountersignatureEncoded` | `0x110690` | 75 | UnwindData |  |
| 1199 | `CryptMsgEncodeAndSignCTL` | `0x1106F0` | 244 | UnwindData |  |
| 1204 | `CryptMsgSignCTL` | `0x1107F0` | 233 | UnwindData |  |
