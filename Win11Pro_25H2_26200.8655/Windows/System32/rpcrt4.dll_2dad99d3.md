# Binary Specification: rpcrt4.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\rpcrt4.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2dad99d34322779c1f6945cb0fc6bb996f0f830d0188804482fe6c4a2f39b638`
* **Total Exported Functions:** 557

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1049 | `I_RpcBindingInqDynamicEndpoint` | `0x0` | - | Forwarded | Forwarded to: `RPCRT4.I_RpcBindingInqDynamicEndpointW` |
| 1089 | `I_RpcNsBindingSetEntryName` | `0x0` | - | Forwarded | Forwarded to: `RPCRT4.I_RpcNsBindingSetEntryNameW` |
| 1525 | `RpcSsDontSerializeContext` | `0x0` | - | Forwarded | Forwarded to: `RPCRT4.I_RpcSsDontSerializeContext` |
| 1174 | `NdrClientCall2` | `0x1010` | 37 | UnwindData |  |
| 1016 | `NdrpClientCall2` | `0x1040` | 2,695 | UnwindData |  |
| 1368 | `RpcAsyncAbortCall` | `0x1AD0` | 326 | UnwindData |  |
| 1165 | `NdrAsyncClientCall` | `0x1C20` | 1,128 | UnwindData |  |
| 1370 | `RpcAsyncCompleteCall` | `0x23A0` | 52 | UnwindData |  |
| 1372 | `RpcAsyncInitializeHandle` | `0x2D90` | 126 | UnwindData |  |
| 1166 | `NdrAsyncServerCall` | `0x2E20` | 970 | UnwindData |  |
| 1173 | `NdrClearOutParameters` | `0x3260` | 283 | UnwindData |  |
| 1012 | `NdrFullPointerFree` | `0x3DB0` | 193 | UnwindData |  |
| 1182 | `NdrComplexArrayMarshall` | `0x8FB0` | 1,232 | UnwindData |  |
| 1180 | `NdrComplexArrayBufferSize` | `0x9B00` | 456 | UnwindData |  |
| 1190 | `NdrConformantArrayBufferSize` | `0xA4C0` | 184 | UnwindData |  |
| 1324 | `NdrSimpleStructBufferSize` | `0xB5C0` | 92 | UnwindData |  |
| 1462 | `RpcRaiseException` | `0xBBD0` | 21 | UnwindData |  |
| 1364 | `NdrpMemoryIncrement` | `0xC930` | 1,487 | UnwindData |  |
| 1187 | `NdrComplexStructMarshall` | `0xCF10` | 4,184 | UnwindData |  |
| 1340 | `NdrTypeSize` | `0xE2F0` | 51 | UnwindData |  |
| 1295 | `NdrPointerMarshall` | `0xE5A0` | 203 | UnwindData |  |
| 1281 | `NdrNonEncapsulatedUnionMarshall` | `0x10800` | 498 | UnwindData |  |
| 1339 | `NdrTypeMarshall` | `0x11150` | 71 | UnwindData |  |
| 1326 | `NdrSimpleStructMarshall` | `0x112B0` | 185 | UnwindData |  |
| 1270 | `NdrMesTypeEncode` | `0x11710` | 41 | UnwindData |  |
| 1271 | `NdrMesTypeEncode2` | `0x11CF0` | 1,977 | UnwindData |  |
| 1264 | `NdrMesTypeAlignSize` | `0x124B0` | 374 | UnwindData |  |
| 1267 | `NdrMesTypeDecode` | `0x12630` | 74 | UnwindData |  |
| 1265 | `NdrMesTypeAlignSize2` | `0x128F0` | 886 | UnwindData |  |
| 1268 | `NdrMesTypeDecode2` | `0x12C70` | 1,396 | UnwindData |  |
| 1203 | `NdrConformantStructUnmarshall` | `0x13490` | 67 | UnwindData |  |
| 1194 | `NdrConformantArrayUnmarshall` | `0x13A30` | 335 | UnwindData |  |
| 1184 | `NdrComplexArrayUnmarshall` | `0x141F0` | 628 | UnwindData |  |
| 1183 | `NdrComplexArrayMemorySize` | `0x14FE0` | 444 | UnwindData |  |
| 1283 | `NdrNonEncapsulatedUnionUnmarshall` | `0x15B20` | 227 | UnwindData |  |
| 1332 | `NdrStubCall3` | `0x16B90` | 266 | UnwindData |  |
| 1342 | `NdrUnmarshallBasetypeInline` | `0x16D60` | 435 | UnwindData |  |
| 1312 | `NdrServerCall2` | `0x16F20` | 32 | UnwindData |  |
| 1328 | `NdrSimpleStructUnmarshall` | `0x16F50` | 599 | UnwindData |  |
| 1331 | `NdrStubCall2` | `0x171B0` | 3,232 | UnwindData |  |
| 1189 | `NdrComplexStructUnmarshall` | `0x19350` | 4,160 | UnwindData |  |
| 1181 | `NdrComplexArrayFree` | `0x1A3A0` | 20 | UnwindData |  |
| 1191 | `NdrConformantArrayFree` | `0x1A690` | 78 | UnwindData |  |
| 1288 | `NdrOutInit` | `0x1A780` | 842 | UnwindData |  |
| 1294 | `NdrPointerFree` | `0x1AAD0` | 517 | UnwindData |  |
| 1186 | `NdrComplexStructFree` | `0x1ACE0` | 81 | UnwindData |  |
| 1378 | `RpcBindingFree` | `0x1C130` | 111 | UnwindData |  |
| 1240 | `NdrFullPointerXlatInit` | `0x1C3B0` | 269 | UnwindData |  |
| 1040 | `I_RpcAllocate` | `0x1C4D0` | 48 | UnwindData |  |
| 1317 | `NdrServerContextNewUnmarshall` | `0x1C570` | 322 | UnwindData |  |
| 1269 | `NdrMesTypeDecode3` | `0x1CA20` | 423 | UnwindData |  |
| 1238 | `NdrFreeBuffer` | `0x1CFF0` | 161 | UnwindData |  |
| 1239 | `NdrFullPointerXlatFree` | `0x1DA90` | 91 | UnwindData |  |
| 1272 | `NdrMesTypeEncode3` | `0x1EC50` | 350 | UnwindData |  |
| 1536 | `RpcStringBindingParseW` | `0x2A980` | 1,122 | UnwindData |  |
| 1546 | `UuidCompare` | `0x2C0B0` | 152 | UnwindData |  |
| 1554 | `UuidIsNil` | `0x2C150` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1535 | `RpcStringBindingParseA` | `0x2C1B0` | 876 | UnwindData |  |
| 1533 | `RpcStringBindingComposeA` | `0x2C530` | 1,253 | UnwindData |  |
| 1478 | `RpcServerInterfaceGroupCreateW` | `0x2CE00` | 141 | UnwindData |  |
| 1459 | `RpcObjectSetType` | `0x2E200` | 59 | UnwindData |  |
| 1136 | `I_RpcTransGetThreadEventThreadOptional` | `0x2EFC0` | 26 | UnwindData |  |
| 1488 | `RpcServerSubscribeForNotification` | `0x31730` | 114 | UnwindData |  |
| 1492 | `RpcServerUnsubscribeForNotification` | `0x318F0` | 77 | UnwindData |  |
| 1138 | `I_RpcTransServerNewConnection` | `0x31D90` | 33 | UnwindData |  |
| 1490 | `RpcServerUnregisterIf` | `0x332B0` | 88 | UnwindData |  |
| 1486 | `RpcServerRegisterIf3` | `0x33850` | 176 | UnwindData |  |
| 1151 | `NDRCContextMarshall` | `0x36AC0` | 138 | UnwindData |  |
| 1316 | `NdrServerContextNewMarshall` | `0x36B50` | 580 | UnwindData |  |
| 1154 | `NDRSContextMarshall2` | `0x36DA0` | 580 | UnwindData |  |
| 1547 | `UuidCreate` | `0x375B0` | 80 | UnwindData |  |
| 1067 | `I_RpcExceptionFilter` | `0x39430` | 24 | UnwindData |  |
| 1423 | `RpcExceptionFilter` | `0x39430` | 24 | UnwindData |  |
| 1095 | `I_RpcParseSecurity` | `0x45F80` | 520 | UnwindData |  |
| 1102 | `I_RpcSend` | `0x46290` | 216 | UnwindData |  |
| 1242 | `NdrGetBuffer` | `0x46370` | 729 | UnwindData |  |
| 1380 | `RpcBindingFromStringBindingW` | `0x48D80` | 578 | UnwindData |  |
| 1157 | `NDRSContextUnmarshall2` | `0x4D050` | 77 | UnwindData |  |
| 1075 | `I_RpcGetBufferWithObject` | `0x4FA90` | 77 | UnwindData |  |
| 1088 | `I_RpcNegotiateTransferSyntax` | `0x50350` | 206 | UnwindData |  |
| 1043 | `I_RpcBCacheAllocate` | `0x509E0` | 37 | UnwindData |  |
| 1103 | `I_RpcSendReceive` | `0x50BD0` | 152 | UnwindData |  |
| 1319 | `NdrServerInitialize` | `0x50C70` | 286 | UnwindData |  |
| 1428 | `RpcImpersonateClient` | `0x50DA0` | 195 | UnwindData |  |
| 1044 | `I_RpcBCacheFree` | `0x52580` | 23 | UnwindData |  |
| 1544 | `TowerConstruct` | `0x56E80` | 654 | UnwindData |  |
| 1377 | `RpcBindingCreateW` | `0x57C60` | 413 | UnwindData |  |
| 1375 | `RpcBindingCopy` | `0x58790` | 133 | UnwindData |  |
| 1446 | `RpcMgmtSetComTimeout` | `0x58880` | 105 | UnwindData |  |
| 1399 | `RpcBindingSetOption` | `0x588F0` | 215 | UnwindData |  |
| 1398 | `RpcBindingSetObject` | `0x59050` | 82 | UnwindData |  |
| 1371 | `RpcAsyncGetCallStatus` | `0x59250` | 172 | UnwindData |  |
| 1551 | `UuidFromStringA` | `0x59410` | 228 | UnwindData |  |
| 1552 | `UuidFromStringW` | `0x59E80` | 69 | UnwindData |  |
| 1556 | `UuidToStringW` | `0x5A460` | 100 | UnwindData |  |
| 1534 | `RpcStringBindingComposeW` | `0x5A910` | 447 | UnwindData |  |
| 1470 | `RpcServerInqCallAttributesA` | `0x5B080` | 596 | UnwindData |  |
| 1538 | `RpcStringFreeW` | `0x5B2E0` | 62 | UnwindData |  |
| 1048 | `I_RpcBindingInqClientTokenAttributes` | `0x5B330` | 272 | UnwindData |  |
| 1471 | `RpcServerInqCallAttributesW` | `0x5B450` | 171 | UnwindData |  |
| 1056 | `I_RpcBindingInqTransportType` | `0x5B680` | 153 | UnwindData |  |
| 1390 | `RpcBindingInqObject` | `0x5B720` | 138 | UnwindData |  |
| 1052 | `I_RpcBindingInqLocalClientPID` | `0x5B7B0` | 124 | UnwindData |  |
| 1142 | `MesDecodeBufferHandleCreate` | `0x5B840` | 103 | UnwindData |  |
| 1145 | `MesEncodeFixedBufferHandleCreate` | `0x5BB70` | 56 | UnwindData |  |
| 1141 | `MesBufferHandleReset` | `0x5BEB0` | 49 | UnwindData |  |
| 1396 | `RpcBindingSetAuthInfoExW` | `0x5C710` | 1,312 | UnwindData |  |
| 1429 | `RpcImpersonateClient2` | `0x5CC70` | 149 | UnwindData |  |
| 1555 | `UuidToStringA` | `0x5CD10` | 126 | UnwindData |  |
| 1144 | `MesEncodeDynBufferHandleCreate` | `0x5CDA0` | 256 | UnwindData |  |
| 1465 | `RpcRevertToSelfEx` | `0x5CEB0` | 123 | UnwindData |  |
| 1058 | `I_RpcBindingIsClientLocal` | `0x5CF40` | 118 | UnwindData |  |
| 1397 | `RpcBindingSetAuthInfoW` | `0x5CFC0` | 39 | UnwindData |  |
| 1464 | `RpcRevertToSelf` | `0x5D120` | 77 | UnwindData |  |
| 1374 | `RpcBindingBind` | `0x5D180` | 115 | UnwindData |  |
| 1148 | `MesIncrementalHandleReset` | `0x5D200` | 271 | UnwindData |  |
| 1109 | `I_RpcServerInqLocalConnAddress` | `0x5D320` | 211 | UnwindData |  |
| 1412 | `RpcEpResolveBinding` | `0x5D400` | 99 | UnwindData |  |
| 1143 | `MesDecodeIncrementalHandleCreate` | `0x5D470` | 238 | UnwindData |  |
| 1110 | `I_RpcServerInqRemoteConnAddress` | `0x5D570` | 191 | UnwindData |  |
| 1425 | `RpcGetAuthorizationContextForClient` | `0x5D640` | 295 | UnwindData |  |
| 1147 | `MesHandleFree` | `0x5D9B0` | 320 | UnwindData |  |
| 1445 | `RpcMgmtSetCancelTimeout` | `0x5DB40` | 57 | UnwindData |  |
| 1402 | `RpcBindingUnbind` | `0x5DB80` | 91 | UnwindData |  |
| 1440 | `RpcMgmtInqServerPrincNameA` | `0x5DCC0` | 125 | UnwindData |  |
| 1441 | `RpcMgmtInqServerPrincNameW` | `0x5DD50` | 248 | UnwindData |  |
| 1384 | `RpcBindingInqAuthClientW` | `0x5DE50` | 179 | UnwindData |  |
| 1383 | `RpcBindingInqAuthClientExW` | `0x5DF10` | 182 | UnwindData |  |
| 1521 | `RpcSsContextLockExclusive` | `0x5E150` | 114 | UnwindData |  |
| 1387 | `RpcBindingInqAuthInfoExW` | `0x5E230` | 342 | UnwindData |  |
| 1401 | `RpcBindingToStringBindingW` | `0x5E390` | 108 | UnwindData |  |
| 1393 | `RpcBindingServerFromClient` | `0x5E510` | 168 | UnwindData |  |
| 1117 | `I_RpcServerSubscribeForDisconnectNotification2` | `0x5E5C0` | 398 | UnwindData |  |
| 1118 | `I_RpcServerUnsubscribeForDisconnectNotification` | `0x5E760` | 272 | UnwindData |  |
| 1009 | `I_RpcOpenClientThread` | `0x5E880` | 224 | UnwindData |  |
| 1369 | `RpcAsyncCancelCall` | `0x5E970` | 223 | UnwindData |  |
| 1427 | `RpcIfInqId` | `0x5EF50` | 74 | UnwindData |  |
| 1051 | `I_RpcBindingInqDynamicEndpointW` | `0x5EFA0` | 90 | UnwindData |  |
| 1400 | `RpcBindingToStringBindingA` | `0x5F000` | 125 | UnwindData |  |
| 1041 | `I_RpcAsyncAbortCall` | `0x5FAE0` | 190 | UnwindData |  |
| 1475 | `RpcServerInterfaceGroupActivate` | `0x60440` | 54 | UnwindData |  |
| 1500 | `RpcServerUseProtseqEpExW` | `0x608D0` | 41 | UnwindData |  |
| 1501 | `RpcServerUseProtseqEpW` | `0x60900` | 87 | UnwindData |  |
| 1122 | `I_RpcServerUseProtseqEp2W` | `0x60960` | 171 | UnwindData |  |
| 1476 | `RpcServerInterfaceGroupClose` | `0x61D60` | 44 | UnwindData |  |
| 1468 | `RpcServerInqBindings` | `0x61FB0` | 61 | UnwindData |  |
| 1503 | `RpcServerUseProtseqExW` | `0x62930` | 31 | UnwindData |  |
| 1508 | `RpcServerUseProtseqW` | `0x62960` | 140 | UnwindData |  |
| 1120 | `I_RpcServerUseProtseq2W` | `0x62A00` | 195 | UnwindData |  |
| 1469 | `RpcServerInqBindingsEx` | `0x62D70` | 71 | UnwindData |  |
| 1198 | `NdrConformantStringUnmarshall` | `0x64A90` | 519 | UnwindData |  |
| 1353 | `NdrVaryingArrayUnmarshall` | `0x65110` | 606 | UnwindData |  |
| 1352 | `NdrVaryingArrayMemorySize` | `0x65380` | 355 | UnwindData |  |
| 1170 | `NdrByteCountPointerUnmarshall` | `0x65870` | 520 | UnwindData |  |
| 1327 | `NdrSimpleStructMemorySize` | `0x66240` | 156 | UnwindData |  |
| 1346 | `NdrUserMarshalMemorySize` | `0x662F0` | 567 | UnwindData |  |
| 1282 | `NdrNonEncapsulatedUnionMemorySize` | `0x66530` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1208 | `NdrConformantVaryingArrayUnmarshall` | `0x66630` | 256 | UnwindData |  |
| 1202 | `NdrConformantStructMemorySize` | `0x66A40` | 364 | UnwindData |  |
| 1038 | `IUnknown_QueryInterface_Proxy` | `0x67560` | 99 | UnwindData |  |
| 1027 | `CStdStubBuffer_Disconnect` | `0x675D0` | 56 | UnwindData |  |
| 1224 | `NdrDllCanUnloadNow` | `0x67610` | 76 | UnwindData |  |
| 1185 | `NdrComplexStructBufferSize` | `0x67670` | 66 | UnwindData |  |
| 1188 | `NdrComplexStructMemorySize` | `0x680B0` | 53 | UnwindData |  |
| 1039 | `IUnknown_Release_Proxy` | `0x68BA0` | 63 | UnwindData |  |
| 1037 | `IUnknown_AddRef_Proxy` | `0x68BF0` | 63 | UnwindData |  |
| 1022 | `CStdStubBuffer_AddRef` | `0x68C40` | 62 | UnwindData |  |
| 1028 | `CStdStubBuffer_Invoke` | `0x68C90` | 99 | UnwindData |  |
| 1172 | `NdrCStdStubBuffer_Release` | `0x68D00` | 78 | UnwindData |  |
| 1225 | `NdrDllGetClassObject` | `0x68D60` | 138 | UnwindData |  |
| 1286 | `NdrOleAllocate` | `0x68DF0` | 66 | UnwindData |  |
| 1287 | `NdrOleFree` | `0x68E40` | 59 | UnwindData |  |
| 1031 | `CreateProxyFromTypeInfo` | `0x69120` | 125 | UnwindData |  |
| 1171 | `NdrCStdStubBuffer2_Release` | `0x691B0` | 78 | UnwindData |  |
| 1293 | `NdrPointerBufferSize` | `0x69270` | 514 | UnwindData |  |
| 1279 | `NdrNonEncapsulatedUnionBufferSize` | `0x69730` | 590 | UnwindData |  |
| 1032 | `CreateStubFromTypeInfo` | `0x69C80` | 115 | UnwindData |  |
| 1030 | `CStdStubBuffer_QueryInterface` | `0x69D00` | 99 | UnwindData |  |
| 1333 | `NdrStubForwardingFunction` | `0x69D70` | 106 | UnwindData |  |
| 1026 | `CStdStubBuffer_DebugServerRelease` | `0x6A000` | 71 | UnwindData |  |
| 1025 | `CStdStubBuffer_DebugServerQueryInterface` | `0x6A050` | 83 | UnwindData |  |
| 1367 | `NdrpVarVtOfTypeDesc` | `0x6A0B0` | 102 | UnwindData |  |
| 1365 | `NdrpReleaseTypeFormatString` | `0x6A120` | 76 | UnwindData |  |
| 1363 | `NdrpGetTypeGenCookie` | `0x6A180` | 76 | UnwindData |  |
| 1361 | `NdrpGetProcFormatString` | `0x6A1E0` | 140 | UnwindData |  |
| 1362 | `NdrpGetTypeFormatString` | `0x6A280` | 102 | UnwindData |  |
| 1226 | `NdrDllRegisterProxy` | `0x6A2F0` | 102 | UnwindData |  |
| 1042 | `I_RpcAsyncSetHandle` | `0x76200` | 521 | UnwindData |  |
| 1083 | `I_RpcMapWin32Status` | `0x778F0` | 16,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `NdrServerInitializeNew` | `0x7B950` | 428 | UnwindData |  |
| 1098 | `I_RpcReceive` | `0x7BC40` | 206 | UnwindData |  |
| 1311 | `NdrSendReceive` | `0x7BD50` | 247 | UnwindData |  |
| 1100 | `I_RpcRequestMutex` | `0x7BE50` | 109 | UnwindData |  |
| 1074 | `I_RpcGetBuffer` | `0x7BF20` | 636 | UnwindData |  |
| 1483 | `RpcServerRegisterAuthInfoW` | `0x7C450` | 112 | UnwindData |  |
| 1473 | `RpcServerInqDefaultPrincNameW` | `0x7C5D0` | 177 | UnwindData |  |
| 1417 | `RpcErrorGetNextRecord` | `0x7E6A0` | 75 | UnwindData |  |
| 1297 | `NdrPointerUnmarshall` | `0x7F1E0` | 1,466 | UnwindData |  |
| 1330 | `NdrSimpleTypeUnmarshall` | `0x80210` | 749 | UnwindData |  |
| 1348 | `NdrUserMarshalUnmarshall` | `0x82100` | 900 | UnwindData |  |
| 1303 | `NdrRangeUnmarshall` | `0x83150` | 528 | UnwindData |  |
| 1351 | `NdrVaryingArrayMarshall` | `0x83FF0` | 307 | UnwindData |  |
| 1349 | `NdrVaryingArrayBufferSize` | `0x84130` | 250 | UnwindData |  |
| 1206 | `NdrConformantVaryingArrayMarshall` | `0x84230` | 41 | UnwindData |  |
| 1192 | `NdrConformantArrayMarshall` | `0x85BC0` | 240 | UnwindData |  |
| 1329 | `NdrSimpleTypeMarshall` | `0x85CC0` | 49 | UnwindData |  |
| 1247 | `NdrGetTypeFlags` | `0x85EF0` | 1,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1341 | `NdrTypeUnmarshall` | `0x865D0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `NdrConformantStringBufferSize` | `0x86860` | 402 | UnwindData |  |
| 1248 | `NdrGetUserMarshalInfo` | `0x86A00` | 216 | UnwindData |  |
| 1273 | `NdrMesTypeFree2` | `0x86CE0` | 362 | UnwindData |  |
| 1219 | `NdrCorrelationInitialize` | `0x86F70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `NdrConformantStringMarshall` | `0x86FC0` | 404 | UnwindData |  |
| 1343 | `NdrUserMarshalBufferSize` | `0x87160` | 770 | UnwindData |  |
| 1345 | `NdrUserMarshalMarshall` | `0x87690` | 362 | UnwindData |  |
| 1512 | `RpcSmDestroyClientContext` | `0x87EE0` | 26 | UnwindData |  |
| 1523 | `RpcSsDestroyClientContext` | `0x87F00` | 112 | UnwindData |  |
| 1150 | `NDRCContextBinding` | `0x880D0` | 45 | UnwindData |  |
| 1199 | `NdrConformantStructBufferSize` | `0x883A0` | 314 | UnwindData |  |
| 1070 | `I_RpcFreeBuffer` | `0x88580` | 132 | UnwindData |  |
| 1001 | `I_RpcBindingInqCurrentModifiedId` | `0x88A80` | 131 | UnwindData |  |
| 1435 | `RpcMgmtEpEltInqNextW` | `0x88BF0` | 93 | UnwindData |  |
| 1434 | `RpcMgmtEpEltInqNextA` | `0x88C60` | 1,531 | UnwindData |  |
| 1545 | `TowerExplode` | `0x89270` | 889 | UnwindData |  |
| 1201 | `NdrConformantStructMarshall` | `0x89F80` | 301 | UnwindData |  |
| 1179 | `NdrClientInitializeNew` | `0x8A240` | 271 | UnwindData |  |
| 1073 | `I_RpcFreeSystemHandleCollection` | `0x8A3C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `NdrTypeFree` | `0x8A3F0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `NdrClientInitialize` | `0x8A600` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `NdrServerCallAll` | `0x8A740` | 66 | UnwindData |  |
| 1550 | `UuidEqual` | `0x8AFE0` | 91 | UnwindData |  |
| 1218 | `NdrCorrelationFree` | `0x8B0D0` | 6,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1169 | `NdrByteCountPointerMarshall` | `0x8CA80` | 172 | UnwindData |  |
| 1220 | `NdrCorrelationPass` | `0x8E570` | 102 | UnwindData |  |
| 1094 | `I_RpcOpenClientProcess` | `0x8EC70` | 248 | UnwindData |  |
| 1233 | `NdrFixedArrayBufferSize` | `0x8EDB0` | 121 | UnwindData |  |
| 1235 | `NdrFixedArrayMarshall` | `0x8F050` | 201 | UnwindData |  |
| 1280 | `NdrNonEncapsulatedUnionFree` | `0x8F900` | 263 | UnwindData |  |
| 1237 | `NdrFixedArrayUnmarshall` | `0x8FA80` | 326 | UnwindData |  |
| 1236 | `NdrFixedArrayMemorySize` | `0x8FEE0` | 178 | UnwindData |  |
| 1045 | `I_RpcBindingCopy` | `0x90570` | 105 | UnwindData |  |
| 1214 | `NdrContextHandleInitialize` | `0x90720` | 192 | UnwindData |  |
| 1344 | `NdrUserMarshalFree` | `0x92090` | 166 | UnwindData |  |
| 1266 | `NdrMesTypeAlignSize3` | `0x924C0` | 350 | UnwindData |  |
| 1197 | `NdrConformantStringMemorySize` | `0x92760` | 97 | UnwindData |  |
| 1467 | `RpcServerInqBindingHandle` | `0x92900` | 47 | UnwindData |  |
| 1414 | `RpcErrorAddRecord` | `0x939B0` | 246 | UnwindData |  |
| 1422 | `RpcErrorStartEnumeration` | `0x93C40` | 80 | UnwindData |  |
| 1080 | `I_RpcGetSystemHandle` | `0x93DC0` | 90 | UnwindData |  |
| 1069 | `I_RpcFree` | `0x93ED0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1308 | `NdrRpcSsDefaultFree` | `0x93ED0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `NdrConformantArrayMemorySize` | `0x93FD0` | 66 | UnwindData |  |
| 1489 | `RpcServerTestCancel` | `0x94160` | 86 | UnwindData |  |
| 1424 | `RpcFreeAuthorizationContext` | `0x94290` | 58 | UnwindData |  |
| 1167 | `NdrByteCountPointerBufferSize` | `0x942D0` | 153 | UnwindData |  |
| 1205 | `NdrConformantVaryingArrayFree` | `0x94440` | 113 | UnwindData |  |
| 1125 | `I_RpcSetSystemHandle` | `0x94780` | 50 | UnwindData |  |
| 1131 | `I_RpcTransConnectionReallocPacket` | `0x949F0` | 112 | UnwindData |  |
| 1107 | `I_RpcServerGetAssociationID` | `0x94DF0` | 85 | UnwindData |  |
| 1234 | `NdrFixedArrayFree` | `0x94F80` | 7,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1274 | `NdrMesTypeFree3` | `0x96C60` | 333 | UnwindData |  |
| 1204 | `NdrConformantVaryingArrayBufferSize` | `0x96DC0` | 56 | UnwindData |  |
| 1553 | `UuidHash` | `0x96FA0` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1168 | `NdrByteCountPointerFree` | `0x974C0` | 51 | UnwindData |  |
| 1298 | `NdrProxyErrorHandler` | `0x97AE0` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `NdrServerInitializeMarshall` | `0x97EF0` | 2,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1072 | `I_RpcFreeSystemHandle` | `0x989D0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1549 | `UuidCreateSequential` | `0x98AE0` | 292 | UnwindData |  |
| 1254 | `NdrMapCommAndFaultStatus` | `0x991F0` | 115 | UnwindData |  |
| 1063 | `I_RpcClearMutex` | `0x9AB10` | 1,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1373 | `RpcAsyncRegisterInfo` | `0x9B0D0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1416 | `RpcErrorEndEnumeration` | `0x9B270` | 53 | UnwindData |  |
| 1350 | `NdrVaryingArrayFree` | `0x9B2B0` | 104 | UnwindData |  |
| 1452 | `RpcNetworkInqProtseqsW` | `0x9B7A0` | 44 | UnwindData |  |
| 1454 | `RpcNetworkIsProtseqValidW` | `0x9B7E0` | 44 | UnwindData |  |
| 1461 | `RpcProtseqVectorFreeW` | `0x9BAB0` | 116 | UnwindData |  |
| 1309 | `NdrRpcSsDisableAllocate` | `0x9BFE0` | 51 | UnwindData |  |
| 1379 | `RpcBindingFromStringBindingA` | `0x9C240` | 144 | UnwindData |  |
| 1537 | `RpcStringFreeA` | `0x9C2E0` | 2,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `I_RpcInitNdrImports` | `0x9CC00` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | *Ordinal Only* | `0x9D110` | 68 | UnwindData |  |
| 1146 | `MesEncodeIncrementalHandleCreate` | `0x9D250` | 161 | UnwindData |  |
| 1135 | `I_RpcTransGetThreadEvent` | `0x9D8A0` | 19 | UnwindData |  |
| 1443 | `RpcMgmtIsServerListening` | `0x9D920` | 136 | UnwindData |  |
| 1403 | `RpcBindingVectorFree` | `0x9DD60` | 120 | UnwindData |  |
| 1008 | `I_RpcMgmtQueryDedicatedThreadPool` | `0x9DEB0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1528 | `RpcSsGetContextBinding` | `0x9DFA0` | 55 | UnwindData |  |
| 1481 | `RpcServerListen` | `0x9E850` | 90 | UnwindData |  |
| 1101 | `I_RpcSNCHOption` | `0x9EC00` | 94 | UnwindData |  |
| 1129 | `I_RpcTransConnectionAllocatePacket` | `0x9EEB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1082 | `I_RpcLogEvent` | `0x9EEC0` | 2,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1447 | `RpcMgmtSetServerStackSize` | `0x9F850` | 87 | UnwindData |  |
| 1130 | `I_RpcTransConnectionFreePacket` | `0x9FE50` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1081 | `I_RpcIfInqTransferSyntaxes` | `0xA0140` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1276 | `NdrNonConformantStringMarshall` | `0xA02B0` | 242 | UnwindData |  |
| 1128 | `I_RpcSystemHandleTypeSpecificWork` | `0xA03B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1278 | `NdrNonConformantStringUnmarshall` | `0xA03F0` | 424 | UnwindData |  |
| 1277 | `NdrNonConformantStringMemorySize` | `0xA05A0` | 274 | UnwindData |  |
| 1124 | `I_RpcSetDCOMAppId` | `0xA06C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `NdrConvert2` | `0xA06E0` | 194 | UnwindData |  |
| 1275 | `NdrNonConformantStringBufferSize` | `0xA0A90` | 260 | UnwindData |  |
| 1491 | `RpcServerUnregisterIfEx` | `0xA0BA0` | 120 | UnwindData |  |
| 1246 | `NdrGetSimpleTypeMemorySize` | `0xA1360` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1487 | `RpcServerRegisterIfEx` | `0xA14B0` | 156 | UnwindData |  |
| 1479 | `RpcServerInterfaceGroupDeactivate` | `0xA15C0` | 73 | UnwindData |  |
| 1498 | `RpcServerUseProtseqEpA` | `0xA1770` | 87 | UnwindData |  |
| 1121 | `I_RpcServerUseProtseqEp2A` | `0xA17D0` | 613 | UnwindData |  |
| 1060 | `I_RpcBindingSetPrivateOption` | `0xA1D70` | 104 | UnwindData |  |
| 1411 | `RpcEpRegisterW` | `0xA2420` | 26 | UnwindData |  |
| 1432 | `RpcMgmtEpEltInqBegin` | `0xA2490` | 677 | UnwindData |  |
| 1394 | `RpcBindingSetAuthInfoA` | `0xA3130` | 39 | UnwindData |  |
| 1395 | `RpcBindingSetAuthInfoExA` | `0xA3160` | 276 | UnwindData |  |
| 1085 | `I_RpcMgmtEnableDedicatedThreadPool` | `0xA32D0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `NdrContextHandleSize` | `0xA33A0` | 75 | UnwindData |  |
| 1449 | `RpcMgmtStopServerListening` | `0xA3400` | 142 | UnwindData |  |
| 1485 | `RpcServerRegisterIf2` | `0xA3780` | 157 | UnwindData |  |
| 1433 | `RpcMgmtEpEltInqDone` | `0xA3C30` | 162 | UnwindData |  |
| 1484 | `RpcServerRegisterIf` | `0xA5290` | 121 | UnwindData |  |
| 1413 | `RpcEpUnregister` | `0xA5310` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `I_RpcServerDisableExceptionFilter` | `0xA53C0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1548 | `UuidCreateNil` | `0xA5560` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1431 | `RpcMgmtEnableIdleCleanup` | `0xA5EB0` | 40 | UnwindData |  |
| 1076 | `I_RpcGetCurrentCallHandle` | `0xA6210` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1482 | `RpcServerRegisterAuthInfoA` | `0xA66A0` | 182 | UnwindData |  |
| 1381 | `RpcBindingInqAuthClientA` | `0xA7810` | 40 | UnwindData |  |
| 1137 | `I_RpcTransIoCancelled` | `0xA7840` | 51 | UnwindData |  |
| 1450 | `RpcMgmtWaitServerListen` | `0xA7AB0` | 33 | UnwindData |  |
| 1253 | `NdrInterfacePointerUnmarshall` | `0xA8B50` | 156 | UnwindData |  |
| 1207 | `NdrConformantVaryingArrayMemorySize` | `0xA8C00` | 66 | UnwindData |  |
| 1046 | `I_RpcBindingCreateNP` | `0xA9100` | 611 | UnwindData |  |
| 1228 | `NdrEncapsulatedUnionBufferSize` | `0xA9440` | 150 | UnwindData |  |
| 1230 | `NdrEncapsulatedUnionMarshall` | `0xA94E0` | 152 | UnwindData |  |
| 1322 | `NdrServerInitializePartial` | `0xA9580` | 104 | UnwindData |  |
| 1251 | `NdrInterfacePointerMarshall` | `0xA9810` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `NdrInterfacePointerBufferSize` | `0xA99D0` | 144 | UnwindData |  |
| 1231 | `NdrEncapsulatedUnionMemorySize` | `0xA9E10` | 83 | UnwindData |  |
| 1086 | `I_RpcNDRCGetWireRepresentation` | `0xA9F20` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1382 | `RpcBindingInqAuthClientExA` | `0xAA0F0` | 171 | UnwindData |  |
| 1097 | `I_RpcReallocPipeBuffer` | `0xAA630` | 73 | UnwindData |  |
| 1310 | `NdrRpcSsEnableAllocate` | `0xAA680` | 85 | UnwindData |  |
| 1418 | `RpcErrorGetNumberOfRecords` | `0xAB750` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1420 | `RpcErrorResetEnumeration` | `0xAB780` | 11,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1050 | `I_RpcBindingInqDynamicEndpointA` | `0xAE310` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1090 | `I_RpcNsBindingSetEntryNameA` | `0xAE310` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1116 | `I_RpcServerSubscribeForDisconnectNotification` | `0xAE310` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1132 | `I_RpcTransDatagramAllocate` | `0xAE310` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1133 | `I_RpcTransDatagramAllocate2` | `0xAE310` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1134 | `I_RpcTransDatagramFree` | `0xAE310` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `I_RpcFixTransferSyntax` | `0xAF260` | 144 | UnwindData |  |
| 1064 | `I_RpcCompleteAndFree` | `0xAF300` | 170 | UnwindData |  |
| 1096 | `I_RpcPauseExecution` | `0xAF3B0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `I_RpcFwThisIsTheManager` | `0xAF480` | 35 | UnwindData |  |
| 1004 | `I_RpcInitFwImports` | `0xAF500` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `I_RpcInitImports` | `0xAF590` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `I_RpcServerTurnOnOffKeepalives` | `0xAF650` | 157 | UnwindData |  |
| 1059 | `I_RpcBindingIsServerLocal` | `0xAF700` | 93 | UnwindData |  |
| 1077 | `I_RpcGetDefaultSD` | `0xAF770` | 49 | UnwindData |  |
| 1108 | `I_RpcServerInqAddressChangeFn` | `0xAF7B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1112 | `I_RpcServerIsClientDisconnected` | `0xAF7C0` | 115 | UnwindData |  |
| 1113 | `I_RpcServerRegisterForwardFunction` | `0xAF840` | 50 | UnwindData |  |
| 1114 | `I_RpcServerSetAddressChangeFn` | `0xAF880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1115 | `I_RpcServerStartService` | `0xAF8A0` | 110 | UnwindData |  |
| 1123 | `I_RpcSessionStrictContextHandle` | `0xAF920` | 44 | UnwindData |  |
| 1426 | `RpcIfIdVectorFree` | `0xAF960` | 92 | UnwindData |  |
| 1430 | `RpcImpersonateClientContainer` | `0xAF9D0` | 141 | UnwindData |  |
| 1439 | `RpcMgmtInqIfIds` | `0xAFA70` | 175 | UnwindData |  |
| 1442 | `RpcMgmtInqStats` | `0xAFB30` | 306 | UnwindData |  |
| 1448 | `RpcMgmtStatsVectorFree` | `0xAFC70` | 58 | UnwindData |  |
| 1457 | `RpcObjectInqType` | `0xAFCB0` | 103 | UnwindData |  |
| 1458 | `RpcObjectSetInqFn` | `0xAFD20` | 43 | UnwindData |  |
| 1463 | `RpcRevertContainerImpersonation` | `0xAFD60` | 67 | UnwindData |  |
| 1466 | `RpcServerCompleteSecurityCallback` | `0xAFDB0` | 83 | UnwindData |  |
| 1472 | `RpcServerInqDefaultPrincNameA` | `0xAFE10` | 87 | UnwindData |  |
| 1474 | `RpcServerInqIf` | `0xAFE70` | 146 | UnwindData |  |
| 1477 | `RpcServerInterfaceGroupCreateA` | `0xAFF10` | 874 | UnwindData |  |
| 1480 | `RpcServerInterfaceGroupInqBindings` | `0xB0280` | 67 | UnwindData |  |
| 1493 | `RpcServerUseAllProtseqs` | `0xB02D0` | 37 | UnwindData |  |
| 1494 | `RpcServerUseAllProtseqsEx` | `0xB0300` | 422 | UnwindData |  |
| 1495 | `RpcServerUseAllProtseqsIf` | `0xB04B0` | 66 | UnwindData |  |
| 1496 | `RpcServerUseAllProtseqsIfEx` | `0xB0500` | 197 | UnwindData |  |
| 1506 | `RpcServerUseProtseqIfExW` | `0xB05D0` | 322 | UnwindData |  |
| 1507 | `RpcServerUseProtseqIfW` | `0xB0720` | 71 | UnwindData |  |
| 1011 | `I_RpcVerifierCorruptionExpected` | `0xB0770` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `I_RpcEnableWmiTrace` | `0xB0A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `RpcCertMatchPrincipalName` | `0xB0A90` | 90 | UnwindData |  |
| 1062 | `I_RpcCertProcessAndProvision` | `0xB0B40` | 124 | UnwindData |  |
| 1407 | `RpcCertGeneratePrincipalNameW` | `0xB0C70` | 101 | UnwindData |  |
| 1033 | `DceErrorInqTextA` | `0xB0CE0` | 126 | UnwindData |  |
| 1034 | `DceErrorInqTextW` | `0xB0D70` | 133 | UnwindData |  |
| 1437 | `RpcMgmtInqComTimeout` | `0xB0E00` | 77 | UnwindData |  |
| 1054 | `I_RpcBindingInqSecurityContext` | `0xB0EF0` | 88 | UnwindData |  |
| 1055 | `I_RpcBindingInqSecurityContextKeyInfo` | `0xB0F50` | 128 | UnwindData |  |
| 1084 | `I_RpcMarshalBindingHandleAndInterfaceForNDF` | `0xB0FE0` | 78 | UnwindData |  |
| 1091 | `I_RpcNsBindingSetEntryNameW` | `0xB1040` | 78 | UnwindData |  |
| 1092 | `I_RpcNsInterfaceExported` | `0xB1040` | 78 | UnwindData |  |
| 1093 | `I_RpcNsInterfaceUnexported` | `0xB1040` | 78 | UnwindData |  |
| 1456 | `RpcNsBindingInqEntryNameW` | `0xB1040` | 78 | UnwindData |  |
| 1139 | `I_RpcTurnOnEEInfoPropagation` | `0xB10A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1388 | `RpcBindingInqAuthInfoW` | `0xB1160` | 120 | UnwindData |  |
| 1392 | `RpcBindingReset` | `0xB11E0` | 80 | UnwindData |  |
| 1284 | `NdrNsGetBuffer` | `0xB3F70` | 15 | UnwindData |  |
| 1285 | `NdrNsSendReceive` | `0xB3F70` | 15 | UnwindData |  |
| 1047 | `I_RpcBindingHandleToAsyncHandle` | `0xB41B0` | 102 | UnwindData |  |
| 1053 | `I_RpcBindingInqMarshalledTargetInfo` | `0xB4220` | 113 | UnwindData |  |
| 1057 | `I_RpcBindingInqWireIdForSnego` | `0xB42A0` | 114 | UnwindData |  |
| 1061 | `I_RpcBindingToStaticStringBindingW` | `0xB4340` | 109 | UnwindData |  |
| 1389 | `RpcBindingInqMaxCalls` | `0xB43C0` | 94 | UnwindData |  |
| 1391 | `RpcBindingInqOption` | `0xB4430` | 114 | UnwindData |  |
| 1438 | `RpcMgmtInqDefaultProtectLevel` | `0xB44B0` | 142 | UnwindData |  |
| 1065 | `I_RpcDeleteMutex` | `0xB4550` | 20 | UnwindData |  |
| 1079 | `I_RpcGetPortAllocationData` | `0xB4570` | 1,499 | UnwindData |  |
| 1068 | `I_RpcFilterDCOMActivation` | `0xB8A60` | 178 | UnwindData |  |
| 1071 | `I_RpcFreePipeBuffer` | `0xB8F40` | 33 | UnwindData |  |
| 1111 | `I_RpcServerInqTransportType` | `0xB8F70` | 56 | UnwindData |  |
| 1078 | `I_RpcGetExtendedError` | `0xB9250` | 48 | UnwindData |  |
| 1404 | `RpcCancelThread` | `0xB9290` | 67 | UnwindData |  |
| 1405 | `RpcCancelThreadEx` | `0xB92E0` | 76 | UnwindData |  |
| 1509 | `RpcServerYield` | `0xB9340` | 66 | UnwindData |  |
| 1539 | `RpcTestCancel` | `0xB9390` | 1,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1127 | `I_RpcSystemFunction001` | `0xB9AC0` | 648 | UnwindData |  |
| 1105 | `I_RpcServerCheckClientRestriction` | `0xBAE40` | 85 | UnwindData |  |
| 1099 | `I_RpcRecordCalloutFailure` | `0xBBEB0` | 221 | UnwindData |  |
| 1415 | `RpcErrorClearInformation` | `0xBBFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1419 | `RpcErrorLoadErrorInfo` | `0xBBFB0` | 57 | UnwindData |  |
| 1421 | `RpcErrorSaveErrorInfo` | `0xBBFF0` | 388 | UnwindData |  |
| 1104 | `I_RpcServerAllocateIpPort` | `0xBC220` | 377 | UnwindData |  |
| 1119 | `I_RpcServerUseProtseq2A` | `0xBC3A0` | 434 | UnwindData |  |
| 1376 | `RpcBindingCreateA` | `0xBC560` | 807 | UnwindData |  |
| 1385 | `RpcBindingInqAuthInfoA` | `0xBC890` | 46 | UnwindData |  |
| 1386 | `RpcBindingInqAuthInfoExA` | `0xBC8D0` | 168 | UnwindData |  |
| 1406 | `RpcCertGeneratePrincipalNameA` | `0xBC980` | 87 | UnwindData |  |
| 1451 | `RpcNetworkInqProtseqsA` | `0xBC9E0` | 133 | UnwindData |  |
| 1453 | `RpcNetworkIsProtseqValidA` | `0xBCA70` | 357 | UnwindData |  |
| 1455 | `RpcNsBindingInqEntryNameA` | `0xBCBE0` | 115 | UnwindData |  |
| 1460 | `RpcProtseqVectorFreeA` | `0xBCC60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1497 | `RpcServerUseProtseqA` | `0xBCC70` | 82 | UnwindData |  |
| 1499 | `RpcServerUseProtseqEpExA` | `0xBCCD0` | 41 | UnwindData |  |
| 1502 | `RpcServerUseProtseqExA` | `0xBCD00` | 31 | UnwindData |  |
| 1504 | `RpcServerUseProtseqIfA` | `0xBCD30` | 71 | UnwindData |  |
| 1505 | `RpcServerUseProtseqIfExA` | `0xBCD80` | 392 | UnwindData |  |
| 1140 | `I_UuidCreate` | `0xBCF10` | 25 | UnwindData |  |
| 1408 | `RpcEpRegisterA` | `0xBCF30` | 26 | UnwindData |  |
| 1409 | `RpcEpRegisterNoReplaceA` | `0xBCF50` | 228 | UnwindData |  |
| 1410 | `RpcEpRegisterNoReplaceW` | `0xBD040` | 137 | UnwindData |  |
| 1436 | `RpcMgmtEpUnregister` | `0xBD0D0` | 15 | UnwindData |  |
| 1444 | `RpcMgmtSetAuthorizationFn` | `0xBD0F0` | 29,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1152 | `NDRCContextUnmarshall` | `0xC42A0` | 28 | UnwindData |  |
| 1087 | `I_RpcNDRSContextEmergencyCleanup` | `0xC4420` | 24 | UnwindData |  |
| 1126 | `I_RpcSsDontSerializeContext` | `0xC4440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1153 | `NDRSContextMarshall` | `0xC4460` | 74 | UnwindData |  |
| 1155 | `NDRSContextMarshallEx` | `0xC44B0` | 26 | UnwindData |  |
| 1156 | `NDRSContextUnmarshall` | `0xC44D0` | 54 | UnwindData |  |
| 1158 | `NDRSContextUnmarshallEx` | `0xC4510` | 23 | UnwindData |  |
| 1522 | `RpcSsContextLockShared` | `0xC4530` | 118 | UnwindData |  |
| 1013 | `NdrFullPointerInsertRefId` | `0xC45B0` | 165 | UnwindData |  |
| 1014 | `NdrFullPointerQueryPointer` | `0xC4660` | 452 | UnwindData |  |
| 1015 | `NdrFullPointerQueryRefId` | `0xC4830` | 270 | UnwindData |  |
| 1200 | `NdrConformantStructFree` | `0xC4B30` | 97 | UnwindData |  |
| 1210 | `NdrConformantVaryingStructFree` | `0xC4BA0` | 153 | UnwindData |  |
| 1229 | `NdrEncapsulatedUnionFree` | `0xC4C40` | 139 | UnwindData |  |
| 1250 | `NdrInterfacePointerFree` | `0xC4CE0` | 34 | UnwindData |  |
| 1325 | `NdrSimpleStructFree` | `0xC4D10` | 25 | UnwindData |  |
| 1355 | `NdrXmitOrRepAsFree` | `0xC4D30` | 56 | UnwindData |  |
| 1176 | `NdrClientContextMarshall` | `0xC4D90` | 69 | UnwindData |  |
| 1211 | `NdrConformantVaryingStructMarshall` | `0xC4DE0` | 323 | UnwindData |  |
| 1290 | `NdrPartialIgnoreClientMarshall` | `0xC4F30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1315 | `NdrServerContextMarshall` | `0xC4F60` | 62 | UnwindData |  |
| 1356 | `NdrXmitOrRepAsMarshall` | `0xC4FB0` | 383 | UnwindData |  |
| 1209 | `NdrConformantVaryingStructBufferSize` | `0xC5260` | 268 | UnwindData |  |
| 1289 | `NdrPartialIgnoreClientBufferSize` | `0xC5380` | 42 | UnwindData |  |
| 1354 | `NdrXmitOrRepAsBufferSize` | `0xC53B0` | 378 | UnwindData |  |
| 1177 | `NdrClientContextUnmarshall` | `0xC5E80` | 86 | UnwindData |  |
| 1213 | `NdrConformantVaryingStructUnmarshall` | `0xC5EE0` | 1,468 | UnwindData |  |
| 1232 | `NdrEncapsulatedUnionUnmarshall` | `0xC64B0` | 238 | UnwindData |  |
| 1292 | `NdrPartialIgnoreServerUnmarshall` | `0xC65B0` | 72 | UnwindData |  |
| 1318 | `NdrServerContextUnmarshall` | `0xC6600` | 100 | UnwindData |  |
| 1358 | `NdrXmitOrRepAsUnmarshall` | `0xC6670` | 759 | UnwindData |  |
| 1023 | `CStdStubBuffer_Connect` | `0xC6970` | 83 | UnwindData |  |
| 1024 | `CStdStubBuffer_CountRefs` | `0xC69D0` | 63 | UnwindData |  |
| 1029 | `CStdStubBuffer_IsIIDSupported` | `0xC6A20` | 75 | UnwindData |  |
| 1035 | `DllGetClassObject` | `0xC6A80` | 99 | UnwindData |  |
| 1036 | `DllRegisterServer` | `0xC6AF0` | 63 | UnwindData |  |
| 1162 | `Ndr64DcomAsyncClientCall` | `0xC6B40` | 112 | UnwindData |  |
| 1163 | `Ndr64DcomAsyncStubCall` | `0xC6BC0` | 118 | UnwindData |  |
| 1221 | `NdrCreateServerInterfaceFromStub` | `0xC6C40` | 74 | UnwindData |  |
| 1222 | `NdrDcomAsyncClientCall` | `0xC6C90` | 114 | UnwindData |  |
| 1223 | `NdrDcomAsyncStubCall` | `0xC6D10` | 118 | UnwindData |  |
| 1227 | `NdrDllUnregisterProxy` | `0xC6D90` | 102 | UnwindData |  |
| 1241 | `NdrGetBaseInterfaceFromStub` | `0xC6E00` | 102 | UnwindData |  |
| 1243 | `NdrGetDcomProtocolVersion` | `0xC6E70` | 86 | UnwindData |  |
| 1299 | `NdrProxyFreeBuffer` | `0xC6ED0` | 71 | UnwindData |  |
| 1300 | `NdrProxyGetBuffer` | `0xC6F20` | 71 | UnwindData |  |
| 1301 | `NdrProxyInitialize` | `0xC6F70` | 119 | UnwindData |  |
| 1302 | `NdrProxySendReceive` | `0xC6FF0` | 71 | UnwindData |  |
| 1334 | `NdrStubGetBuffer` | `0xC7040` | 87 | UnwindData |  |
| 1335 | `NdrStubInitialize` | `0xC70A0` | 111 | UnwindData |  |
| 1336 | `NdrStubInitializeMarshall` | `0xC7120` | 96 | UnwindData |  |
| 1359 | `NdrpCreateProxy` | `0xC7190` | 118 | UnwindData |  |
| 1360 | `NdrpCreateStub` | `0xC7210` | 102 | UnwindData |  |
| 1366 | `NdrpReleaseTypeGenCookie` | `0xC7280` | 76 | UnwindData |  |
| 1149 | `MesInqProcEncodingId` | `0xC7660` | 278 | UnwindData |  |
| 1255 | `NdrMesProcEncodeDecode` | `0xC7780` | 1,229 | UnwindData |  |
| 1256 | `NdrMesProcEncodeDecode2` | `0xC7C60` | 677 | UnwindData |  |
| 1258 | `NdrMesSimpleTypeAlignSize` | `0xC7F10` | 90 | UnwindData |  |
| 1260 | `NdrMesSimpleTypeDecode` | `0xC7F70` | 306 | UnwindData |  |
| 1262 | `NdrMesSimpleTypeEncode` | `0xC80B0` | 217 | UnwindData |  |
| 1164 | `NdrAllocate` | `0xC8650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `NdrServerInitializeUnmarshall` | `0xC8660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1540 | `RpcUserFree` | `0xC8680` | 80 | UnwindData |  |
| 1212 | `NdrConformantVaryingStructMemorySize` | `0xC8C20` | 379 | UnwindData |  |
| 1252 | `NdrInterfacePointerMemorySize` | `0xC8E30` | 129 | UnwindData |  |
| 1296 | `NdrPointerMemorySize` | `0xC8EC0` | 60 | UnwindData |  |
| 1357 | `NdrXmitOrRepAsMemorySize` | `0xC8F10` | 319 | UnwindData |  |
| 1216 | `NdrConvert` | `0xCAEB0` | 269 | UnwindData |  |
| 1347 | `NdrUserMarshalSimpleTypeConvert` | `0xCAFD0` | 90 | UnwindData |  |
| 1244 | `NdrGetSimpleTypeBufferAlignment` | `0xCB030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1245 | `NdrGetSimpleTypeBufferSize` | `0xCB050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1291 | `NdrPartialIgnoreServerInitialize` | `0xCB070` | 30 | UnwindData |  |
| 1304 | `NdrRpcSmClientAllocate` | `0xCB590` | 106 | UnwindData |  |
| 1305 | `NdrRpcSmClientFree` | `0xCB600` | 107 | UnwindData |  |
| 1306 | `NdrRpcSmSetClientToOsf` | `0xCB680` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1307 | `NdrRpcSsDefaultAllocate` | `0xCB6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1510 | `RpcSmAllocate` | `0xCB6C0` | 59 | UnwindData |  |
| 1511 | `RpcSmClientFree` | `0xCB710` | 26 | UnwindData |  |
| 1513 | `RpcSmDisableAllocate` | `0xCB730` | 28 | UnwindData |  |
| 1514 | `RpcSmEnableAllocate` | `0xCB760` | 28 | UnwindData |  |
| 1515 | `RpcSmFree` | `0xCB790` | 26 | UnwindData |  |
| 1516 | `RpcSmGetThreadHandle` | `0xCB7B0` | 54 | UnwindData |  |
| 1517 | `RpcSmSetClientAllocFree` | `0xCB7F0` | 26 | UnwindData |  |
| 1518 | `RpcSmSetThreadHandle` | `0xCB810` | 26 | UnwindData |  |
| 1519 | `RpcSmSwapClientAllocFree` | `0xCB830` | 26 | UnwindData |  |
| 1520 | `RpcSsAllocate` | `0xCB850` | 137 | UnwindData |  |
| 1524 | `RpcSsDisableAllocate` | `0xCB8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1526 | `RpcSsEnableAllocate` | `0xCB8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1527 | `RpcSsFree` | `0xCB900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1529 | `RpcSsGetThreadHandle` | `0xCB910` | 89 | UnwindData |  |
| 1530 | `RpcSsSetClientAllocFree` | `0xCB970` | 93 | UnwindData |  |
| 1531 | `RpcSsSetThreadHandle` | `0xCB9E0` | 202 | UnwindData |  |
| 1532 | `RpcSsSwapClientAllocFree` | `0xCBAB0` | 120 | UnwindData |  |
| 1005 | `I_RpcInitHttpImports` | `0xCE4E0` | 12,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `NdrMesProcEncodeDecode3` | `0xD1570` | 86 | UnwindData |  |
| 1259 | `NdrMesSimpleTypeAlignSizeAll` | `0xD15D0` | 173 | UnwindData |  |
| 1261 | `NdrMesSimpleTypeDecodeAll` | `0xD1690` | 422 | UnwindData |  |
| 1263 | `NdrMesSimpleTypeEncodeAll` | `0xD1840` | 357 | UnwindData |  |
| 1314 | `NdrServerCallNdr64` | `0xD1A40` | 62 | UnwindData |  |
| 1160 | `Ndr64AsyncServerCall64` | `0xD5010` | 9,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `NdrClientCall3` | `0xD7510` | 326 | UnwindData |  |
| 1159 | `Ndr64AsyncClientCall` | `0xD85C0` | 1,378 | UnwindData |  |
| 1161 | `Ndr64AsyncServerCallAll` | `0xDAF80` | 48,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `pfnFreeRoutines` | `0xE6B78` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `pfnMarshallRoutines` | `0xE6B80` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `pfnSizeRoutines` | `0xE6B88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `pfnUnmarshallRoutines` | `0xE6B90` | 19,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1543 | `SimpleTypeMemorySize` | `0xEB640` | 4,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `NdrTypeFlags` | `0xEC640` | 10,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1542 | `SimpleTypeBufferSize` | `0xEF020` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1541 | `SimpleTypeAlignment` | `0xEF0E0` | 0 | Indeterminate |  |
