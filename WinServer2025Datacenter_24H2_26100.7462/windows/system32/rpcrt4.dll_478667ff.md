# Binary Specification: rpcrt4.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\rpcrt4.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `478667ffc376c9725af56ede8fc56f68d4a4804b92afc2977187e185525fb393`
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
| 1317 | `NdrServerContextNewUnmarshall` | `0x1C660` | 322 | UnwindData |  |
| 1042 | `I_RpcAsyncSetHandle` | `0x216C0` | 521 | UnwindData |  |
| 1083 | `I_RpcMapWin32Status` | `0x22DB0` | 48,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1536 | `RpcStringBindingParseW` | `0x2E9C0` | 1,122 | UnwindData |  |
| 1546 | `UuidCompare` | `0x300F0` | 152 | UnwindData |  |
| 1554 | `UuidIsNil` | `0x30190` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1535 | `RpcStringBindingParseA` | `0x301F0` | 876 | UnwindData |  |
| 1533 | `RpcStringBindingComposeA` | `0x30570` | 1,253 | UnwindData |  |
| 1478 | `RpcServerInterfaceGroupCreateW` | `0x30E40` | 141 | UnwindData |  |
| 1459 | `RpcObjectSetType` | `0x32240` | 59 | UnwindData |  |
| 1136 | `I_RpcTransGetThreadEventThreadOptional` | `0x33000` | 26 | UnwindData |  |
| 1488 | `RpcServerSubscribeForNotification` | `0x35770` | 114 | UnwindData |  |
| 1492 | `RpcServerUnsubscribeForNotification` | `0x35930` | 77 | UnwindData |  |
| 1138 | `I_RpcTransServerNewConnection` | `0x35DD0` | 33 | UnwindData |  |
| 1490 | `RpcServerUnregisterIf` | `0x372F0` | 88 | UnwindData |  |
| 1486 | `RpcServerRegisterIf3` | `0x37890` | 176 | UnwindData |  |
| 1151 | `NDRCContextMarshall` | `0x3AB00` | 138 | UnwindData |  |
| 1316 | `NdrServerContextNewMarshall` | `0x3AB90` | 580 | UnwindData |  |
| 1154 | `NDRSContextMarshall2` | `0x3ADE0` | 580 | UnwindData |  |
| 1547 | `UuidCreate` | `0x3B5F0` | 80 | UnwindData |  |
| 1067 | `I_RpcExceptionFilter` | `0x3D470` | 24 | UnwindData |  |
| 1423 | `RpcExceptionFilter` | `0x3D470` | 24 | UnwindData |  |
| 1095 | `I_RpcParseSecurity` | `0x49FC0` | 520 | UnwindData |  |
| 1102 | `I_RpcSend` | `0x4A2D0` | 216 | UnwindData |  |
| 1242 | `NdrGetBuffer` | `0x4A3B0` | 729 | UnwindData |  |
| 1380 | `RpcBindingFromStringBindingW` | `0x4CDC0` | 578 | UnwindData |  |
| 1157 | `NDRSContextUnmarshall2` | `0x51090` | 77 | UnwindData |  |
| 1075 | `I_RpcGetBufferWithObject` | `0x53AD0` | 77 | UnwindData |  |
| 1088 | `I_RpcNegotiateTransferSyntax` | `0x54390` | 206 | UnwindData |  |
| 1043 | `I_RpcBCacheAllocate` | `0x54A20` | 37 | UnwindData |  |
| 1103 | `I_RpcSendReceive` | `0x54C10` | 152 | UnwindData |  |
| 1319 | `NdrServerInitialize` | `0x54CB0` | 286 | UnwindData |  |
| 1428 | `RpcImpersonateClient` | `0x54DE0` | 195 | UnwindData |  |
| 1044 | `I_RpcBCacheFree` | `0x565C0` | 23 | UnwindData |  |
| 1544 | `TowerConstruct` | `0x5AEC0` | 654 | UnwindData |  |
| 1377 | `RpcBindingCreateW` | `0x5BCA0` | 413 | UnwindData |  |
| 1375 | `RpcBindingCopy` | `0x5C7D0` | 133 | UnwindData |  |
| 1446 | `RpcMgmtSetComTimeout` | `0x5C8C0` | 105 | UnwindData |  |
| 1399 | `RpcBindingSetOption` | `0x5C930` | 215 | UnwindData |  |
| 1398 | `RpcBindingSetObject` | `0x5D090` | 82 | UnwindData |  |
| 1371 | `RpcAsyncGetCallStatus` | `0x5D290` | 172 | UnwindData |  |
| 1551 | `UuidFromStringA` | `0x5D450` | 228 | UnwindData |  |
| 1552 | `UuidFromStringW` | `0x5DEC0` | 69 | UnwindData |  |
| 1556 | `UuidToStringW` | `0x5E4A0` | 100 | UnwindData |  |
| 1534 | `RpcStringBindingComposeW` | `0x5E950` | 447 | UnwindData |  |
| 1470 | `RpcServerInqCallAttributesA` | `0x5F0C0` | 596 | UnwindData |  |
| 1538 | `RpcStringFreeW` | `0x5F320` | 62 | UnwindData |  |
| 1048 | `I_RpcBindingInqClientTokenAttributes` | `0x5F370` | 272 | UnwindData |  |
| 1471 | `RpcServerInqCallAttributesW` | `0x5F490` | 171 | UnwindData |  |
| 1056 | `I_RpcBindingInqTransportType` | `0x5F6C0` | 153 | UnwindData |  |
| 1390 | `RpcBindingInqObject` | `0x5F760` | 138 | UnwindData |  |
| 1052 | `I_RpcBindingInqLocalClientPID` | `0x5F7F0` | 124 | UnwindData |  |
| 1142 | `MesDecodeBufferHandleCreate` | `0x5F880` | 103 | UnwindData |  |
| 1145 | `MesEncodeFixedBufferHandleCreate` | `0x5FBB0` | 56 | UnwindData |  |
| 1141 | `MesBufferHandleReset` | `0x5FEF0` | 49 | UnwindData |  |
| 1396 | `RpcBindingSetAuthInfoExW` | `0x60750` | 1,312 | UnwindData |  |
| 1429 | `RpcImpersonateClient2` | `0x60CB0` | 149 | UnwindData |  |
| 1555 | `UuidToStringA` | `0x60D50` | 126 | UnwindData |  |
| 1144 | `MesEncodeDynBufferHandleCreate` | `0x60DE0` | 256 | UnwindData |  |
| 1465 | `RpcRevertToSelfEx` | `0x60EF0` | 123 | UnwindData |  |
| 1058 | `I_RpcBindingIsClientLocal` | `0x60F80` | 118 | UnwindData |  |
| 1397 | `RpcBindingSetAuthInfoW` | `0x61000` | 39 | UnwindData |  |
| 1464 | `RpcRevertToSelf` | `0x61160` | 77 | UnwindData |  |
| 1374 | `RpcBindingBind` | `0x611C0` | 115 | UnwindData |  |
| 1148 | `MesIncrementalHandleReset` | `0x61240` | 271 | UnwindData |  |
| 1109 | `I_RpcServerInqLocalConnAddress` | `0x61360` | 211 | UnwindData |  |
| 1412 | `RpcEpResolveBinding` | `0x61440` | 99 | UnwindData |  |
| 1143 | `MesDecodeIncrementalHandleCreate` | `0x614B0` | 238 | UnwindData |  |
| 1110 | `I_RpcServerInqRemoteConnAddress` | `0x615B0` | 191 | UnwindData |  |
| 1425 | `RpcGetAuthorizationContextForClient` | `0x61680` | 295 | UnwindData |  |
| 1147 | `MesHandleFree` | `0x619F0` | 320 | UnwindData |  |
| 1445 | `RpcMgmtSetCancelTimeout` | `0x61B80` | 57 | UnwindData |  |
| 1402 | `RpcBindingUnbind` | `0x61BC0` | 91 | UnwindData |  |
| 1440 | `RpcMgmtInqServerPrincNameA` | `0x61D00` | 125 | UnwindData |  |
| 1441 | `RpcMgmtInqServerPrincNameW` | `0x61D90` | 248 | UnwindData |  |
| 1384 | `RpcBindingInqAuthClientW` | `0x61E90` | 179 | UnwindData |  |
| 1383 | `RpcBindingInqAuthClientExW` | `0x61F50` | 182 | UnwindData |  |
| 1521 | `RpcSsContextLockExclusive` | `0x62190` | 114 | UnwindData |  |
| 1387 | `RpcBindingInqAuthInfoExW` | `0x62270` | 342 | UnwindData |  |
| 1401 | `RpcBindingToStringBindingW` | `0x623D0` | 108 | UnwindData |  |
| 1393 | `RpcBindingServerFromClient` | `0x62550` | 168 | UnwindData |  |
| 1117 | `I_RpcServerSubscribeForDisconnectNotification2` | `0x62600` | 398 | UnwindData |  |
| 1118 | `I_RpcServerUnsubscribeForDisconnectNotification` | `0x627A0` | 272 | UnwindData |  |
| 1009 | `I_RpcOpenClientThread` | `0x628C0` | 224 | UnwindData |  |
| 1369 | `RpcAsyncCancelCall` | `0x629B0` | 223 | UnwindData |  |
| 1427 | `RpcIfInqId` | `0x62F90` | 74 | UnwindData |  |
| 1051 | `I_RpcBindingInqDynamicEndpointW` | `0x62FE0` | 90 | UnwindData |  |
| 1400 | `RpcBindingToStringBindingA` | `0x63040` | 125 | UnwindData |  |
| 1041 | `I_RpcAsyncAbortCall` | `0x63B20` | 190 | UnwindData |  |
| 1475 | `RpcServerInterfaceGroupActivate` | `0x64480` | 54 | UnwindData |  |
| 1500 | `RpcServerUseProtseqEpExW` | `0x64910` | 41 | UnwindData |  |
| 1501 | `RpcServerUseProtseqEpW` | `0x64940` | 87 | UnwindData |  |
| 1122 | `I_RpcServerUseProtseqEp2W` | `0x649A0` | 171 | UnwindData |  |
| 1476 | `RpcServerInterfaceGroupClose` | `0x65DA0` | 44 | UnwindData |  |
| 1468 | `RpcServerInqBindings` | `0x65FF0` | 61 | UnwindData |  |
| 1503 | `RpcServerUseProtseqExW` | `0x66970` | 31 | UnwindData |  |
| 1508 | `RpcServerUseProtseqW` | `0x669A0` | 140 | UnwindData |  |
| 1120 | `I_RpcServerUseProtseq2W` | `0x66A40` | 195 | UnwindData |  |
| 1469 | `RpcServerInqBindingsEx` | `0x66DB0` | 71 | UnwindData |  |
| 1198 | `NdrConformantStringUnmarshall` | `0x68AD0` | 519 | UnwindData |  |
| 1353 | `NdrVaryingArrayUnmarshall` | `0x69150` | 606 | UnwindData |  |
| 1352 | `NdrVaryingArrayMemorySize` | `0x693C0` | 355 | UnwindData |  |
| 1170 | `NdrByteCountPointerUnmarshall` | `0x698B0` | 520 | UnwindData |  |
| 1327 | `NdrSimpleStructMemorySize` | `0x6A280` | 156 | UnwindData |  |
| 1346 | `NdrUserMarshalMemorySize` | `0x6A330` | 567 | UnwindData |  |
| 1282 | `NdrNonEncapsulatedUnionMemorySize` | `0x6A570` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1208 | `NdrConformantVaryingArrayUnmarshall` | `0x6A670` | 256 | UnwindData |  |
| 1202 | `NdrConformantStructMemorySize` | `0x6AA80` | 364 | UnwindData |  |
| 1038 | `IUnknown_QueryInterface_Proxy` | `0x6B5A0` | 99 | UnwindData |  |
| 1027 | `CStdStubBuffer_Disconnect` | `0x6B610` | 56 | UnwindData |  |
| 1224 | `NdrDllCanUnloadNow` | `0x6B650` | 76 | UnwindData |  |
| 1185 | `NdrComplexStructBufferSize` | `0x6B6B0` | 66 | UnwindData |  |
| 1188 | `NdrComplexStructMemorySize` | `0x6C0F0` | 53 | UnwindData |  |
| 1039 | `IUnknown_Release_Proxy` | `0x6CBE0` | 63 | UnwindData |  |
| 1037 | `IUnknown_AddRef_Proxy` | `0x6CC30` | 63 | UnwindData |  |
| 1022 | `CStdStubBuffer_AddRef` | `0x6CC80` | 62 | UnwindData |  |
| 1028 | `CStdStubBuffer_Invoke` | `0x6CCD0` | 99 | UnwindData |  |
| 1172 | `NdrCStdStubBuffer_Release` | `0x6CD40` | 78 | UnwindData |  |
| 1225 | `NdrDllGetClassObject` | `0x6CDA0` | 138 | UnwindData |  |
| 1286 | `NdrOleAllocate` | `0x6CE30` | 66 | UnwindData |  |
| 1287 | `NdrOleFree` | `0x6CE80` | 59 | UnwindData |  |
| 1031 | `CreateProxyFromTypeInfo` | `0x6D160` | 125 | UnwindData |  |
| 1171 | `NdrCStdStubBuffer2_Release` | `0x6D1F0` | 78 | UnwindData |  |
| 1293 | `NdrPointerBufferSize` | `0x6D2B0` | 514 | UnwindData |  |
| 1279 | `NdrNonEncapsulatedUnionBufferSize` | `0x6D770` | 590 | UnwindData |  |
| 1032 | `CreateStubFromTypeInfo` | `0x6DCC0` | 115 | UnwindData |  |
| 1030 | `CStdStubBuffer_QueryInterface` | `0x6DD40` | 99 | UnwindData |  |
| 1333 | `NdrStubForwardingFunction` | `0x6DDB0` | 106 | UnwindData |  |
| 1026 | `CStdStubBuffer_DebugServerRelease` | `0x6E040` | 71 | UnwindData |  |
| 1025 | `CStdStubBuffer_DebugServerQueryInterface` | `0x6E090` | 83 | UnwindData |  |
| 1367 | `NdrpVarVtOfTypeDesc` | `0x6E0F0` | 102 | UnwindData |  |
| 1365 | `NdrpReleaseTypeFormatString` | `0x6E160` | 76 | UnwindData |  |
| 1363 | `NdrpGetTypeGenCookie` | `0x6E1C0` | 76 | UnwindData |  |
| 1361 | `NdrpGetProcFormatString` | `0x6E220` | 140 | UnwindData |  |
| 1362 | `NdrpGetTypeFormatString` | `0x6E2C0` | 102 | UnwindData |  |
| 1226 | `NdrDllRegisterProxy` | `0x6E330` | 102 | UnwindData |  |
| 1266 | `NdrMesTypeAlignSize3` | `0x6FCE0` | 350 | UnwindData |  |
| 1272 | `NdrMesTypeEncode3` | `0x6FE50` | 350 | UnwindData |  |
| 1269 | `NdrMesTypeDecode3` | `0x70380` | 423 | UnwindData |  |
| 1238 | `NdrFreeBuffer` | `0x70950` | 161 | UnwindData |  |
| 1239 | `NdrFullPointerXlatFree` | `0x713F0` | 91 | UnwindData |  |
| 1321 | `NdrServerInitializeNew` | `0x7B110` | 428 | UnwindData |  |
| 1098 | `I_RpcReceive` | `0x7B400` | 206 | UnwindData |  |
| 1311 | `NdrSendReceive` | `0x7B510` | 247 | UnwindData |  |
| 1100 | `I_RpcRequestMutex` | `0x7B610` | 109 | UnwindData |  |
| 1074 | `I_RpcGetBuffer` | `0x7B6E0` | 636 | UnwindData |  |
| 1483 | `RpcServerRegisterAuthInfoW` | `0x7BC10` | 112 | UnwindData |  |
| 1473 | `RpcServerInqDefaultPrincNameW` | `0x7BD90` | 177 | UnwindData |  |
| 1417 | `RpcErrorGetNextRecord` | `0x7DE60` | 75 | UnwindData |  |
| 1297 | `NdrPointerUnmarshall` | `0x7EC50` | 1,466 | UnwindData |  |
| 1330 | `NdrSimpleTypeUnmarshall` | `0x7FC80` | 749 | UnwindData |  |
| 1348 | `NdrUserMarshalUnmarshall` | `0x81B70` | 900 | UnwindData |  |
| 1303 | `NdrRangeUnmarshall` | `0x82BC0` | 528 | UnwindData |  |
| 1351 | `NdrVaryingArrayMarshall` | `0x83A60` | 307 | UnwindData |  |
| 1349 | `NdrVaryingArrayBufferSize` | `0x83BA0` | 250 | UnwindData |  |
| 1206 | `NdrConformantVaryingArrayMarshall` | `0x83CA0` | 41 | UnwindData |  |
| 1192 | `NdrConformantArrayMarshall` | `0x85630` | 240 | UnwindData |  |
| 1329 | `NdrSimpleTypeMarshall` | `0x85730` | 49 | UnwindData |  |
| 1247 | `NdrGetTypeFlags` | `0x85960` | 1,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1341 | `NdrTypeUnmarshall` | `0x86040` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `NdrConformantStringBufferSize` | `0x862D0` | 402 | UnwindData |  |
| 1248 | `NdrGetUserMarshalInfo` | `0x86470` | 216 | UnwindData |  |
| 1273 | `NdrMesTypeFree2` | `0x86750` | 362 | UnwindData |  |
| 1219 | `NdrCorrelationInitialize` | `0x869E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `NdrConformantStringMarshall` | `0x86A30` | 404 | UnwindData |  |
| 1343 | `NdrUserMarshalBufferSize` | `0x86BD0` | 770 | UnwindData |  |
| 1345 | `NdrUserMarshalMarshall` | `0x87100` | 362 | UnwindData |  |
| 1512 | `RpcSmDestroyClientContext` | `0x87950` | 26 | UnwindData |  |
| 1523 | `RpcSsDestroyClientContext` | `0x87970` | 112 | UnwindData |  |
| 1150 | `NDRCContextBinding` | `0x87B40` | 45 | UnwindData |  |
| 1199 | `NdrConformantStructBufferSize` | `0x87E10` | 314 | UnwindData |  |
| 1070 | `I_RpcFreeBuffer` | `0x87FF0` | 132 | UnwindData |  |
| 1001 | `I_RpcBindingInqCurrentModifiedId` | `0x884F0` | 131 | UnwindData |  |
| 1435 | `RpcMgmtEpEltInqNextW` | `0x88660` | 93 | UnwindData |  |
| 1434 | `RpcMgmtEpEltInqNextA` | `0x886D0` | 1,531 | UnwindData |  |
| 1545 | `TowerExplode` | `0x88CE0` | 889 | UnwindData |  |
| 1201 | `NdrConformantStructMarshall` | `0x899F0` | 301 | UnwindData |  |
| 1179 | `NdrClientInitializeNew` | `0x89CB0` | 271 | UnwindData |  |
| 1073 | `I_RpcFreeSystemHandleCollection` | `0x89E30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `NdrTypeFree` | `0x89E60` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `NdrClientInitialize` | `0x8A070` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `NdrServerCallAll` | `0x8A1B0` | 66 | UnwindData |  |
| 1550 | `UuidEqual` | `0x8AA50` | 91 | UnwindData |  |
| 1218 | `NdrCorrelationFree` | `0x8AB40` | 6,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1169 | `NdrByteCountPointerMarshall` | `0x8C4F0` | 172 | UnwindData |  |
| 1220 | `NdrCorrelationPass` | `0x8DFE0` | 102 | UnwindData |  |
| 1094 | `I_RpcOpenClientProcess` | `0x8E6E0` | 248 | UnwindData |  |
| 1233 | `NdrFixedArrayBufferSize` | `0x8E820` | 121 | UnwindData |  |
| 1235 | `NdrFixedArrayMarshall` | `0x8EAC0` | 201 | UnwindData |  |
| 1280 | `NdrNonEncapsulatedUnionFree` | `0x8F370` | 263 | UnwindData |  |
| 1237 | `NdrFixedArrayUnmarshall` | `0x8F4F0` | 326 | UnwindData |  |
| 1236 | `NdrFixedArrayMemorySize` | `0x8F950` | 178 | UnwindData |  |
| 1045 | `I_RpcBindingCopy` | `0x8FFE0` | 105 | UnwindData |  |
| 1214 | `NdrContextHandleInitialize` | `0x90190` | 192 | UnwindData |  |
| 1344 | `NdrUserMarshalFree` | `0x91B00` | 166 | UnwindData |  |
| 1197 | `NdrConformantStringMemorySize` | `0x92060` | 97 | UnwindData |  |
| 1467 | `RpcServerInqBindingHandle` | `0x92200` | 47 | UnwindData |  |
| 1414 | `RpcErrorAddRecord` | `0x932B0` | 246 | UnwindData |  |
| 1422 | `RpcErrorStartEnumeration` | `0x93540` | 80 | UnwindData |  |
| 1080 | `I_RpcGetSystemHandle` | `0x936C0` | 90 | UnwindData |  |
| 1069 | `I_RpcFree` | `0x937D0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1308 | `NdrRpcSsDefaultFree` | `0x937D0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `NdrConformantArrayMemorySize` | `0x938D0` | 66 | UnwindData |  |
| 1489 | `RpcServerTestCancel` | `0x93A60` | 86 | UnwindData |  |
| 1424 | `RpcFreeAuthorizationContext` | `0x93B90` | 58 | UnwindData |  |
| 1167 | `NdrByteCountPointerBufferSize` | `0x93BD0` | 153 | UnwindData |  |
| 1205 | `NdrConformantVaryingArrayFree` | `0x93D40` | 113 | UnwindData |  |
| 1125 | `I_RpcSetSystemHandle` | `0x94080` | 50 | UnwindData |  |
| 1131 | `I_RpcTransConnectionReallocPacket` | `0x942F0` | 112 | UnwindData |  |
| 1107 | `I_RpcServerGetAssociationID` | `0x946F0` | 85 | UnwindData |  |
| 1234 | `NdrFixedArrayFree` | `0x94880` | 8,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1274 | `NdrMesTypeFree3` | `0x96940` | 333 | UnwindData |  |
| 1204 | `NdrConformantVaryingArrayBufferSize` | `0x96AA0` | 56 | UnwindData |  |
| 1553 | `UuidHash` | `0x96C80` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1168 | `NdrByteCountPointerFree` | `0x971A0` | 51 | UnwindData |  |
| 1298 | `NdrProxyErrorHandler` | `0x977C0` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `NdrServerInitializeMarshall` | `0x97BD0` | 2,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1072 | `I_RpcFreeSystemHandle` | `0x986B0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1549 | `UuidCreateSequential` | `0x987C0` | 292 | UnwindData |  |
| 1254 | `NdrMapCommAndFaultStatus` | `0x98ED0` | 115 | UnwindData |  |
| 1063 | `I_RpcClearMutex` | `0x9A7F0` | 1,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1373 | `RpcAsyncRegisterInfo` | `0x9ADB0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1416 | `RpcErrorEndEnumeration` | `0x9AF50` | 53 | UnwindData |  |
| 1350 | `NdrVaryingArrayFree` | `0x9AF90` | 104 | UnwindData |  |
| 1452 | `RpcNetworkInqProtseqsW` | `0x9B480` | 44 | UnwindData |  |
| 1454 | `RpcNetworkIsProtseqValidW` | `0x9B4C0` | 44 | UnwindData |  |
| 1461 | `RpcProtseqVectorFreeW` | `0x9B790` | 116 | UnwindData |  |
| 1309 | `NdrRpcSsDisableAllocate` | `0x9BCC0` | 51 | UnwindData |  |
| 1379 | `RpcBindingFromStringBindingA` | `0x9BF20` | 144 | UnwindData |  |
| 1537 | `RpcStringFreeA` | `0x9BFC0` | 2,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `I_RpcInitNdrImports` | `0x9C8E0` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | *Ordinal Only* | `0x9CDF0` | 68 | UnwindData |  |
| 1146 | `MesEncodeIncrementalHandleCreate` | `0x9CF30` | 161 | UnwindData |  |
| 1135 | `I_RpcTransGetThreadEvent` | `0x9D580` | 19 | UnwindData |  |
| 1443 | `RpcMgmtIsServerListening` | `0x9D600` | 136 | UnwindData |  |
| 1403 | `RpcBindingVectorFree` | `0x9DA40` | 120 | UnwindData |  |
| 1008 | `I_RpcMgmtQueryDedicatedThreadPool` | `0x9DB90` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1528 | `RpcSsGetContextBinding` | `0x9DC80` | 55 | UnwindData |  |
| 1481 | `RpcServerListen` | `0x9E530` | 90 | UnwindData |  |
| 1101 | `I_RpcSNCHOption` | `0x9E8E0` | 94 | UnwindData |  |
| 1129 | `I_RpcTransConnectionAllocatePacket` | `0x9EB90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1082 | `I_RpcLogEvent` | `0x9EBA0` | 2,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1447 | `RpcMgmtSetServerStackSize` | `0x9F530` | 87 | UnwindData |  |
| 1130 | `I_RpcTransConnectionFreePacket` | `0x9FB30` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1081 | `I_RpcIfInqTransferSyntaxes` | `0xA0060` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1276 | `NdrNonConformantStringMarshall` | `0xA01D0` | 242 | UnwindData |  |
| 1128 | `I_RpcSystemHandleTypeSpecificWork` | `0xA02D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1278 | `NdrNonConformantStringUnmarshall` | `0xA0310` | 424 | UnwindData |  |
| 1277 | `NdrNonConformantStringMemorySize` | `0xA04C0` | 274 | UnwindData |  |
| 1124 | `I_RpcSetDCOMAppId` | `0xA05E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `NdrConvert2` | `0xA0600` | 194 | UnwindData |  |
| 1275 | `NdrNonConformantStringBufferSize` | `0xA09B0` | 260 | UnwindData |  |
| 1491 | `RpcServerUnregisterIfEx` | `0xA0AC0` | 120 | UnwindData |  |
| 1246 | `NdrGetSimpleTypeMemorySize` | `0xA1280` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1487 | `RpcServerRegisterIfEx` | `0xA1420` | 156 | UnwindData |  |
| 1479 | `RpcServerInterfaceGroupDeactivate` | `0xA1530` | 73 | UnwindData |  |
| 1498 | `RpcServerUseProtseqEpA` | `0xA16E0` | 87 | UnwindData |  |
| 1121 | `I_RpcServerUseProtseqEp2A` | `0xA1740` | 613 | UnwindData |  |
| 1060 | `I_RpcBindingSetPrivateOption` | `0xA1CE0` | 104 | UnwindData |  |
| 1411 | `RpcEpRegisterW` | `0xA2390` | 26 | UnwindData |  |
| 1432 | `RpcMgmtEpEltInqBegin` | `0xA2400` | 677 | UnwindData |  |
| 1394 | `RpcBindingSetAuthInfoA` | `0xA30A0` | 39 | UnwindData |  |
| 1395 | `RpcBindingSetAuthInfoExA` | `0xA30D0` | 276 | UnwindData |  |
| 1085 | `I_RpcMgmtEnableDedicatedThreadPool` | `0xA3240` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `NdrContextHandleSize` | `0xA3310` | 75 | UnwindData |  |
| 1449 | `RpcMgmtStopServerListening` | `0xA3370` | 142 | UnwindData |  |
| 1485 | `RpcServerRegisterIf2` | `0xA3770` | 157 | UnwindData |  |
| 1433 | `RpcMgmtEpEltInqDone` | `0xA3C20` | 162 | UnwindData |  |
| 1484 | `RpcServerRegisterIf` | `0xA5280` | 121 | UnwindData |  |
| 1413 | `RpcEpUnregister` | `0xA5300` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `I_RpcServerDisableExceptionFilter` | `0xA53B0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1548 | `UuidCreateNil` | `0xA5550` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1431 | `RpcMgmtEnableIdleCleanup` | `0xA5EA0` | 40 | UnwindData |  |
| 1076 | `I_RpcGetCurrentCallHandle` | `0xA6200` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1482 | `RpcServerRegisterAuthInfoA` | `0xA6690` | 182 | UnwindData |  |
| 1381 | `RpcBindingInqAuthClientA` | `0xA7800` | 40 | UnwindData |  |
| 1137 | `I_RpcTransIoCancelled` | `0xA7830` | 51 | UnwindData |  |
| 1450 | `RpcMgmtWaitServerListen` | `0xA7AA0` | 33 | UnwindData |  |
| 1253 | `NdrInterfacePointerUnmarshall` | `0xA8B40` | 156 | UnwindData |  |
| 1207 | `NdrConformantVaryingArrayMemorySize` | `0xA8BF0` | 66 | UnwindData |  |
| 1046 | `I_RpcBindingCreateNP` | `0xA90F0` | 611 | UnwindData |  |
| 1228 | `NdrEncapsulatedUnionBufferSize` | `0xA9430` | 150 | UnwindData |  |
| 1230 | `NdrEncapsulatedUnionMarshall` | `0xA94D0` | 152 | UnwindData |  |
| 1322 | `NdrServerInitializePartial` | `0xA9570` | 104 | UnwindData |  |
| 1251 | `NdrInterfacePointerMarshall` | `0xA9800` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `NdrInterfacePointerBufferSize` | `0xA99C0` | 144 | UnwindData |  |
| 1231 | `NdrEncapsulatedUnionMemorySize` | `0xA9E00` | 83 | UnwindData |  |
| 1086 | `I_RpcNDRCGetWireRepresentation` | `0xA9F10` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1382 | `RpcBindingInqAuthClientExA` | `0xAA0E0` | 171 | UnwindData |  |
| 1097 | `I_RpcReallocPipeBuffer` | `0xAA620` | 73 | UnwindData |  |
| 1310 | `NdrRpcSsEnableAllocate` | `0xAA670` | 85 | UnwindData |  |
| 1418 | `RpcErrorGetNumberOfRecords` | `0xAB740` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1420 | `RpcErrorResetEnumeration` | `0xAB770` | 11,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1050 | `I_RpcBindingInqDynamicEndpointA` | `0xAE2B0` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1090 | `I_RpcNsBindingSetEntryNameA` | `0xAE2B0` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1116 | `I_RpcServerSubscribeForDisconnectNotification` | `0xAE2B0` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1132 | `I_RpcTransDatagramAllocate` | `0xAE2B0` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1133 | `I_RpcTransDatagramAllocate2` | `0xAE2B0` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1134 | `I_RpcTransDatagramFree` | `0xAE2B0` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `I_RpcFixTransferSyntax` | `0xAF200` | 144 | UnwindData |  |
| 1064 | `I_RpcCompleteAndFree` | `0xAF2A0` | 170 | UnwindData |  |
| 1096 | `I_RpcPauseExecution` | `0xAF350` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `I_RpcFwThisIsTheManager` | `0xAF420` | 35 | UnwindData |  |
| 1004 | `I_RpcInitFwImports` | `0xAF4A0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `I_RpcInitImports` | `0xAF530` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `I_RpcServerTurnOnOffKeepalives` | `0xAF5F0` | 157 | UnwindData |  |
| 1059 | `I_RpcBindingIsServerLocal` | `0xAF6A0` | 93 | UnwindData |  |
| 1077 | `I_RpcGetDefaultSD` | `0xAF710` | 49 | UnwindData |  |
| 1108 | `I_RpcServerInqAddressChangeFn` | `0xAF750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1112 | `I_RpcServerIsClientDisconnected` | `0xAF760` | 115 | UnwindData |  |
| 1113 | `I_RpcServerRegisterForwardFunction` | `0xAF7E0` | 50 | UnwindData |  |
| 1114 | `I_RpcServerSetAddressChangeFn` | `0xAF820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1115 | `I_RpcServerStartService` | `0xAF840` | 110 | UnwindData |  |
| 1123 | `I_RpcSessionStrictContextHandle` | `0xAF8C0` | 44 | UnwindData |  |
| 1426 | `RpcIfIdVectorFree` | `0xAF900` | 92 | UnwindData |  |
| 1430 | `RpcImpersonateClientContainer` | `0xAF970` | 141 | UnwindData |  |
| 1439 | `RpcMgmtInqIfIds` | `0xAFA10` | 175 | UnwindData |  |
| 1442 | `RpcMgmtInqStats` | `0xAFAD0` | 306 | UnwindData |  |
| 1448 | `RpcMgmtStatsVectorFree` | `0xAFC10` | 58 | UnwindData |  |
| 1457 | `RpcObjectInqType` | `0xAFC50` | 103 | UnwindData |  |
| 1458 | `RpcObjectSetInqFn` | `0xAFCC0` | 43 | UnwindData |  |
| 1463 | `RpcRevertContainerImpersonation` | `0xAFD00` | 67 | UnwindData |  |
| 1466 | `RpcServerCompleteSecurityCallback` | `0xAFD50` | 83 | UnwindData |  |
| 1472 | `RpcServerInqDefaultPrincNameA` | `0xAFDB0` | 87 | UnwindData |  |
| 1474 | `RpcServerInqIf` | `0xAFE10` | 146 | UnwindData |  |
| 1477 | `RpcServerInterfaceGroupCreateA` | `0xAFEB0` | 874 | UnwindData |  |
| 1480 | `RpcServerInterfaceGroupInqBindings` | `0xB0220` | 67 | UnwindData |  |
| 1493 | `RpcServerUseAllProtseqs` | `0xB0270` | 37 | UnwindData |  |
| 1494 | `RpcServerUseAllProtseqsEx` | `0xB02A0` | 422 | UnwindData |  |
| 1495 | `RpcServerUseAllProtseqsIf` | `0xB0450` | 66 | UnwindData |  |
| 1496 | `RpcServerUseAllProtseqsIfEx` | `0xB04A0` | 197 | UnwindData |  |
| 1506 | `RpcServerUseProtseqIfExW` | `0xB0570` | 322 | UnwindData |  |
| 1507 | `RpcServerUseProtseqIfW` | `0xB06C0` | 71 | UnwindData |  |
| 1011 | `I_RpcVerifierCorruptionExpected` | `0xB0710` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `I_RpcEnableWmiTrace` | `0xB0A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `RpcCertMatchPrincipalName` | `0xB0A30` | 90 | UnwindData |  |
| 1062 | `I_RpcCertProcessAndProvision` | `0xB0AE0` | 124 | UnwindData |  |
| 1407 | `RpcCertGeneratePrincipalNameW` | `0xB0C10` | 101 | UnwindData |  |
| 1033 | `DceErrorInqTextA` | `0xB0C80` | 126 | UnwindData |  |
| 1034 | `DceErrorInqTextW` | `0xB0D10` | 133 | UnwindData |  |
| 1437 | `RpcMgmtInqComTimeout` | `0xB0DA0` | 77 | UnwindData |  |
| 1054 | `I_RpcBindingInqSecurityContext` | `0xB0E90` | 88 | UnwindData |  |
| 1055 | `I_RpcBindingInqSecurityContextKeyInfo` | `0xB0EF0` | 128 | UnwindData |  |
| 1084 | `I_RpcMarshalBindingHandleAndInterfaceForNDF` | `0xB0F80` | 78 | UnwindData |  |
| 1091 | `I_RpcNsBindingSetEntryNameW` | `0xB0FE0` | 78 | UnwindData |  |
| 1092 | `I_RpcNsInterfaceExported` | `0xB0FE0` | 78 | UnwindData |  |
| 1093 | `I_RpcNsInterfaceUnexported` | `0xB0FE0` | 78 | UnwindData |  |
| 1456 | `RpcNsBindingInqEntryNameW` | `0xB0FE0` | 78 | UnwindData |  |
| 1139 | `I_RpcTurnOnEEInfoPropagation` | `0xB1040` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1388 | `RpcBindingInqAuthInfoW` | `0xB1100` | 120 | UnwindData |  |
| 1392 | `RpcBindingReset` | `0xB1180` | 80 | UnwindData |  |
| 1284 | `NdrNsGetBuffer` | `0xB3F30` | 15 | UnwindData |  |
| 1285 | `NdrNsSendReceive` | `0xB3F30` | 15 | UnwindData |  |
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
| 1104 | `I_RpcServerAllocateIpPort` | `0xBC1E0` | 377 | UnwindData |  |
| 1119 | `I_RpcServerUseProtseq2A` | `0xBC360` | 434 | UnwindData |  |
| 1376 | `RpcBindingCreateA` | `0xBC520` | 807 | UnwindData |  |
| 1385 | `RpcBindingInqAuthInfoA` | `0xBC850` | 46 | UnwindData |  |
| 1386 | `RpcBindingInqAuthInfoExA` | `0xBC890` | 168 | UnwindData |  |
| 1406 | `RpcCertGeneratePrincipalNameA` | `0xBC940` | 87 | UnwindData |  |
| 1451 | `RpcNetworkInqProtseqsA` | `0xBC9A0` | 133 | UnwindData |  |
| 1453 | `RpcNetworkIsProtseqValidA` | `0xBCA30` | 357 | UnwindData |  |
| 1455 | `RpcNsBindingInqEntryNameA` | `0xBCBA0` | 115 | UnwindData |  |
| 1460 | `RpcProtseqVectorFreeA` | `0xBCC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1497 | `RpcServerUseProtseqA` | `0xBCC30` | 82 | UnwindData |  |
| 1499 | `RpcServerUseProtseqEpExA` | `0xBCC90` | 41 | UnwindData |  |
| 1502 | `RpcServerUseProtseqExA` | `0xBCCC0` | 31 | UnwindData |  |
| 1504 | `RpcServerUseProtseqIfA` | `0xBCCF0` | 71 | UnwindData |  |
| 1505 | `RpcServerUseProtseqIfExA` | `0xBCD40` | 392 | UnwindData |  |
| 1140 | `I_UuidCreate` | `0xBCED0` | 25 | UnwindData |  |
| 1408 | `RpcEpRegisterA` | `0xBCEF0` | 26 | UnwindData |  |
| 1409 | `RpcEpRegisterNoReplaceA` | `0xBCF10` | 228 | UnwindData |  |
| 1410 | `RpcEpRegisterNoReplaceW` | `0xBD000` | 137 | UnwindData |  |
| 1436 | `RpcMgmtEpUnregister` | `0xBD090` | 15 | UnwindData |  |
| 1444 | `RpcMgmtSetAuthorizationFn` | `0xBD0B0` | 29,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1152 | `NDRCContextUnmarshall` | `0xC4260` | 28 | UnwindData |  |
| 1087 | `I_RpcNDRSContextEmergencyCleanup` | `0xC43E0` | 24 | UnwindData |  |
| 1126 | `I_RpcSsDontSerializeContext` | `0xC4400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1153 | `NDRSContextMarshall` | `0xC4420` | 74 | UnwindData |  |
| 1155 | `NDRSContextMarshallEx` | `0xC4470` | 26 | UnwindData |  |
| 1156 | `NDRSContextUnmarshall` | `0xC4490` | 54 | UnwindData |  |
| 1158 | `NDRSContextUnmarshallEx` | `0xC44D0` | 23 | UnwindData |  |
| 1522 | `RpcSsContextLockShared` | `0xC44F0` | 118 | UnwindData |  |
| 1013 | `NdrFullPointerInsertRefId` | `0xC4570` | 165 | UnwindData |  |
| 1014 | `NdrFullPointerQueryPointer` | `0xC4620` | 452 | UnwindData |  |
| 1015 | `NdrFullPointerQueryRefId` | `0xC47F0` | 270 | UnwindData |  |
| 1200 | `NdrConformantStructFree` | `0xC4AF0` | 97 | UnwindData |  |
| 1210 | `NdrConformantVaryingStructFree` | `0xC4B60` | 153 | UnwindData |  |
| 1229 | `NdrEncapsulatedUnionFree` | `0xC4C00` | 139 | UnwindData |  |
| 1250 | `NdrInterfacePointerFree` | `0xC4CA0` | 34 | UnwindData |  |
| 1325 | `NdrSimpleStructFree` | `0xC4CD0` | 25 | UnwindData |  |
| 1355 | `NdrXmitOrRepAsFree` | `0xC4CF0` | 56 | UnwindData |  |
| 1176 | `NdrClientContextMarshall` | `0xC4D50` | 69 | UnwindData |  |
| 1211 | `NdrConformantVaryingStructMarshall` | `0xC4DA0` | 323 | UnwindData |  |
| 1290 | `NdrPartialIgnoreClientMarshall` | `0xC4EF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1315 | `NdrServerContextMarshall` | `0xC4F20` | 62 | UnwindData |  |
| 1356 | `NdrXmitOrRepAsMarshall` | `0xC4F70` | 383 | UnwindData |  |
| 1209 | `NdrConformantVaryingStructBufferSize` | `0xC5220` | 268 | UnwindData |  |
| 1289 | `NdrPartialIgnoreClientBufferSize` | `0xC5340` | 42 | UnwindData |  |
| 1354 | `NdrXmitOrRepAsBufferSize` | `0xC5370` | 378 | UnwindData |  |
| 1177 | `NdrClientContextUnmarshall` | `0xC5E40` | 86 | UnwindData |  |
| 1213 | `NdrConformantVaryingStructUnmarshall` | `0xC5EA0` | 1,468 | UnwindData |  |
| 1232 | `NdrEncapsulatedUnionUnmarshall` | `0xC6470` | 238 | UnwindData |  |
| 1292 | `NdrPartialIgnoreServerUnmarshall` | `0xC6570` | 72 | UnwindData |  |
| 1318 | `NdrServerContextUnmarshall` | `0xC65C0` | 100 | UnwindData |  |
| 1358 | `NdrXmitOrRepAsUnmarshall` | `0xC6630` | 759 | UnwindData |  |
| 1023 | `CStdStubBuffer_Connect` | `0xC6930` | 83 | UnwindData |  |
| 1024 | `CStdStubBuffer_CountRefs` | `0xC6990` | 63 | UnwindData |  |
| 1029 | `CStdStubBuffer_IsIIDSupported` | `0xC69E0` | 75 | UnwindData |  |
| 1035 | `DllGetClassObject` | `0xC6A40` | 99 | UnwindData |  |
| 1036 | `DllRegisterServer` | `0xC6AB0` | 63 | UnwindData |  |
| 1162 | `Ndr64DcomAsyncClientCall` | `0xC6B00` | 112 | UnwindData |  |
| 1163 | `Ndr64DcomAsyncStubCall` | `0xC6B80` | 118 | UnwindData |  |
| 1221 | `NdrCreateServerInterfaceFromStub` | `0xC6C00` | 74 | UnwindData |  |
| 1222 | `NdrDcomAsyncClientCall` | `0xC6C50` | 114 | UnwindData |  |
| 1223 | `NdrDcomAsyncStubCall` | `0xC6CD0` | 118 | UnwindData |  |
| 1227 | `NdrDllUnregisterProxy` | `0xC6D50` | 102 | UnwindData |  |
| 1241 | `NdrGetBaseInterfaceFromStub` | `0xC6DC0` | 102 | UnwindData |  |
| 1243 | `NdrGetDcomProtocolVersion` | `0xC6E30` | 86 | UnwindData |  |
| 1299 | `NdrProxyFreeBuffer` | `0xC6E90` | 71 | UnwindData |  |
| 1300 | `NdrProxyGetBuffer` | `0xC6EE0` | 71 | UnwindData |  |
| 1301 | `NdrProxyInitialize` | `0xC6F30` | 119 | UnwindData |  |
| 1302 | `NdrProxySendReceive` | `0xC6FB0` | 71 | UnwindData |  |
| 1334 | `NdrStubGetBuffer` | `0xC7000` | 87 | UnwindData |  |
| 1335 | `NdrStubInitialize` | `0xC7060` | 111 | UnwindData |  |
| 1336 | `NdrStubInitializeMarshall` | `0xC70E0` | 96 | UnwindData |  |
| 1359 | `NdrpCreateProxy` | `0xC7150` | 118 | UnwindData |  |
| 1360 | `NdrpCreateStub` | `0xC71D0` | 102 | UnwindData |  |
| 1366 | `NdrpReleaseTypeGenCookie` | `0xC7240` | 76 | UnwindData |  |
| 1149 | `MesInqProcEncodingId` | `0xC7620` | 278 | UnwindData |  |
| 1255 | `NdrMesProcEncodeDecode` | `0xC7740` | 1,229 | UnwindData |  |
| 1256 | `NdrMesProcEncodeDecode2` | `0xC7C20` | 677 | UnwindData |  |
| 1258 | `NdrMesSimpleTypeAlignSize` | `0xC7ED0` | 90 | UnwindData |  |
| 1260 | `NdrMesSimpleTypeDecode` | `0xC7F30` | 306 | UnwindData |  |
| 1262 | `NdrMesSimpleTypeEncode` | `0xC8070` | 217 | UnwindData |  |
| 1164 | `NdrAllocate` | `0xC8610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `NdrServerInitializeUnmarshall` | `0xC8620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1540 | `RpcUserFree` | `0xC8640` | 80 | UnwindData |  |
| 1212 | `NdrConformantVaryingStructMemorySize` | `0xC8BE0` | 379 | UnwindData |  |
| 1252 | `NdrInterfacePointerMemorySize` | `0xC8DF0` | 129 | UnwindData |  |
| 1296 | `NdrPointerMemorySize` | `0xC8E80` | 60 | UnwindData |  |
| 1357 | `NdrXmitOrRepAsMemorySize` | `0xC8ED0` | 319 | UnwindData |  |
| 1216 | `NdrConvert` | `0xCAE70` | 269 | UnwindData |  |
| 1347 | `NdrUserMarshalSimpleTypeConvert` | `0xCAF90` | 90 | UnwindData |  |
| 1244 | `NdrGetSimpleTypeBufferAlignment` | `0xCAFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1245 | `NdrGetSimpleTypeBufferSize` | `0xCB010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1291 | `NdrPartialIgnoreServerInitialize` | `0xCB030` | 30 | UnwindData |  |
| 1304 | `NdrRpcSmClientAllocate` | `0xCB550` | 106 | UnwindData |  |
| 1305 | `NdrRpcSmClientFree` | `0xCB5C0` | 107 | UnwindData |  |
| 1306 | `NdrRpcSmSetClientToOsf` | `0xCB640` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1307 | `NdrRpcSsDefaultAllocate` | `0xCB670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1510 | `RpcSmAllocate` | `0xCB680` | 59 | UnwindData |  |
| 1511 | `RpcSmClientFree` | `0xCB6D0` | 26 | UnwindData |  |
| 1513 | `RpcSmDisableAllocate` | `0xCB6F0` | 28 | UnwindData |  |
| 1514 | `RpcSmEnableAllocate` | `0xCB720` | 28 | UnwindData |  |
| 1515 | `RpcSmFree` | `0xCB750` | 26 | UnwindData |  |
| 1516 | `RpcSmGetThreadHandle` | `0xCB770` | 54 | UnwindData |  |
| 1517 | `RpcSmSetClientAllocFree` | `0xCB7B0` | 26 | UnwindData |  |
| 1518 | `RpcSmSetThreadHandle` | `0xCB7D0` | 26 | UnwindData |  |
| 1519 | `RpcSmSwapClientAllocFree` | `0xCB7F0` | 26 | UnwindData |  |
| 1520 | `RpcSsAllocate` | `0xCB810` | 137 | UnwindData |  |
| 1524 | `RpcSsDisableAllocate` | `0xCB8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1526 | `RpcSsEnableAllocate` | `0xCB8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1527 | `RpcSsFree` | `0xCB8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1529 | `RpcSsGetThreadHandle` | `0xCB8D0` | 89 | UnwindData |  |
| 1530 | `RpcSsSetClientAllocFree` | `0xCB930` | 93 | UnwindData |  |
| 1531 | `RpcSsSetThreadHandle` | `0xCB9A0` | 202 | UnwindData |  |
| 1532 | `RpcSsSwapClientAllocFree` | `0xCBA70` | 120 | UnwindData |  |
| 1005 | `I_RpcInitHttpImports` | `0xCE4A0` | 12,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `NdrMesProcEncodeDecode3` | `0xD1530` | 86 | UnwindData |  |
| 1259 | `NdrMesSimpleTypeAlignSizeAll` | `0xD1590` | 173 | UnwindData |  |
| 1261 | `NdrMesSimpleTypeDecodeAll` | `0xD1650` | 422 | UnwindData |  |
| 1263 | `NdrMesSimpleTypeEncodeAll` | `0xD1800` | 357 | UnwindData |  |
| 1314 | `NdrServerCallNdr64` | `0xD1A00` | 62 | UnwindData |  |
| 1160 | `Ndr64AsyncServerCall64` | `0xD5010` | 9,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `NdrClientCall3` | `0xD7510` | 326 | UnwindData |  |
| 1159 | `Ndr64AsyncClientCall` | `0xD85C0` | 1,378 | UnwindData |  |
| 1161 | `Ndr64AsyncServerCallAll` | `0xDAF80` | 48,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `pfnFreeRoutines` | `0xE6B90` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `pfnMarshallRoutines` | `0xE6B98` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `pfnSizeRoutines` | `0xE6BA0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `pfnUnmarshallRoutines` | `0xE6BA8` | 19,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1543 | `SimpleTypeMemorySize` | `0xEB650` | 4,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `NdrTypeFlags` | `0xEC640` | 10,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1542 | `SimpleTypeBufferSize` | `0xEF020` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1541 | `SimpleTypeAlignment` | `0xEF0E0` | 0 | Indeterminate |  |
