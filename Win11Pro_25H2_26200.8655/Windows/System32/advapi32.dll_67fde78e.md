# Binary Specification: advapi32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\advapi32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `67fde78ed511226c04f02448082dcc399f16c9ac427aaa5618dbe99b59e85fe1`
* **Total Exported Functions:** 854

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1002 | `A_SHAFinal` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.A_SHAFinal` |
| 1003 | `A_SHAInit` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.A_SHAInit` |
| 1004 | `A_SHAUpdate` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.A_SHAUpdate` |
| 1029 | `AddMandatoryAce` | `0x0` | - | Forwarded | Forwarded to: `KERNELBASE.AddMandatoryAce` |
| 1148 | `CreateTraceInstanceId` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwCreateTraceInstanceId` |
| 1234 | `CveEventWrite` | `0x0` | - | Forwarded | Forwarded to: `KERNELBASE.CveEventWrite` |
| 1267 | `EventActivityIdControl` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwEventActivityIdControl` |
| 1268 | `EventEnabled` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwEventEnabled` |
| 1269 | `EventProviderEnabled` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwEventProviderEnabled` |
| 1270 | `EventRegister` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwEventRegister` |
| 1271 | `EventSetInformation` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwEventSetInformation` |
| 1272 | `EventUnregister` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwEventUnregister` |
| 1273 | `EventWrite` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwEventWrite` |
| 1274 | `EventWriteEndScenario` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwEventWriteEndScenario` |
| 1275 | `EventWriteEx` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwEventWriteEx` |
| 1276 | `EventWriteStartScenario` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwEventWriteStartScenario` |
| 1277 | `EventWriteString` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwEventWriteString` |
| 1278 | `EventWriteTransfer` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwEventWriteTransfer` |
| 1350 | `GetTraceEnableFlags` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwGetTraceEnableFlags` |
| 1351 | `GetTraceEnableLevel` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwGetTraceEnableLevel` |
| 1352 | `GetTraceLoggerHandle` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwGetTraceLoggerHandle` |
| 1362 | `I_QueryTagInformation` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-service-private-l1-1-0.I_QueryTagInformation` |
| 1363 | `I_ScIsSecurityProcess` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-service-private-l1-1-0.I_ScIsSecurityProcess` |
| 1364 | `I_ScPnPGetServiceName` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-service-private-l1-1-0.I_ScPnPGetServiceName` |
| 1365 | `I_ScQueryServiceConfig` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-service-private-l1-1-0.I_ScQueryServiceConfig` |
| 1366 | `I_ScRegisterPreshutdownRestart` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-service-private-l1-1-1.I_ScRegisterPreshutdownRestart` |
| 1368 | `I_ScSendPnPMessage` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-service-private-l1-1-0.I_ScSendPnPMessage` |
| 1369 | `I_ScSendTSMessage` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-service-private-l1-1-0.I_ScSendTSMessage` |
| 1372 | `I_ScValidatePnPService` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-service-private-l1-1-0.I_ScValidatePnPService` |
| 1392 | `IsValidRelativeSecurityDescriptor` | `0x0` | - | Forwarded | Forwarded to: `KERNELBASE.IsValidRelativeSecurityDescriptor` |
| 1497 | `MD4Final` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD4Final` |
| 1498 | `MD4Init` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD4Init` |
| 1499 | `MD4Update` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD4Update` |
| 1500 | `MD5Final` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD5Final` |
| 1501 | `MD5Init` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD5Init` |
| 1502 | `MD5Update` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD5Update` |
| 1543 | `PerfCreateInstance` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfCreateInstance` |
| 1544 | `PerfDecrementULongCounterValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfDecrementULongCounterValue` |
| 1545 | `PerfDecrementULongLongCounterValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfDecrementULongLongCounterValue` |
| 1547 | `PerfDeleteInstance` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfDeleteInstance` |
| 1550 | `PerfIncrementULongCounterValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfIncrementULongCounterValue` |
| 1551 | `PerfIncrementULongLongCounterValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfIncrementULongLongCounterValue` |
| 1556 | `PerfQueryInstance` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfQueryInstance` |
| 1563 | `PerfSetCounterRefValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfSetCounterRefValue` |
| 1564 | `PerfSetCounterSetInfo` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfSetCounterSetInfo` |
| 1565 | `PerfSetULongCounterValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfSetULongCounterValue` |
| 1566 | `PerfSetULongLongCounterValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfSetULongLongCounterValue` |
| 1567 | `PerfStartProvider` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfStartProvider` |
| 1568 | `PerfStartProviderEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfStartProviderEx` |
| 1569 | `PerfStopProvider` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfStopProvider` |
| 1689 | `RegisterTraceGuidsA` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwRegisterTraceGuidsA` |
| 1690 | `RegisterTraceGuidsW` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwRegisterTraceGuidsW` |
| 1698 | `RemoveTraceCallback` | `0x0` | - | Forwarded | Forwarded to: `sechost.RemoveTraceCallback` |
| 1754 | `SetTraceCallback` | `0x0` | - | Forwarded | Forwarded to: `sechost.SetTraceCallback` |
| 1765 | `SystemFunction001` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction001` |
| 1766 | `SystemFunction002` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction002` |
| 1767 | `SystemFunction003` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction003` |
| 1768 | `SystemFunction004` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction004` |
| 1769 | `SystemFunction005` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction005` |
| 1770 | `SystemFunction006` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction006` |
| 1771 | `SystemFunction007` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction007` |
| 1772 | `SystemFunction008` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction008` |
| 1773 | `SystemFunction009` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction009` |
| 1774 | `SystemFunction010` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction010` |
| 1775 | `SystemFunction011` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction011` |
| 1776 | `SystemFunction012` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction012` |
| 1777 | `SystemFunction013` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction013` |
| 1778 | `SystemFunction014` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction014` |
| 1779 | `SystemFunction015` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction015` |
| 1780 | `SystemFunction016` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction016` |
| 1782 | `SystemFunction018` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction018` |
| 1784 | `SystemFunction020` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction020` |
| 1785 | `SystemFunction021` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction021` |
| 1786 | `SystemFunction022` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction022` |
| 1787 | `SystemFunction023` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction023` |
| 1788 | `SystemFunction024` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction024` |
| 1789 | `SystemFunction025` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction025` |
| 1790 | `SystemFunction026` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction026` |
| 1791 | `SystemFunction027` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction027` |
| 1792 | `SystemFunction028` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction028` |
| 1793 | `SystemFunction029` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction029` |
| 1794 | `SystemFunction030` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction030` |
| 1795 | `SystemFunction031` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction031` |
| 1796 | `SystemFunction032` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction032` |
| 1797 | `SystemFunction033` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction033` |
| 1798 | `SystemFunction034` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction034` |
| 1799 | `SystemFunction035` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.CheckSignatureInFile` |
| 1800 | `SystemFunction036` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction036` |
| 1801 | `SystemFunction040` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction040` |
| 1802 | `SystemFunction041` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction041` |
| 1803 | `TraceEvent` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwLogTraceEvent` |
| 1804 | `TraceEventInstance` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwTraceEventInstance` |
| 1805 | `TraceMessage` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwTraceMessage` |
| 1806 | `TraceMessageVa` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwTraceMessageVa` |
| 1807 | `TraceQueryInformation` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-controller-l1-1-0.TraceQueryInformation` |
| 1818 | `UnregisterTraceGuids` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwUnregisterTraceGuids` |
| 1557 | `PerfRegCloseKey` | `0x1490` | 1,120 | UnwindData |  |
| 1554 | `PerfQueryCounterInfo` | `0x6620` | 313 | UnwindData |  |
| 1555 | `PerfQueryCounterSetRegistrationInfo` | `0x6D90` | 392 | UnwindData |  |
| 1542 | `PerfCloseQueryHandle` | `0x6F20` | 191 | UnwindData |  |
| 1553 | `PerfQueryCounterData` | `0x6FF0` | 313 | UnwindData |  |
| 1552 | `PerfOpenQueryHandle` | `0x7130` | 387 | UnwindData |  |
| 1549 | `PerfEnumerateCounterSetInstances` | `0x76E0` | 337 | UnwindData |  |
| 1107 | `ComputeAccessTokenFromCodeAuthzLevel` | `0x12400` | 757 | UnwindData |  |
| 1705 | `SaferComputeTokenFromLevel` | `0x12400` | 757 | UnwindData |  |
| 1714 | `SaferiCompareTokenLevels` | `0x132C0` | 127 | UnwindData |  |
| 1715 | `SaferiIsDllAllowed` | `0x14FB0` | 376 | UnwindData |  |
| 1373 | `IdentifyCodeAuthzLevelW` | `0x15130` | 2,204 | UnwindData |  |
| 1709 | `SaferIdentifyLevel` | `0x15130` | 2,204 | UnwindData |  |
| 1716 | `SaferiIsExecutableFileType` | `0x17F30` | 139 | UnwindData |  |
| 1713 | `SaferiChangeRegistryScope` | `0x184E0` | 42 | UnwindData |  |
| 1132 | `ConvertStringSidToSidA` | `0x18780` | 175 | UnwindData |  |
| 1133 | `ConvertStringSidToSidW` | `0x18890` | 558 | UnwindData |  |
| 1131 | `ConvertStringSecurityDescriptorToSecurityDescriptorW` | `0x1C990` | 102 | UnwindData |  |
| 1125 | `ConvertSidToStringSidW` | `0x1CA30` | 321 | UnwindData |  |
| 1411 | `LookupPrivilegeNameW` | `0x1CBD0` | 382 | UnwindData |  |
| 1413 | `LookupPrivilegeValueW` | `0x1CD60` | 280 | UnwindData |  |
| 1454 | `LsaLookupPrivilegeValue` | `0x1D150` | 131 | UnwindData |  |
| 1453 | `LsaLookupPrivilegeName` | `0x1D1E0` | 155 | UnwindData |  |
| 1412 | `LookupPrivilegeValueA` | `0x1E700` | 256 | UnwindData |  |
| 1130 | `ConvertStringSecurityDescriptorToSecurityDescriptorA` | `0x1E810` | 203 | UnwindData |  |
| 1634 | `RegEnumValueW` | `0x25180` | 67 | UnwindData |  |
| 1255 | `EnumServicesStatusA` | `0x252D0` | 554 | UnwindData |  |
| 1258 | `EnumServicesStatusW` | `0x25570` | 70 | UnwindData |  |
| 1254 | `EnumServiceGroupW` | `0x255C0` | 635 | UnwindData |  |
| 1656 | `RegQueryInfoKeyW` | `0x25ED0` | 121 | UnwindData |  |
| 1613 | `RegDeleteKeyA` | `0x25F50` | 110 | UnwindData |  |
| 1620 | `RegDeleteKeyW` | `0x25FD0` | 286 | UnwindData |  |
| 1124 | `ConvertSidToStringSidA` | `0x27090` | 608 | UnwindData |  |
| 1649 | `RegOpenKeyExW` | `0x27300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1404 | `LookupAccountNameA` | `0x27320` | 656 | UnwindData |  |
| 1406 | `LookupAccountSidA` | `0x275C0` | 735 | UnwindData |  |
| 1405 | `LookupAccountNameW` | `0x278B0` | 164 | UnwindData |  |
| 1407 | `LookupAccountSidW` | `0x27960` | 164 | UnwindData |  |
| 1632 | `RegEnumKeyW` | `0x27F00` | 70 | UnwindData |  |
| 1600 | `RegCloseKey` | `0x287B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1662 | `RegQueryValueExW` | `0x287D0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1660 | `RegQueryValueA` | `0x28950` | 642 | UnwindData |  |
| 1663 | `RegQueryValueW` | `0x28BE0` | 647 | UnwindData |  |
| 1143 | `CreateProcessWithTokenW` | `0x29480` | 102 | UnwindData |  |
| 1324 | `GetNamedSecurityInfoW` | `0x2ADC0` | 67 | UnwindData |  |
| 1652 | `RegOpenKeyW` | `0x2AE30` | 99 | UnwindData |  |
| 1535 | `OpenThreadToken` | `0x2AEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1442 | `LsaGetUserName` | `0x2AEC0` | 271 | UnwindData |  |
| 1394 | `IsValidSid` | `0x2AFE0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1530 | `OpenProcessToken` | `0x2B070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1648 | `RegOpenKeyExA` | `0x2B090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1724 | `SetEntriesInAclA` | `0x2B0B0` | 650 | UnwindData |  |
| 1321 | `GetNamedSecurityInfoA` | `0x2B340` | 168 | UnwindData |  |
| 1733 | `SetNamedSecurityInfoA` | `0x2B3F0` | 155 | UnwindData |  |
| 1651 | `RegOpenKeyTransactedW` | `0x2B5A0` | 1,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1548 | `PerfEnumerateCounterSet` | `0x2BC60` | 299 | UnwindData |  |
| 1633 | `RegEnumValueA` | `0x2BED0` | 67 | UnwindData |  |
| 1349 | `GetTokenInformation` | `0x2BF20` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1455 | `LsaLookupSids` | `0x2C420` | 38 | UnwindData |  |
| 1560 | `PerfRegQueryInfoKey` | `0x2CC20` | 1,007 | UnwindData |  |
| 1561 | `PerfRegQueryValue` | `0x2D120` | 65 | UnwindData |  |
| 1336 | `GetSecurityInfo` | `0x2E020` | 67 | UnwindData |  |
| 1611 | `RegCreateKeyTransactedW` | `0x2E070` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `EnumServicesStatusExW` | `0x2E0B0` | 96 | UnwindData |  |
| 1661 | `RegQueryValueExA` | `0x2E120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1638 | `RegGetValueW` | `0x2E140` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1300 | `GetEffectiveRightsFromAclW` | `0x2E270` | 166 | UnwindData |  |
| 1810 | `TreeResetNamedSecurityInfoW` | `0x2E320` | 259 | UnwindData |  |
| 1812 | `TreeSetNamedSecurityInfoW` | `0x2E430` | 252 | UnwindData |  |
| 1082 | `BuildSecurityDescriptorW` | `0x2E710` | 987 | UnwindData |  |
| 1719 | `SaferiSearchMatchingHashRules` | `0x2F0B0` | 489 | UnwindData |  |
| 1312 | `GetLengthSid` | `0x2F2A0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1378 | `InitializeAcl` | `0x2F6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `RegEnumKeyExA` | `0x2F6C0` | 67 | UnwindData |  |
| 1631 | `RegEnumKeyExW` | `0x2F710` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1135 | `CopySid` | `0x2F950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1034 | `AllocateAndInitializeSid` | `0x2F970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1837 | `WmiOpenBlock` | `0x2F990` | 256 | UnwindData |  |
| 1297 | `GetCurrentHwProfileW` | `0x2FAA0` | 799 | UnwindData |  |
| 1219 | `CryptHashData` | `0x30340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1360 | `GetUserNameW` | `0x30360` | 36 | UnwindData |  |
| 1702 | `RevertToSelf` | `0x30390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1608 | `RegCreateKeyExA` | `0x303B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1458 | `LsaNtStatusToWinError` | `0x303D0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1678 | `RegSetValueExW` | `0x30530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1379 | `InitializeSecurityDescriptor` | `0x30550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1259 | `EnumerateTraceGuids` | `0x30570` | 461 | UnwindData |  |
| 1359 | `GetUserNameA` | `0x30750` | 36 | UnwindData |  |
| 1655 | `RegQueryInfoKeyA` | `0x308D0` | 121 | UnwindData |  |
| 1503 | `MIDL_user_free_Ext` | `0x30950` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1141 | `CreateProcessAsUserW` | `0x309C0` | 107 | UnwindData |  |
| 1263 | `EqualSid` | `0x30A40` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1609 | `RegCreateKeyExW` | `0x30AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1293 | `GetAclInformation` | `0x30B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1752 | `SetThreadToken` | `0x30B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `CryptGetHashParam` | `0x30B50` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `CryptCreateHash` | `0x30C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1741 | `SetSecurityDescriptorDacl` | `0x30C70` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1097 | `CheckTokenMembership` | `0x30D10` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1612 | `RegCreateKeyW` | `0x30EC0` | 124 | UnwindData |  |
| 1540 | `OperationStart` | `0x30F50` | 225 | UnwindData |  |
| 1103 | `CloseServiceHandle` | `0x31040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `BuildTrusteeWithSidA` | `0x31060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1090 | `BuildTrusteeWithSidW` | `0x31060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1375 | `ImpersonateLoggedOnUser` | `0x31080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1123 | `ConvertSecurityDescriptorToStringSecurityDescriptorW` | `0x310A0` | 204 | UnwindData |  |
| 1539 | `OperationEnd` | `0x31180` | 229 | UnwindData |  |
| 1647 | `RegOpenKeyA` | `0x313D0` | 96 | UnwindData |  |
| 1201 | `CryptDestroyHash` | `0x31440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1645 | `RegNotifyChangeKeyValue` | `0x31460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1136 | `CreateCodeAuthzLevel` | `0x31480` | 192 | UnwindData |  |
| 1706 | `SaferCreateLevel` | `0x31480` | 192 | UnwindData |  |
| 1677 | `RegSetValueExA` | `0x31770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `AccessCheck` | `0x31790` | 67 | UnwindData |  |
| 1436 | `LsaFreeMemory` | `0x317E0` | 24 | UnwindData |  |
| 1380 | `InitializeSid` | `0x31800` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1532 | `OpenSCManagerW` | `0x31850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `CryptImportKey` | `0x31870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1345 | `GetSidSubAuthority` | `0x31890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `FreeSid` | `0x318B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1344 | `GetSidLengthRequired` | `0x318D0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `CheckForHiberboot` | `0x31A40` | 42 | UnwindData |  |
| 1534 | `OpenServiceW` | `0x32240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1243 | `DuplicateTokenEx` | `0x32260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `AddAce` | `0x32280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1637 | `RegGetValueA` | `0x322A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `CryptAcquireContextW` | `0x322C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1100 | `CloseCodeAuthzLevel` | `0x322E0` | 42 | UnwindData |  |
| 1704 | `SaferCloseLevel` | `0x322E0` | 42 | UnwindData |  |
| 1033 | `AdjustTokenPrivileges` | `0x323E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1629 | `RegEnumKeyA` | `0x32400` | 67 | UnwindData |  |
| 1292 | `GetAce` | `0x32450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1388 | `IsTextUnicode` | `0x32470` | 31 | UnwindData |  |
| 1330 | `GetSecurityDescriptorDacl` | `0x324A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1329 | `GetSecurityDescriptorControl` | `0x324C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `GetSecurityDescriptorLength` | `0x324E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1346 | `GetSidSubAuthorityCount` | `0x32500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1746 | `SetSecurityInfo` | `0x32520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1590 | `QueryServiceStatusEx` | `0x32540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1751 | `SetServiceStatus` | `0x32560` | 1,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1333 | `GetSecurityDescriptorOwner` | `0x32CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1075 | `BuildExplicitAccessWithNameA` | `0x32CF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `BuildExplicitAccessWithNameW` | `0x32CF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1624 | `RegDeleteValueW` | `0x32D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `CryptDecrypt` | `0x32D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1242 | `DuplicateToken` | `0x32D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `CommandLineFromMsiDescriptor` | `0x32D80` | 910 | UnwindData |  |
| 1210 | `CryptExportKey` | `0x33480` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1589 | `QueryServiceStatus` | `0x340C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `CryptGenRandom` | `0x340E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1725 | `SetEntriesInAclW` | `0x34100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `CryptSetHashParam` | `0x34120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1509 | `MapGenericMask` | `0x34140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1584 | `QueryServiceConfigW` | `0x34160` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1222 | `CryptReleaseContext` | `0x34220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1541 | `PerfAddCounters` | `0x34240` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1625 | `RegDisablePredefinedCache` | `0x342B0` | 41 | UnwindData |  |
| 1607 | `RegCreateKeyA` | `0x342E0` | 124 | UnwindData |  |
| 1112 | `ControlTraceW` | `0x34370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `CryptAcquireContextA` | `0x34390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1508 | `MakeSelfRelativeSD` | `0x343B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1308 | `GetInformationCodeAuthzPolicyW` | `0x343D0` | 52 | UnwindData |  |
| 1708 | `SaferGetPolicyInformation` | `0x343D0` | 52 | UnwindData |  |
| 1335 | `GetSecurityDescriptorSacl` | `0x344B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1622 | `RegDeleteTreeW` | `0x344D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `CreateWellKnownSid` | `0x344F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1604 | `RegConnectRegistryW` | `0x34510` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `AddAccessAllowedAce` | `0x34570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `CryptDestroyKey` | `0x34590` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1575 | `ProcessTrace` | `0x34650` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1244 | `EnableTrace` | `0x34690` | 130 | UnwindData |  |
| 1753 | `SetTokenInformation` | `0x34720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1245 | `EnableTraceEx` | `0x34740` | 207 | UnwindData |  |
| 1083 | `BuildTrusteeWithNameA` | `0x34820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1084 | `BuildTrusteeWithNameW` | `0x34820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `CreatePrivateObjectSecurity` | `0x34840` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1694 | `RemoteRegQueryInfoKeyWrapper` | `0x34BA0` | 235 | UnwindData |  |
| 1240 | `DestroyPrivateObjectSecurity` | `0x34D90` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1623 | `RegDeleteValueA` | `0x34F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1393 | `IsValidSecurityDescriptor` | `0x34F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1646 | `RegOpenCurrentUser` | `0x34FB0` | 5,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `CreateRestrictedToken` | `0x36340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1460 | `LsaOpenPolicy` | `0x36360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `GetSecurityDescriptorGroup` | `0x36370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1216 | `CryptGetKeyParam` | `0x36390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1636 | `RegGetKeySecurity` | `0x363B0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1736 | `SetNamedSecurityInfoW` | `0x365E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1570 | `PrivilegeCheck` | `0x36600` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1419 | `LsaClose` | `0x36680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1260 | `EnumerateTraceGuidsEx` | `0x36690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `AddAccessAllowedAceEx` | `0x366B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1197 | `CryptContextAddRef` | `0x366D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `ConvertSecurityDescriptorToStringSecurityDescriptorA` | `0x366F0` | 498 | UnwindData |  |
| 1306 | `GetFileSecurityW` | `0x368F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `QueryTraceW` | `0x36910` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1140 | `CreateProcessAsUserA` | `0x36C30` | 107 | UnwindData |  |
| 1014 | `AccessCheckByTypeResultListAndAuditAlarmA` | `0x36CB0` | 484 | UnwindData |  |
| 1342 | `GetServiceKeyNameW` | `0x36EA0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1675 | `RegSetKeyValueW` | `0x37050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1246 | `EnableTraceEx2` | `0x37070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | *Ordinal Only* | `0x37090` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `OpenSCManagerA` | `0x370F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1644 | `RegLoadMUIStringW` | `0x37110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1377 | `ImpersonateSelf` | `0x37130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1382 | `InitiateShutdownW` | `0x37150` | 271 | UnwindData |  |
| 1533 | `OpenServiceA` | `0x37290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1108 | `ControlService` | `0x372B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1506 | `MakeAbsoluteSD` | `0x372D0` | 109 | UnwindData |  |
| 1395 | `IsWellKnownSid` | `0x37350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1615 | `RegDeleteKeyExW` | `0x37370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `GetLocalManagedApplicationData` | `0x37390` | 633 | UnwindData |  |
| 1582 | `QueryServiceConfig2W` | `0x37610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `RegDeleteKeyTransactedW` | `0x37630` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1205 | `CryptEncrypt` | `0x37670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1389 | `IsTokenRestricted` | `0x37690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `FlushTraceW` | `0x376B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1583 | `QueryServiceConfigA` | `0x37700` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1139 | `CreatePrivateObjectSecurityWithMultipleInheritance` | `0x378A0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1627 | `RegDisableReflectionKey` | `0x37980` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1628 | `RegEnableReflectionKey` | `0x37980` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1742 | `SetSecurityDescriptorGroup` | `0x37D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1340 | `GetServiceDisplayNameW` | `0x37D70` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1155 | `CredEnumerateW` | `0x37F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1158 | `CredFree` | `0x37F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1307 | `GetInformationCodeAuthzLevelW` | `0x37F80` | 183 | UnwindData |  |
| 1707 | `SaferGetLevelInformation` | `0x37F80` | 183 | UnwindData |  |
| 1729 | `SetFileSecurityW` | `0x383F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1237 | `DeleteAce` | `0x38410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1224 | `CryptSetKeyParam` | `0x38430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1200 | `CryptDeriveKey` | `0x38450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1343 | `GetSidIdentifierAuthority` | `0x38470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `OpenTraceW` | `0x38490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1147 | `CreateServiceW` | `0x384B0` | 130 | UnwindData |  |
| 1105 | `CloseTrace` | `0x38790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1214 | `CryptGetDefaultProviderW` | `0x387B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1762 | `StartTraceW` | `0x387D0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1658 | `RegQueryMultipleValuesW` | `0x38D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1095 | `ChangeServiceConfigW` | `0x38DA0` | 109 | UnwindData |  |
| 1182 | `CredUnmarshalCredentialW` | `0x38E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1691 | `RegisterWaitChainCOMCallback` | `0x38E40` | 183 | UnwindData |  |
| 1602 | `RegConnectRegistryExA` | `0x38F00` | 164 | UnwindData |  |
| 1603 | `RegConnectRegistryExW` | `0x38FB0` | 261 | UnwindData |  |
| 1510 | `NotifyBootConfigStatus` | `0x390C0` | 102 | UnwindData |  |
| 1673 | `RegSetKeySecurity` | `0x39130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1743 | `SetSecurityDescriptorOwner` | `0x39150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1728 | `SetFileSecurityA` | `0x39170` | 176 | UnwindData |  |
| 1374 | `ImpersonateAnonymousToken` | `0x39230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1203 | `CryptDuplicateHash` | `0x39250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1817 | `UnregisterIdleTask` | `0x39270` | 17 | UnwindData |  |
| 1249 | `EncryptedFileKeyInfo` | `0x39810` | 122 | UnwindData |  |
| 1449 | `LsaIsUserArsoEnabled` | `0x39890` | 99 | UnwindData |  |
| 1759 | `StartServiceCtrlDispatcherW` | `0x39900` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1252 | `EnumDependentServicesW` | `0x39B80` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1537 | `OpenTraceA` | `0x39C70` | 229 | UnwindData |  |
| 1403 | `LogonUserW` | `0x39E60` | 63 | UnwindData |  |
| 1472 | `LsaQueryInformationPolicy` | `0x39FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1635 | `RegFlushKey` | `0x39FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1233 | `CryptVerifySignatureW` | `0x39FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1745 | `SetSecurityDescriptorSacl` | `0x3A000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1177 | `CredReadW` | `0x3A020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1311 | `GetKernelObjectSecurity` | `0x3A040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1764 | `StopTraceW` | `0x3A060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `AreAllAccessesGranted` | `0x3A080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1653 | `RegOpenUserClassesRoot` | `0x3A0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `CryptGetProvParam` | `0x3A0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `AuditQuerySystemPolicy` | `0x3A0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1760 | `StartServiceW` | `0x3A100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1448 | `LsaIsUserArsoAllowed` | `0x3A120` | 94 | UnwindData |  |
| 1376 | `ImpersonateNamedPipeClient` | `0x3A190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1679 | `RegSetValueW` | `0x3A1B0` | 367 | UnwindData |  |
| 1546 | `PerfDeleteCounters` | `0x3A330` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `CryptGenKey` | `0x3A3C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1688 | `RegisterServiceCtrlHandlerW` | `0x3A430` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1619 | `RegDeleteKeyValueW` | `0x3A4E0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1361 | `GetWindowsAccountDomainSid` | `0x3A680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `AddAccessDeniedAce` | `0x3A6A0` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `AuditQueryPerUserPolicy` | `0x3AA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1451 | `LsaLookupNames2` | `0x3AA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1204 | `CryptDuplicateKey` | `0x3AA80` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `AllocateLocallyUniqueId` | `0x3ABB0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1740 | `SetSecurityDescriptorControl` | `0x3ACD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1305 | `GetFileSecurityA` | `0x3ACF0` | 201 | UnwindData |  |
| 1701 | `ReportEventW` | `0x3ADC0` | 534 | UnwindData |  |
| 1043 | `AuditFree` | `0x3B190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `CryptVerifySignatureA` | `0x3B1B0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1515 | `NpGetUserName` | `0x3B500` | 354 | UnwindData |  |
| 1218 | `CryptGetUserKey` | `0x3B670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1188 | `CredWriteW` | `0x3B690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1296 | `GetCurrentHwProfileA` | `0x3B6B0` | 303 | UnwindData |  |
| 1431 | `LsaEnumerateAccountsWithUserRight` | `0x3B890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1391 | `IsValidAcl` | `0x3B8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1687 | `RegisterServiceCtrlHandlerExW` | `0x3B8C0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1513 | `NotifyServiceStatusChangeA` | `0x3BB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1606 | `RegCopyTreeW` | `0x3BB40` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1457 | `LsaManageSidNameMapping` | `0x3BD00` | 281 | UnwindData |  |
| 1514 | `NotifyServiceStatusChangeW` | `0x3BE20` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1396 | `LockServiceDatabase` | `0x3BEC0` | 110 | UnwindData |  |
| 1614 | `RegDeleteKeyExA` | `0x3BF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1672 | `RegSaveKeyW` | `0x3BF60` | 384 | UnwindData |  |
| 1732 | `SetKernelObjectSecurity` | `0x3C0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1093 | `ChangeServiceConfig2W` | `0x3C110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1152 | `CredDeleteW` | `0x3C130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1256 | `EnumServicesStatusExA` | `0x3C150` | 589 | UnwindData |  |
| 1434 | `LsaEnumerateTrustedDomains` | `0x3C550` | 203 | UnwindData |  |
| 1577 | `QueryAllTracesW` | `0x3CEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1280 | `FileEncryptionStatusW` | `0x3CEE0` | 75 | UnwindData |  |
| 1410 | `LookupPrivilegeNameA` | `0x3CF60` | 433 | UnwindData |  |
| 1601 | `RegConnectRegistryA` | `0x3D120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1208 | `CryptEnumProvidersA` | `0x3D140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1450 | `LsaLookupNames` | `0x3D160` | 392 | UnwindData |  |
| 1059 | `AuditSetSystemPolicy` | `0x3D450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1654 | `RegOverridePredefKey` | `0x3D470` | 102 | UnwindData |  |
| 1264 | `EventAccessControl` | `0x3D640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1225 | `CryptSetProvParam` | `0x3D660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1829 | `WmiExecuteMethodW` | `0x3D680` | 876 | UnwindData |  |
| 1062 | `BaseRegCloseKey` | `0x3DB60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1285 | `FreeEncryptedFileKeyInfo` | `0x3DB90` | 38 | UnwindData |  |
| 1287 | `FreeEncryptionCertificateHashList` | `0x3DBC0` | 35 | UnwindData |  |
| 1674 | `RegSetKeyValueA` | `0x3DCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1757 | `StartServiceA` | `0x3DCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1238 | `DeleteService` | `0x3DD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `GetExplicitEntriesFromAclA` | `0x3DD20` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `GetExplicitEntriesFromAclW` | `0x3DD20` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1581 | `QueryServiceConfig2A` | `0x3E0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1758 | `StartServiceCtrlDispatcherA` | `0x3E0C0` | 3,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1262 | `EqualPrefixSid` | `0x3EE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1185 | `CredWriteA` | `0x3EE70` | 1,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1684 | `RegisterIdleTask` | `0x3F510` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `RegLoadKeyW` | `0x3F5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1092 | `ChangeServiceConfig2A` | `0x3F5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1750 | `SetServiceObjectSecurity` | `0x3F600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `QueryServiceObjectSecurity` | `0x3F620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `CredDeleteA` | `0x3F640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `AddAuditAccessAce` | `0x3F660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `AuditSetGlobalSaclW` | `0x3F680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `CryptEnumProvidersW` | `0x3F6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1640 | `RegLoadAppKeyW` | `0x3F6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `CredReadA` | `0x3F6E0` | 1,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1429 | `LsaEnumerateAccountRights` | `0x3FC60` | 2,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1111 | `ControlTraceA` | `0x40550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1576 | `QueryAllTracesA` | `0x40560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1761 | `StartTraceA` | `0x40570` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `NotifyServiceStatusChange` | `0x406E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `CreateServiceEx` | `0x406F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1367 | `I_ScReparseServiceDatabase` | `0x40700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1578 | `QueryLocalUserServiceName` | `0x40710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1594 | `QueryUserServiceName` | `0x40720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1595 | `QueryUserServiceNameForContext` | `0x40730` | 3,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1030 | `AddUsersToEncryptedFile` | `0x41300` | 106 | UnwindData |  |
| 1031 | `AddUsersToEncryptedFileEx` | `0x41370` | 141 | UnwindData |  |
| 1101 | `CloseEncryptedFileRaw` | `0x41410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1235 | `DecryptFileA` | `0x41430` | 199 | UnwindData |  |
| 1236 | `DecryptFileW` | `0x41500` | 124 | UnwindData |  |
| 1241 | `DuplicateEncryptionInfoFile` | `0x41590` | 148 | UnwindData |  |
| 1247 | `EncryptFileA` | `0x41630` | 183 | UnwindData |  |
| 1248 | `EncryptFileW` | `0x416F0` | 110 | UnwindData |  |
| 1250 | `EncryptionDisable` | `0x41770` | 73 | UnwindData |  |
| 1279 | `FileEncryptionStatusA` | `0x417C0` | 201 | UnwindData |  |
| 1282 | `FlushEfsCache` | `0x41890` | 133 | UnwindData |  |
| 1286 | `FreeEncryptedFileMetadata` | `0x41920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1301 | `GetEncryptedFileMetadata` | `0x41930` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `I_ScGetCurrentGroupStateW` | `0x41930` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1721 | `SetEncryptedFileMetadata` | `0x41930` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1526 | `OpenEncryptedFileRawA` | `0x41A70` | 183 | UnwindData |  |
| 1527 | `OpenEncryptedFileRawW` | `0x41B30` | 103 | UnwindData |  |
| 1579 | `QueryRecoveryAgentsOnEncryptedFile` | `0x41BA0` | 106 | UnwindData |  |
| 1596 | `QueryUsersOnEncryptedFile` | `0x41C10` | 106 | UnwindData |  |
| 1597 | `ReadEncryptedFileRaw` | `0x41C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1699 | `RemoveUsersFromEncryptedFile` | `0x41CA0` | 106 | UnwindData |  |
| 1755 | `SetUserFileEncryptionKey` | `0x41D10` | 80 | UnwindData |  |
| 1756 | `SetUserFileEncryptionKeyEx` | `0x41D70` | 115 | UnwindData |  |
| 1821 | `UsePinForEncryptedFilesA` | `0x41DF0` | 127 | UnwindData |  |
| 1822 | `UsePinForEncryptedFilesW` | `0x41E80` | 151 | UnwindData |  |
| 1853 | `WriteEncryptedFileRaw` | `0x41F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `AccessCheckAndAuditAlarmW` | `0x41F40` | 107 | UnwindData |  |
| 1012 | `AccessCheckByTypeAndAuditAlarmW` | `0x41FC0` | 170 | UnwindData |  |
| 1016 | `AccessCheckByTypeResultListAndAuditAlarmByHandleW` | `0x42070` | 182 | UnwindData |  |
| 1017 | `AccessCheckByTypeResultListAndAuditAlarmW` | `0x42130` | 170 | UnwindData |  |
| 1013 | `AccessCheckByTypeResultList` | `0x421E0` | 108 | UnwindData |  |
| 1010 | `AccessCheckByType` | `0x42260` | 108 | UnwindData |  |
| 1020 | `AddAccessAllowedObjectAce` | `0x422E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `AddAccessDeniedAceEx` | `0x42300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `AddAccessDeniedObjectAce` | `0x42320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `AddAuditAccessAceEx` | `0x42340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `AddAuditAccessObjectAce` | `0x42360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `AdjustTokenGroups` | `0x42380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `AreAnyAccessesGranted` | `0x423A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `AuditComputeEffectivePolicyBySid` | `0x423C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1040 | `AuditEnumerateCategories` | `0x423E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | `AuditEnumeratePerUserPolicy` | `0x42400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1042 | `AuditEnumerateSubCategories` | `0x42420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1047 | `AuditLookupCategoryNameW` | `0x42440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1049 | `AuditLookupSubCategoryNameW` | `0x42460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1051 | `AuditQueryGlobalSaclW` | `0x42480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1053 | `AuditQuerySecurity` | `0x424A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `AuditSetPerUserPolicy` | `0x424C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `AuditSetSecurity` | `0x424E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1094 | `ChangeServiceConfigA` | `0x42500` | 109 | UnwindData |  |
| 1109 | `ControlServiceExA` | `0x42580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1110 | `ControlServiceExW` | `0x425A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1134 | `ConvertToAutoInheritPrivateObjectSecurity` | `0x425C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `CreatePrivateObjectSecurityEx` | `0x425E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `CreateServiceA` | `0x42600` | 130 | UnwindData |  |
| 1150 | `CredBackupCredentials` | `0x42690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1153 | `CredEncryptAndMarshalBinaryBlob` | `0x426B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1154 | `CredEnumerateA` | `0x426D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1156 | `CredFindBestCredentialA` | `0x426F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1157 | `CredFindBestCredentialW` | `0x42710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1159 | `CredGetSessionTypes` | `0x42730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1160 | `CredGetTargetInfoA` | `0x42750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1161 | `CredGetTargetInfoW` | `0x42770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1163 | `CredIsMarshaledCredentialW` | `0x42790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1164 | `CredIsProtectedA` | `0x427B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1165 | `CredIsProtectedW` | `0x427D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1166 | `CredMarshalCredentialA` | `0x427F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `CredMarshalCredentialW` | `0x42810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1169 | `CredProfileLoadedEx` | `0x42830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1168 | `CredProfileLoaded` | `0x42850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1170 | `CredProfileUnloaded` | `0x42870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `CredProtectA` | `0x42890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1172 | `CredProtectW` | `0x428B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `CredReadByTokenHandle` | `0x428D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `CredReadDomainCredentialsA` | `0x428F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1176 | `CredReadDomainCredentialsW` | `0x42910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `CredRestoreCredentials` | `0x42930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1181 | `CredUnmarshalCredentialA` | `0x42950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1183 | `CredUnprotectA` | `0x42970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1184 | `CredUnprotectW` | `0x42990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1186 | `CredWriteDomainCredentialsA` | `0x429B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `CredWriteDomainCredentialsW` | `0x429D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1189 | `CredpConvertCredential` | `0x429F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1190 | `CredpConvertOneCredentialSize` | `0x42A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1191 | `CredpConvertTargetInfo` | `0x42A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1192 | `CredpDecodeCredential` | `0x42A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `CredpEncodeCredential` | `0x42A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1194 | `CredpEncodeSecret` | `0x42A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1206 | `CryptEnumProviderTypesA` | `0x42AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `CryptEnumProviderTypesW` | `0x42AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `CryptGetDefaultProviderA` | `0x42AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `CryptHashSessionKey` | `0x42B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `CryptSetProviderA` | `0x42B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `CryptSetProviderExA` | `0x42B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1228 | `CryptSetProviderExW` | `0x42B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1229 | `CryptSetProviderW` | `0x42B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `CryptSignHashA` | `0x42BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `CryptSignHashW` | `0x42BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `EnumDynamicTimeZoneInformation` | `0x42BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1261 | `EqualDomainSid` | `0x42C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1265 | `EventAccessQuery` | `0x42C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1266 | `EventAccessRemove` | `0x42C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1281 | `FindFirstFreeAce` | `0x42C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1298 | `GetDynamicTimeZoneInformationEffectiveYears` | `0x42C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `GetPrivateObjectSecurity` | `0x42CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `GetSecurityDescriptorRMControl` | `0x42CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1370 | `I_ScSetServiceBitsA` | `0x42CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1371 | `I_ScSetServiceBitsW` | `0x42D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1401 | `LogonUserExExW` | `0x42D30` | 108 | UnwindData |  |
| 1416 | `LsaAddAccountRights` | `0x42DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1422 | `LsaCreateSecret` | `0x42DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `LsaDelete` | `0x42DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1443 | `LsaICLookupNames` | `0x42DE0` | 88 | UnwindData |  |
| 1444 | `LsaICLookupNamesWithCreds` | `0x42E40` | 111 | UnwindData |  |
| 1445 | `LsaICLookupSids` | `0x42EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1446 | `LsaICLookupSidsWithCreds` | `0x42ED0` | 111 | UnwindData |  |
| 1456 | `LsaLookupSids2` | `0x42F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1462 | `LsaOpenSecret` | `0x42F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1475 | `LsaQuerySecret` | `0x42F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `LsaRemoveAccountRights` | `0x42F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1481 | `LsaRetrievePrivateData` | `0x42F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1486 | `LsaSetInformationPolicy` | `0x42FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1490 | `LsaSetSecret` | `0x42FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1495 | `LsaStorePrivateData` | `0x42FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1507 | `MakeAbsoluteSD2` | `0x42FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1517 | `ObjectCloseAuditAlarmW` | `0x42FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1519 | `ObjectDeleteAuditAlarmW` | `0x43010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1521 | `ObjectOpenAuditAlarmW` | `0x43030` | 117 | UnwindData |  |
| 1523 | `ObjectPrivilegeAuditAlarmW` | `0x430B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1572 | `PrivilegedServiceAuditAlarmW` | `0x430D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1580 | `QuerySecurityAccessMask` | `0x430F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1585 | `QueryServiceDynamicInformation` | `0x43110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1592 | `QueryTraceProcessingHandle` | `0x43130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1618 | `RegDeleteKeyValueA` | `0x43150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1621 | `RegDeleteTreeA` | `0x43170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1626 | `RegDisablePredefinedCacheEx` | `0x43190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1639 | `RegLoadAppKeyA` | `0x431B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1641 | `RegLoadKeyA` | `0x431D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1643 | `RegLoadMUIStringA` | `0x431F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1657 | `RegQueryMultipleValuesA` | `0x43210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1667 | `RegRestoreKeyA` | `0x43230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `RegRestoreKeyW` | `0x43250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1670 | `RegSaveKeyExA` | `0x43270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1671 | `RegSaveKeyExW` | `0x43290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1680 | `RegUnLoadKeyA` | `0x432B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1681 | `RegUnLoadKeyW` | `0x432D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1685 | `RegisterServiceCtrlHandlerA` | `0x432F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `RegisterServiceCtrlHandlerExA` | `0x43310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1720 | `SetAclInformation` | `0x43330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1738 | `SetPrivateObjectSecurityEx` | `0x43350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1737 | `SetPrivateObjectSecurity` | `0x43370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1739 | `SetSecurityAccessMask` | `0x43390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1744 | `SetSecurityDescriptorRMControl` | `0x433B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1808 | `TraceSetInformation` | `0x433D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1823 | `WaitServiceState` | `0x433F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1504 | `MSChapSrvChangePassword` | `0x43410` | 712 | UnwindData |  |
| 1505 | `MSChapSrvChangePassword2` | `0x436E0` | 249 | UnwindData |  |
| 1659 | `RegQueryReflectionKey` | `0x43A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1573 | `ProcessIdleTasks` | `0x43A40` | 60 | UnwindData |  |
| 1574 | `ProcessIdleTasksW` | `0x43A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1781 | `SystemFunction017` | `0x43AA0` | 80 | UnwindData |  |
| 1783 | `SystemFunction019` | `0x43B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `AuditComputeEffectivePolicyByToken` | `0x43B10` | 346 | UnwindData |  |
| 1044 | `AuditLookupCategoryGuidFromCategoryId` | `0x43C70` | 56 | UnwindData |  |
| 1045 | `AuditLookupCategoryIdFromCategoryGuid` | `0x43CB0` | 103 | UnwindData |  |
| 1046 | `AuditLookupCategoryNameA` | `0x43D20` | 157 | UnwindData |  |
| 1048 | `AuditLookupSubCategoryNameA` | `0x43DD0` | 157 | UnwindData |  |
| 1050 | `AuditQueryGlobalSaclA` | `0x43E80` | 176 | UnwindData |  |
| 1055 | `AuditSetGlobalSaclA` | `0x43F40` | 176 | UnwindData |  |
| 1162 | `CredIsMarshaledCredentialA` | `0x442D0` | 68 | UnwindData |  |
| 1178 | `CredRenameA` | `0x44320` | 29 | UnwindData |  |
| 1179 | `CredRenameW` | `0x44320` | 29 | UnwindData |  |
| 1417 | `LsaAddPrivilegesToAccount` | `0x44350` | 104 | UnwindData |  |
| 1418 | `LsaClearAuditLog` | `0x443C0` | 99 | UnwindData |  |
| 1420 | `LsaConfigureAutoLogonCredentials` | `0x44430` | 86 | UnwindData |  |
| 1421 | `LsaCreateAccount` | `0x44490` | 229 | UnwindData |  |
| 1423 | `LsaCreateTrustedDomain` | `0x44580` | 229 | UnwindData |  |
| 1427 | `LsaDisableUserArso` | `0x44670` | 91 | UnwindData |  |
| 1428 | `LsaEnableUserArso` | `0x446E0` | 91 | UnwindData |  |
| 1430 | `LsaEnumerateAccounts` | `0x44750` | 188 | UnwindData |  |
| 1432 | `LsaEnumeratePrivileges` | `0x44820` | 188 | UnwindData |  |
| 1433 | `LsaEnumeratePrivilegesOfAccount` | `0x448F0` | 108 | UnwindData |  |
| 1437 | `LsaGetAppliedCAPIDs` | `0x44970` | 271 | UnwindData |  |
| 1439 | `LsaGetQuotasForAccount` | `0x44A90` | 104 | UnwindData |  |
| 1440 | `LsaGetRemoteUserName` | `0x44B00` | 290 | UnwindData |  |
| 1441 | `LsaGetSystemAccessAccount` | `0x44C30` | 104 | UnwindData |  |
| 1447 | `LsaInvokeTrustScanner` | `0x44CA0` | 102 | UnwindData |  |
| 1452 | `LsaLookupPrivilegeDisplayName` | `0x44D10` | 733 | UnwindData |  |
| 1459 | `LsaOpenAccount` | `0x45000` | 229 | UnwindData |  |
| 1461 | `LsaOpenPolicySce` | `0x450F0` | 224 | UnwindData |  |
| 1463 | `LsaOpenTrustedDomain` | `0x451E0` | 229 | UnwindData |  |
| 1465 | `LsaProfileDeleted` | `0x452D0` | 91 | UnwindData |  |
| 1466 | `LsaPurgeLocalSystemAccessTable` | `0x45340` | 146 | UnwindData |  |
| 1467 | `LsaQueryCAPs` | `0x453E0` | 273 | UnwindData |  |
| 1471 | `LsaQueryInfoTrustedDomain` | `0x45500` | 222 | UnwindData |  |
| 1473 | `LsaQueryLocalSystemAccess` | `0x455F0` | 174 | UnwindData |  |
| 1474 | `LsaQueryLocalSystemAccessAll` | `0x456B0` | 158 | UnwindData |  |
| 1476 | `LsaQuerySecurityObject` | `0x45760` | 168 | UnwindData |  |
| 1480 | `LsaRemovePrivilegesFromAccount` | `0x45810` | 111 | UnwindData |  |
| 1482 | `LsaSetCAPs` | `0x45890` | 217 | UnwindData |  |
| 1487 | `LsaSetInformationTrustedDomain` | `0x45970` | 859 | UnwindData |  |
| 1488 | `LsaSetLocalSystemAccess` | `0x45CE0` | 154 | UnwindData |  |
| 1489 | `LsaSetQuotasForAccount` | `0x45D80` | 104 | UnwindData |  |
| 1491 | `LsaSetSecurityObject` | `0x45DF0` | 303 | UnwindData |  |
| 1492 | `LsaSetSystemAccessAccount` | `0x45F30` | 103 | UnwindData |  |
| 1496 | `LsaValidateProcUniqueLuid` | `0x45FA0` | 91 | UnwindData |  |
| 1424 | `LsaCreateTrustedDomainEx` | `0x46070` | 443 | UnwindData |  |
| 1426 | `LsaDeleteTrustedDomain` | `0x46240` | 104 | UnwindData |  |
| 1435 | `LsaEnumerateTrustedDomainsEx` | `0x462B0` | 203 | UnwindData |  |
| 1464 | `LsaOpenTrustedDomainByName` | `0x46390` | 229 | UnwindData |  |
| 1468 | `LsaQueryDomainInformationPolicy` | `0x46480` | 133 | UnwindData |  |
| 1469 | `LsaQueryForestTrustInformation` | `0x46510` | 133 | UnwindData |  |
| 1470 | `LsaQueryForestTrustInformation2` | `0x465A0` | 145 | UnwindData |  |
| 1477 | `LsaQueryTrustedDomainInfo` | `0x46640` | 234 | UnwindData |  |
| 1478 | `LsaQueryTrustedDomainInfoByName` | `0x46730` | 150 | UnwindData |  |
| 1483 | `LsaSetDomainInformationPolicy` | `0x467D0` | 125 | UnwindData |  |
| 1484 | `LsaSetForestTrustInformation` | `0x46860` | 163 | UnwindData |  |
| 1485 | `LsaSetForestTrustInformation2` | `0x46910` | 178 | UnwindData |  |
| 1493 | `LsaSetTrustedDomainInfoByName` | `0x469D0` | 877 | UnwindData |  |
| 1494 | `LsaSetTrustedDomainInformation` | `0x46D50` | 238 | UnwindData |  |
| 1438 | `LsaGetDeviceRegistrationInfo` | `0x47C00` | 103 | UnwindData |  |
| 1314 | `GetLocalManagedApplications` | `0x47E60` | 807 | UnwindData |  |
| 1315 | `GetManagedApplicationCategories` | `0x48190` | 101 | UnwindData |  |
| 1316 | `GetManagedApplications` | `0x48200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1387 | `InstallApplication` | `0x48210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1815 | `UninstallApplication` | `0x48220` | 77 | UnwindData |  |
| 1390 | `IsTokenUntrusted` | `0x491B0` | 725 | UnwindData |  |
| 1712 | `SaferSetPolicyInformation` | `0x49AD0` | 149 | UnwindData |  |
| 1731 | `SetInformationCodeAuthzPolicyW` | `0x49AD0` | 149 | UnwindData |  |
| 1710 | `SaferRecordEventLogEntry` | `0x49E60` | 549 | UnwindData |  |
| 1718 | `SaferiRecordEventLogEntry` | `0x49E60` | 549 | UnwindData |  |
| 1711 | `SaferSetLevelInformation` | `0x4A570` | 177 | UnwindData |  |
| 1730 | `SetInformationCodeAuthzLevelW` | `0x4A570` | 177 | UnwindData |  |
| 1717 | `SaferiPopulateDefaultsInRegistry` | `0x4B770` | 1,690 | UnwindData |  |
| 1077 | `BuildImpersonateExplicitAccessWithNameA` | `0x4D470` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `BuildImpersonateExplicitAccessWithNameW` | `0x4D470` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1081 | `BuildSecurityDescriptorA` | `0x4D4A0` | 406 | UnwindData |  |
| 1288 | `FreeInheritedFromArray` | `0x4D640` | 65 | UnwindData |  |
| 1294 | `GetAuditedPermissionsFromAclA` | `0x4D690` | 131 | UnwindData |  |
| 1295 | `GetAuditedPermissionsFromAclW` | `0x4D720` | 154 | UnwindData |  |
| 1299 | `GetEffectiveRightsFromAclA` | `0x4D7C0` | 122 | UnwindData |  |
| 1309 | `GetInheritanceSourceA` | `0x4D840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1809 | `TreeResetNamedSecurityInfoA` | `0x4D840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1811 | `TreeSetNamedSecurityInfoA` | `0x4D840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1310 | `GetInheritanceSourceW` | `0x4D850` | 180 | UnwindData |  |
| 1414 | `LookupSecurityDescriptorPartsA` | `0x4D910` | 769 | UnwindData |  |
| 1415 | `LookupSecurityDescriptorPartsW` | `0x4DC20` | 663 | UnwindData |  |
| 1079 | `BuildImpersonateTrusteeA` | `0x4DEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1080 | `BuildImpersonateTrusteeW` | `0x4DEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `BuildTrusteeWithObjectsAndNameA` | `0x4DEE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1086 | `BuildTrusteeWithObjectsAndNameW` | `0x4DEE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1087 | `BuildTrusteeWithObjectsAndSidA` | `0x4DF40` | 121 | UnwindData |  |
| 1088 | `BuildTrusteeWithObjectsAndSidW` | `0x4DF40` | 121 | UnwindData |  |
| 1317 | `GetMultipleTrusteeA` | `0x4DFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `GetMultipleTrusteeW` | `0x4DFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1318 | `GetMultipleTrusteeOperationA` | `0x4DFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1319 | `GetMultipleTrusteeOperationW` | `0x4DFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1353 | `GetTrusteeFormA` | `0x4E000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1354 | `GetTrusteeFormW` | `0x4E000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1355 | `GetTrusteeNameA` | `0x4E020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1356 | `GetTrusteeNameW` | `0x4E020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1357 | `GetTrusteeTypeA` | `0x4E030` | 1,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1358 | `GetTrusteeTypeW` | `0x4E030` | 1,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1091 | `CancelOverlappedAccess` | `0x4E660` | 99 | UnwindData |  |
| 1113 | `ConvertAccessToSecurityDescriptorA` | `0x4E6D0` | 371 | UnwindData |  |
| 1114 | `ConvertAccessToSecurityDescriptorW` | `0x4E850` | 126 | UnwindData |  |
| 1118 | `ConvertSecurityDescriptorToAccessA` | `0x4E8E0` | 57 | UnwindData |  |
| 1119 | `ConvertSecurityDescriptorToAccessNamedA` | `0x4E8E0` | 57 | UnwindData |  |
| 1120 | `ConvertSecurityDescriptorToAccessNamedW` | `0x4E920` | 57 | UnwindData |  |
| 1121 | `ConvertSecurityDescriptorToAccessW` | `0x4E920` | 57 | UnwindData |  |
| 1290 | `GetAccessPermissionsForObjectA` | `0x4E960` | 852 | UnwindData |  |
| 1291 | `GetAccessPermissionsForObjectW` | `0x4ECC0` | 307 | UnwindData |  |
| 1322 | `GetNamedSecurityInfoExA` | `0x4EE00` | 675 | UnwindData |  |
| 1323 | `GetNamedSecurityInfoExW` | `0x4F0B0` | 806 | UnwindData |  |
| 1327 | `GetOverlappedAccessResults` | `0x4F3E0` | 310 | UnwindData |  |
| 1337 | `GetSecurityInfoExA` | `0x4F520` | 631 | UnwindData |  |
| 1338 | `GetSecurityInfoExW` | `0x4F7A0` | 812 | UnwindData |  |
| 1722 | `SetEntriesInAccessListA` | `0x4FAE0` | 70 | UnwindData |  |
| 1723 | `SetEntriesInAccessListW` | `0x4FB30` | 70 | UnwindData |  |
| 1726 | `SetEntriesInAuditListA` | `0x4FB80` | 46 | UnwindData |  |
| 1727 | `SetEntriesInAuditListW` | `0x4FBC0` | 46 | UnwindData |  |
| 1734 | `SetNamedSecurityInfoExA` | `0x4FC00` | 1,188 | UnwindData |  |
| 1735 | `SetNamedSecurityInfoExW` | `0x500B0` | 827 | UnwindData |  |
| 1747 | `SetSecurityInfoExA` | `0x50400` | 1,097 | UnwindData |  |
| 1748 | `SetSecurityInfoExW` | `0x50850` | 844 | UnwindData |  |
| 1813 | `TrusteeAccessToObjectA` | `0x50BB0` | 616 | UnwindData |  |
| 1814 | `TrusteeAccessToObjectW` | `0x50E20` | 250 | UnwindData |  |
| 1283 | `FlushTraceA` | `0x52220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1591 | `QueryTraceA` | `0x52240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1763 | `StopTraceA` | `0x52260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1819 | `UpdateTraceA` | `0x52280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1820 | `UpdateTraceW` | `0x522A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `AbortSystemShutdownA` | `0x522C0` | 167 | UnwindData |  |
| 1006 | `AbortSystemShutdownW` | `0x52370` | 116 | UnwindData |  |
| 1381 | `InitiateShutdownA` | `0x523F0` | 320 | UnwindData |  |
| 1383 | `InitiateSystemShutdownA` | `0x52540` | 334 | UnwindData |  |
| 1384 | `InitiateSystemShutdownExA` | `0x526A0` | 341 | UnwindData |  |
| 1386 | `InitiateSystemShutdownW` | `0x52800` | 286 | UnwindData |  |
| 1063 | `BaseRegCreateKey` | `0x52930` | 101 | UnwindData |  |
| 1064 | `BaseRegDeleteKeyEx` | `0x529A0` | 54 | UnwindData |  |
| 1065 | `BaseRegDeleteValue` | `0x529E0` | 44 | UnwindData |  |
| 1066 | `BaseRegFlushKey` | `0x52A20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `BaseRegGetVersion` | `0x52A50` | 44 | UnwindData |  |
| 1068 | `BaseRegLoadKey` | `0x52A90` | 49 | UnwindData |  |
| 1069 | `BaseRegOpenKey` | `0x52AD0` | 63 | UnwindData |  |
| 1070 | `BaseRegRestoreKey` | `0x52B60` | 49 | UnwindData |  |
| 1071 | `BaseRegSaveKeyEx` | `0x52BD0` | 54 | UnwindData |  |
| 1072 | `BaseRegSetKeySecurity` | `0x52C10` | 48 | UnwindData |  |
| 1073 | `BaseRegSetValue` | `0x52C50` | 62 | UnwindData |  |
| 1074 | `BaseRegUnLoadKey` | `0x52CA0` | 44 | UnwindData |  |
| 1703 | `SafeBaseRegGetKeySecurity` | `0x52CE0` | 53 | UnwindData |  |
| 1605 | `RegCopyTreeA` | `0x53160` | 118 | UnwindData |  |
| 1610 | `RegCreateKeyTransactedA` | `0x531E0` | 142 | UnwindData |  |
| 1650 | `RegOpenKeyTransactedA` | `0x53280` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1664 | `RegRenameKey` | `0x532C0` | 160 | UnwindData |  |
| 1616 | `RegDeleteKeyTransactedA` | `0x53370` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1692 | `RemoteRegEnumKeyWrapper` | `0x533B0` | 356 | UnwindData |  |
| 1693 | `RemoteRegEnumValueWrapper` | `0x53520` | 287 | UnwindData |  |
| 1697 | `RemoteRegQueryValueWrapper` | `0x53650` | 149 | UnwindData |  |
| 1665 | `RegReplaceKeyA` | `0x536F0` | 568 | UnwindData |  |
| 1669 | `RegSaveKeyA` | `0x53930` | 444 | UnwindData |  |
| 1676 | `RegSetValueA` | `0x53B00` | 356 | UnwindData |  |
| 1695 | `RemoteRegQueryMultipleValues2Wrapper` | `0x53C70` | 363 | UnwindData |  |
| 1696 | `RemoteRegQueryMultipleValuesWrapper` | `0x53DF0` | 350 | UnwindData |  |
| 1385 | `InitiateSystemShutdownExW` | `0x53F60` | 305 | UnwindData |  |
| 1666 | `RegReplaceKeyW` | `0x540A0` | 393 | UnwindData |  |
| 1251 | `EnumDependentServicesA` | `0x54340` | 430 | UnwindData |  |
| 1339 | `GetServiceDisplayNameA` | `0x54500` | 140 | UnwindData |  |
| 1341 | `GetServiceKeyNameA` | `0x545A0` | 140 | UnwindData |  |
| 1586 | `QueryServiceLockStatusA` | `0x54640` | 238 | UnwindData |  |
| 1587 | `QueryServiceLockStatusW` | `0x54740` | 238 | UnwindData |  |
| 1749 | `SetServiceBits` | `0x549F0` | 57 | UnwindData |  |
| 1816 | `UnlockServiceDatabase` | `0x54A30` | 106 | UnwindData |  |
| 1008 | `AccessCheckAndAuditAlarmA` | `0x54AA0` | 430 | UnwindData |  |
| 1011 | `AccessCheckByTypeAndAuditAlarmA` | `0x54C60` | 475 | UnwindData |  |
| 1015 | `AccessCheckByTypeResultListAndAuditAlarmByHandleA` | `0x54E50` | 490 | UnwindData |  |
| 1408 | `LookupPrivilegeDisplayNameA` | `0x55040` | 525 | UnwindData |  |
| 1409 | `LookupPrivilegeDisplayNameW` | `0x55260` | 413 | UnwindData |  |
| 1516 | `ObjectCloseAuditAlarmA` | `0x55410` | 148 | UnwindData |  |
| 1518 | `ObjectDeleteAuditAlarmA` | `0x554B0` | 148 | UnwindData |  |
| 1520 | `ObjectOpenAuditAlarmA` | `0x55550` | 435 | UnwindData |  |
| 1522 | `ObjectPrivilegeAuditAlarmA` | `0x55710` | 181 | UnwindData |  |
| 1571 | `PrivilegedServiceAuditAlarmA` | `0x557D0` | 250 | UnwindData |  |
| 1142 | `CreateProcessWithLogonW` | `0x580D0` | 116 | UnwindData |  |
| 1397 | `LogoffSecondaryUserFromSessionW` | `0x58150` | 113 | UnwindData |  |
| 1398 | `LogonSecondaryUserIntoSessionW` | `0x581D0` | 213 | UnwindData |  |
| 1399 | `LogonUserA` | `0x587E0` | 63 | UnwindData |  |
| 1400 | `LogonUserExA` | `0x589D0` | 89 | UnwindData |  |
| 1402 | `LogonUserExW` | `0x58A30` | 89 | UnwindData |  |
| 1028 | `AddConditionalAce` | `0x58A90` | 728 | UnwindData |  |
| 1347 | `GetStringConditionFromBinary` | `0x58D70` | 77 | UnwindData |  |
| 1115 | `ConvertSDToStringSDDomainW` | `0x59290` | 135 | UnwindData |  |
| 1116 | `ConvertSDToStringSDRootDomainA` | `0x59320` | 372 | UnwindData |  |
| 1117 | `ConvertSDToStringSDRootDomainW` | `0x594A0` | 120 | UnwindData |  |
| 1126 | `ConvertStringSDToSDDomainA` | `0x59520` | 316 | UnwindData |  |
| 1127 | `ConvertStringSDToSDDomainW` | `0x59670` | 198 | UnwindData |  |
| 1128 | `ConvertStringSDToSDRootDomainA` | `0x59740` | 215 | UnwindData |  |
| 1129 | `ConvertStringSDToSDRootDomainW` | `0x59820` | 105 | UnwindData |  |
| 1060 | `BackupEventLogA` | `0x5B560` | 198 | UnwindData |  |
| 1061 | `BackupEventLogW` | `0x5B630` | 185 | UnwindData |  |
| 1098 | `ClearEventLogA` | `0x5B730` | 198 | UnwindData |  |
| 1099 | `ClearEventLogW` | `0x5B800` | 185 | UnwindData |  |
| 1102 | `CloseEventLog` | `0x5B8C0` | 65 | UnwindData |  |
| 1239 | `DeregisterEventSource` | `0x5B910` | 65 | UnwindData |  |
| 1302 | `GetEventLogInformation` | `0x5B960` | 75 | UnwindData |  |
| 1325 | `GetNumberOfEventLogRecords` | `0x5B9C0` | 65 | UnwindData |  |
| 1326 | `GetOldestEventLogRecord` | `0x5BA10` | 65 | UnwindData |  |
| 1511 | `NotifyChangeEventLog` | `0x5BA60` | 65 | UnwindData |  |
| 1524 | `OpenBackupEventLogA` | `0x5BAB0` | 284 | UnwindData |  |
| 1525 | `OpenBackupEventLogW` | `0x5BBE0` | 221 | UnwindData |  |
| 1528 | `OpenEventLogA` | `0x5BCD0` | 113 | UnwindData |  |
| 1529 | `OpenEventLogW` | `0x5BD50` | 113 | UnwindData |  |
| 1598 | `ReadEventLogA` | `0x5BDD0` | 146 | UnwindData |  |
| 1599 | `ReadEventLogW` | `0x5BE70` | 148 | UnwindData |  |
| 1682 | `RegisterEventSourceA` | `0x5BF10` | 113 | UnwindData |  |
| 1683 | `RegisterEventSourceW` | `0x5BF90` | 113 | UnwindData |  |
| 1700 | `ReportEventA` | `0x5C010` | 716 | UnwindData |  |
| 1558 | `PerfRegEnumKey` | `0x5E3D0` | 84 | UnwindData |  |
| 1559 | `PerfRegEnumValue` | `0x5E430` | 404 | UnwindData |  |
| 1562 | `PerfRegSetValue` | `0x5E5D0` | 1,220 | UnwindData |  |
| 1824 | `WmiCloseBlock` | `0x60280` | 115 | UnwindData |  |
| 1825 | `WmiDevInstToInstanceNameA` | `0x60300` | 218 | UnwindData |  |
| 1826 | `WmiDevInstToInstanceNameW` | `0x603E0` | 218 | UnwindData |  |
| 1827 | `WmiEnumerateGuids` | `0x604C0` | 488 | UnwindData |  |
| 1828 | `WmiExecuteMethodA` | `0x606B0` | 244 | UnwindData |  |
| 1830 | `WmiFileHandleToInstanceNameA` | `0x607B0` | 613 | UnwindData |  |
| 1831 | `WmiFileHandleToInstanceNameW` | `0x60A20` | 516 | UnwindData |  |
| 1832 | `WmiFreeBuffer` | `0x60C30` | 67 | UnwindData |  |
| 1835 | `WmiNotificationRegistrationA` | `0x60C80` | 123 | UnwindData |  |
| 1836 | `WmiNotificationRegistrationW` | `0x60D10` | 123 | UnwindData |  |
| 1838 | `WmiQueryAllDataA` | `0x60DA0` | 106 | UnwindData |  |
| 1839 | `WmiQueryAllDataMultipleA` | `0x60E10` | 124 | UnwindData |  |
| 1840 | `WmiQueryAllDataMultipleW` | `0x60EA0` | 554 | UnwindData |  |
| 1841 | `WmiQueryAllDataW` | `0x610D0` | 623 | UnwindData |  |
| 1842 | `WmiQueryGuidInformation` | `0x61350` | 183 | UnwindData |  |
| 1843 | `WmiQuerySingleInstanceA` | `0x61410` | 220 | UnwindData |  |
| 1844 | `WmiQuerySingleInstanceMultipleA` | `0x61500` | 415 | UnwindData |  |
| 1845 | `WmiQuerySingleInstanceMultipleW` | `0x616B0` | 603 | UnwindData |  |
| 1846 | `WmiQuerySingleInstanceW` | `0x61920` | 651 | UnwindData |  |
| 1847 | `WmiReceiveNotificationsA` | `0x61BC0` | 113 | UnwindData |  |
| 1848 | `WmiReceiveNotificationsW` | `0x61C40` | 113 | UnwindData |  |
| 1849 | `WmiSetSingleInstanceA` | `0x61CC0` | 202 | UnwindData |  |
| 1850 | `WmiSetSingleInstanceW` | `0x61D90` | 468 | UnwindData |  |
| 1851 | `WmiSetSingleItemA` | `0x61F70` | 210 | UnwindData |  |
| 1852 | `WmiSetSingleItemW` | `0x62050` | 483 | UnwindData |  |
| 1833 | `WmiMofEnumerateResourcesA` | `0x62520` | 562 | UnwindData |  |
| 1834 | `WmiMofEnumerateResourcesW` | `0x62760` | 939 | UnwindData |  |
| 1104 | `CloseThreadWaitChainSession` | `0x68C50` | 215 | UnwindData |  |
| 1348 | `GetThreadWaitChain` | `0x68D30` | 658 | UnwindData |  |
| 1536 | `OpenThreadWaitChainSession` | `0x68FD0` | 392 | UnwindData |  |
