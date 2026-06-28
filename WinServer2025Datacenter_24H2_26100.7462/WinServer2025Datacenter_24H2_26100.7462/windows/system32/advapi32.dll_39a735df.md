# Binary Specification: advapi32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\advapi32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `39a735df6720821ad42ef5e2b4753b3f18c8b35297064062193399bbee97db47`
* **Total Exported Functions:** 852

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
| 1495 | `MD4Final` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD4Final` |
| 1496 | `MD4Init` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD4Init` |
| 1497 | `MD4Update` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD4Update` |
| 1498 | `MD5Final` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD5Final` |
| 1499 | `MD5Init` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD5Init` |
| 1500 | `MD5Update` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD5Update` |
| 1541 | `PerfCreateInstance` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfCreateInstance` |
| 1542 | `PerfDecrementULongCounterValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfDecrementULongCounterValue` |
| 1543 | `PerfDecrementULongLongCounterValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfDecrementULongLongCounterValue` |
| 1545 | `PerfDeleteInstance` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfDeleteInstance` |
| 1548 | `PerfIncrementULongCounterValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfIncrementULongCounterValue` |
| 1549 | `PerfIncrementULongLongCounterValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfIncrementULongLongCounterValue` |
| 1554 | `PerfQueryInstance` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfQueryInstance` |
| 1561 | `PerfSetCounterRefValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfSetCounterRefValue` |
| 1562 | `PerfSetCounterSetInfo` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfSetCounterSetInfo` |
| 1563 | `PerfSetULongCounterValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfSetULongCounterValue` |
| 1564 | `PerfSetULongLongCounterValue` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfSetULongLongCounterValue` |
| 1565 | `PerfStartProvider` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfStartProvider` |
| 1566 | `PerfStartProviderEx` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfStartProviderEx` |
| 1567 | `PerfStopProvider` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-perfcounters-l1-2-0.PerfStopProvider` |
| 1687 | `RegisterTraceGuidsA` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwRegisterTraceGuidsA` |
| 1688 | `RegisterTraceGuidsW` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwRegisterTraceGuidsW` |
| 1696 | `RemoveTraceCallback` | `0x0` | - | Forwarded | Forwarded to: `sechost.RemoveTraceCallback` |
| 1752 | `SetTraceCallback` | `0x0` | - | Forwarded | Forwarded to: `sechost.SetTraceCallback` |
| 1763 | `SystemFunction001` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction001` |
| 1764 | `SystemFunction002` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction002` |
| 1765 | `SystemFunction003` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction003` |
| 1766 | `SystemFunction004` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction004` |
| 1767 | `SystemFunction005` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction005` |
| 1768 | `SystemFunction006` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction006` |
| 1769 | `SystemFunction007` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction007` |
| 1770 | `SystemFunction008` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction008` |
| 1771 | `SystemFunction009` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction009` |
| 1772 | `SystemFunction010` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction010` |
| 1773 | `SystemFunction011` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction011` |
| 1774 | `SystemFunction012` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction012` |
| 1775 | `SystemFunction013` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction013` |
| 1776 | `SystemFunction014` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction014` |
| 1777 | `SystemFunction015` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction015` |
| 1778 | `SystemFunction016` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction016` |
| 1780 | `SystemFunction018` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction018` |
| 1782 | `SystemFunction020` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction020` |
| 1783 | `SystemFunction021` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction021` |
| 1784 | `SystemFunction022` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction022` |
| 1785 | `SystemFunction023` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction023` |
| 1786 | `SystemFunction024` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction024` |
| 1787 | `SystemFunction025` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction025` |
| 1788 | `SystemFunction026` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction026` |
| 1789 | `SystemFunction027` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction027` |
| 1790 | `SystemFunction028` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction028` |
| 1791 | `SystemFunction029` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction029` |
| 1792 | `SystemFunction030` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction030` |
| 1793 | `SystemFunction031` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction031` |
| 1794 | `SystemFunction032` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction032` |
| 1795 | `SystemFunction033` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.SystemFunction033` |
| 1796 | `SystemFunction034` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction034` |
| 1797 | `SystemFunction035` | `0x0` | - | Forwarded | Forwarded to: `CRYPTSP.CheckSignatureInFile` |
| 1798 | `SystemFunction036` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction036` |
| 1799 | `SystemFunction040` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction040` |
| 1800 | `SystemFunction041` | `0x0` | - | Forwarded | Forwarded to: `CRYPTBASE.SystemFunction041` |
| 1801 | `TraceEvent` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwLogTraceEvent` |
| 1802 | `TraceEventInstance` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwTraceEventInstance` |
| 1803 | `TraceMessage` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwTraceMessage` |
| 1804 | `TraceMessageVa` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwTraceMessageVa` |
| 1805 | `TraceQueryInformation` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-eventing-controller-l1-1-0.TraceQueryInformation` |
| 1816 | `UnregisterTraceGuids` | `0x0` | - | Forwarded | Forwarded to: `ntdll.EtwUnregisterTraceGuids` |
| 1555 | `PerfRegCloseKey` | `0x1490` | 1,120 | UnwindData |  |
| 1552 | `PerfQueryCounterInfo` | `0x6620` | 313 | UnwindData |  |
| 1553 | `PerfQueryCounterSetRegistrationInfo` | `0x6D90` | 392 | UnwindData |  |
| 1540 | `PerfCloseQueryHandle` | `0x6F20` | 191 | UnwindData |  |
| 1551 | `PerfQueryCounterData` | `0x6FF0` | 313 | UnwindData |  |
| 1550 | `PerfOpenQueryHandle` | `0x7130` | 387 | UnwindData |  |
| 1547 | `PerfEnumerateCounterSetInstances` | `0x76E0` | 337 | UnwindData |  |
| 1107 | `ComputeAccessTokenFromCodeAuthzLevel` | `0x12400` | 757 | UnwindData |  |
| 1703 | `SaferComputeTokenFromLevel` | `0x12400` | 757 | UnwindData |  |
| 1712 | `SaferiCompareTokenLevels` | `0x132C0` | 127 | UnwindData |  |
| 1713 | `SaferiIsDllAllowed` | `0x14FB0` | 376 | UnwindData |  |
| 1373 | `IdentifyCodeAuthzLevelW` | `0x15130` | 2,204 | UnwindData |  |
| 1707 | `SaferIdentifyLevel` | `0x15130` | 2,204 | UnwindData |  |
| 1714 | `SaferiIsExecutableFileType` | `0x17F30` | 139 | UnwindData |  |
| 1711 | `SaferiChangeRegistryScope` | `0x184E0` | 42 | UnwindData |  |
| 1132 | `ConvertStringSidToSidA` | `0x18780` | 175 | UnwindData |  |
| 1133 | `ConvertStringSidToSidW` | `0x18890` | 558 | UnwindData |  |
| 1131 | `ConvertStringSecurityDescriptorToSecurityDescriptorW` | `0x1C990` | 102 | UnwindData |  |
| 1125 | `ConvertSidToStringSidW` | `0x1CA30` | 321 | UnwindData |  |
| 1409 | `LookupPrivilegeNameW` | `0x1CBD0` | 382 | UnwindData |  |
| 1411 | `LookupPrivilegeValueW` | `0x1CD60` | 280 | UnwindData |  |
| 1452 | `LsaLookupPrivilegeValue` | `0x1D150` | 131 | UnwindData |  |
| 1451 | `LsaLookupPrivilegeName` | `0x1D1E0` | 155 | UnwindData |  |
| 1410 | `LookupPrivilegeValueA` | `0x1E700` | 256 | UnwindData |  |
| 1130 | `ConvertStringSecurityDescriptorToSecurityDescriptorA` | `0x1E810` | 203 | UnwindData |  |
| 1632 | `RegEnumValueW` | `0x25180` | 67 | UnwindData |  |
| 1255 | `EnumServicesStatusA` | `0x252D0` | 554 | UnwindData |  |
| 1258 | `EnumServicesStatusW` | `0x25570` | 70 | UnwindData |  |
| 1254 | `EnumServiceGroupW` | `0x255C0` | 635 | UnwindData |  |
| 1654 | `RegQueryInfoKeyW` | `0x25ED0` | 121 | UnwindData |  |
| 1611 | `RegDeleteKeyA` | `0x25F50` | 110 | UnwindData |  |
| 1618 | `RegDeleteKeyW` | `0x25FD0` | 286 | UnwindData |  |
| 1124 | `ConvertSidToStringSidA` | `0x27090` | 608 | UnwindData |  |
| 1647 | `RegOpenKeyExW` | `0x27300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1402 | `LookupAccountNameA` | `0x27320` | 656 | UnwindData |  |
| 1404 | `LookupAccountSidA` | `0x275C0` | 735 | UnwindData |  |
| 1403 | `LookupAccountNameW` | `0x278B0` | 164 | UnwindData |  |
| 1405 | `LookupAccountSidW` | `0x27960` | 164 | UnwindData |  |
| 1630 | `RegEnumKeyW` | `0x27F00` | 70 | UnwindData |  |
| 1598 | `RegCloseKey` | `0x287B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1660 | `RegQueryValueExW` | `0x287D0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1658 | `RegQueryValueA` | `0x28950` | 642 | UnwindData |  |
| 1661 | `RegQueryValueW` | `0x28BE0` | 647 | UnwindData |  |
| 1143 | `CreateProcessWithTokenW` | `0x29480` | 102 | UnwindData |  |
| 1324 | `GetNamedSecurityInfoW` | `0x2ADC0` | 67 | UnwindData |  |
| 1650 | `RegOpenKeyW` | `0x2AE30` | 99 | UnwindData |  |
| 1533 | `OpenThreadToken` | `0x2AEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1440 | `LsaGetUserName` | `0x2AEC0` | 271 | UnwindData |  |
| 1394 | `IsValidSid` | `0x2AFE0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1528 | `OpenProcessToken` | `0x2B070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1646 | `RegOpenKeyExA` | `0x2B090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1722 | `SetEntriesInAclA` | `0x2B0B0` | 650 | UnwindData |  |
| 1321 | `GetNamedSecurityInfoA` | `0x2B340` | 168 | UnwindData |  |
| 1731 | `SetNamedSecurityInfoA` | `0x2B3F0` | 155 | UnwindData |  |
| 1649 | `RegOpenKeyTransactedW` | `0x2B5A0` | 1,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1546 | `PerfEnumerateCounterSet` | `0x2BC60` | 299 | UnwindData |  |
| 1631 | `RegEnumValueA` | `0x2BED0` | 67 | UnwindData |  |
| 1349 | `GetTokenInformation` | `0x2BF20` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1453 | `LsaLookupSids` | `0x2C420` | 38 | UnwindData |  |
| 1558 | `PerfRegQueryInfoKey` | `0x2CC20` | 1,007 | UnwindData |  |
| 1559 | `PerfRegQueryValue` | `0x2D120` | 65 | UnwindData |  |
| 1336 | `GetSecurityInfo` | `0x2E020` | 67 | UnwindData |  |
| 1609 | `RegCreateKeyTransactedW` | `0x2E070` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `EnumServicesStatusExW` | `0x2E0B0` | 96 | UnwindData |  |
| 1659 | `RegQueryValueExA` | `0x2E120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1636 | `RegGetValueW` | `0x2E140` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1300 | `GetEffectiveRightsFromAclW` | `0x2E270` | 166 | UnwindData |  |
| 1808 | `TreeResetNamedSecurityInfoW` | `0x2E320` | 259 | UnwindData |  |
| 1810 | `TreeSetNamedSecurityInfoW` | `0x2E430` | 252 | UnwindData |  |
| 1082 | `BuildSecurityDescriptorW` | `0x2E710` | 987 | UnwindData |  |
| 1717 | `SaferiSearchMatchingHashRules` | `0x2F0B0` | 489 | UnwindData |  |
| 1312 | `GetLengthSid` | `0x2F2A0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1378 | `InitializeAcl` | `0x2F6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1628 | `RegEnumKeyExA` | `0x2F6C0` | 67 | UnwindData |  |
| 1629 | `RegEnumKeyExW` | `0x2F710` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1135 | `CopySid` | `0x2F950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1034 | `AllocateAndInitializeSid` | `0x2F970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1835 | `WmiOpenBlock` | `0x2F990` | 256 | UnwindData |  |
| 1297 | `GetCurrentHwProfileW` | `0x2FAA0` | 799 | UnwindData |  |
| 1219 | `CryptHashData` | `0x30340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1360 | `GetUserNameW` | `0x30360` | 36 | UnwindData |  |
| 1700 | `RevertToSelf` | `0x30390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1606 | `RegCreateKeyExA` | `0x303B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1456 | `LsaNtStatusToWinError` | `0x303D0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1676 | `RegSetValueExW` | `0x30530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1379 | `InitializeSecurityDescriptor` | `0x30550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1259 | `EnumerateTraceGuids` | `0x30570` | 461 | UnwindData |  |
| 1359 | `GetUserNameA` | `0x30750` | 36 | UnwindData |  |
| 1653 | `RegQueryInfoKeyA` | `0x308D0` | 121 | UnwindData |  |
| 1501 | `MIDL_user_free_Ext` | `0x30950` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1141 | `CreateProcessAsUserW` | `0x309C0` | 107 | UnwindData |  |
| 1263 | `EqualSid` | `0x30A40` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1607 | `RegCreateKeyExW` | `0x30AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1293 | `GetAclInformation` | `0x30B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1750 | `SetThreadToken` | `0x30B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `CryptGetHashParam` | `0x30B50` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `CryptCreateHash` | `0x30C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1739 | `SetSecurityDescriptorDacl` | `0x30C70` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1097 | `CheckTokenMembership` | `0x30D10` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1610 | `RegCreateKeyW` | `0x30EC0` | 124 | UnwindData |  |
| 1538 | `OperationStart` | `0x30F50` | 225 | UnwindData |  |
| 1103 | `CloseServiceHandle` | `0x31040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `BuildTrusteeWithSidA` | `0x31060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1090 | `BuildTrusteeWithSidW` | `0x31060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1375 | `ImpersonateLoggedOnUser` | `0x31080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1123 | `ConvertSecurityDescriptorToStringSecurityDescriptorW` | `0x310A0` | 204 | UnwindData |  |
| 1537 | `OperationEnd` | `0x31180` | 229 | UnwindData |  |
| 1645 | `RegOpenKeyA` | `0x313D0` | 96 | UnwindData |  |
| 1201 | `CryptDestroyHash` | `0x31440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1643 | `RegNotifyChangeKeyValue` | `0x31460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1136 | `CreateCodeAuthzLevel` | `0x31480` | 192 | UnwindData |  |
| 1704 | `SaferCreateLevel` | `0x31480` | 192 | UnwindData |  |
| 1675 | `RegSetValueExA` | `0x31770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `AccessCheck` | `0x31790` | 67 | UnwindData |  |
| 1434 | `LsaFreeMemory` | `0x317E0` | 24 | UnwindData |  |
| 1380 | `InitializeSid` | `0x31800` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1530 | `OpenSCManagerW` | `0x31850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `CryptImportKey` | `0x31870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1345 | `GetSidSubAuthority` | `0x31890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `FreeSid` | `0x318B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1344 | `GetSidLengthRequired` | `0x318D0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `CheckForHiberboot` | `0x31A40` | 42 | UnwindData |  |
| 1532 | `OpenServiceW` | `0x32220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1243 | `DuplicateTokenEx` | `0x32240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `AddAce` | `0x32260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1635 | `RegGetValueA` | `0x32280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `CryptAcquireContextW` | `0x322A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1100 | `CloseCodeAuthzLevel` | `0x322C0` | 42 | UnwindData |  |
| 1702 | `SaferCloseLevel` | `0x322C0` | 42 | UnwindData |  |
| 1033 | `AdjustTokenPrivileges` | `0x323C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1627 | `RegEnumKeyA` | `0x323E0` | 67 | UnwindData |  |
| 1292 | `GetAce` | `0x32430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1388 | `IsTextUnicode` | `0x32450` | 31 | UnwindData |  |
| 1330 | `GetSecurityDescriptorDacl` | `0x32480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1329 | `GetSecurityDescriptorControl` | `0x324A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `GetSecurityDescriptorLength` | `0x324C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1346 | `GetSidSubAuthorityCount` | `0x324E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1744 | `SetSecurityInfo` | `0x32500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `QueryServiceStatusEx` | `0x32520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1749 | `SetServiceStatus` | `0x32540` | 1,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1333 | `GetSecurityDescriptorOwner` | `0x32CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1075 | `BuildExplicitAccessWithNameA` | `0x32CD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `BuildExplicitAccessWithNameW` | `0x32CD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1622 | `RegDeleteValueW` | `0x32D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `CryptDecrypt` | `0x32D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1242 | `DuplicateToken` | `0x32D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `CommandLineFromMsiDescriptor` | `0x32D60` | 910 | UnwindData |  |
| 1210 | `CryptExportKey` | `0x33460` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1587 | `QueryServiceStatus` | `0x340A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `CryptGenRandom` | `0x340C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1723 | `SetEntriesInAclW` | `0x340E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `CryptSetHashParam` | `0x34100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1507 | `MapGenericMask` | `0x34120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1582 | `QueryServiceConfigW` | `0x34140` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1222 | `CryptReleaseContext` | `0x34200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `PerfAddCounters` | `0x34220` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1623 | `RegDisablePredefinedCache` | `0x34290` | 41 | UnwindData |  |
| 1605 | `RegCreateKeyA` | `0x342C0` | 124 | UnwindData |  |
| 1112 | `ControlTraceW` | `0x34350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `CryptAcquireContextA` | `0x34370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1506 | `MakeSelfRelativeSD` | `0x34390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1308 | `GetInformationCodeAuthzPolicyW` | `0x343B0` | 52 | UnwindData |  |
| 1706 | `SaferGetPolicyInformation` | `0x343B0` | 52 | UnwindData |  |
| 1335 | `GetSecurityDescriptorSacl` | `0x34490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1620 | `RegDeleteTreeW` | `0x344B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `CreateWellKnownSid` | `0x344D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1602 | `RegConnectRegistryW` | `0x344F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `AddAccessAllowedAce` | `0x34550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `CryptDestroyKey` | `0x34570` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1573 | `ProcessTrace` | `0x34630` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1244 | `EnableTrace` | `0x34670` | 130 | UnwindData |  |
| 1751 | `SetTokenInformation` | `0x34700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1245 | `EnableTraceEx` | `0x34720` | 207 | UnwindData |  |
| 1083 | `BuildTrusteeWithNameA` | `0x34800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1084 | `BuildTrusteeWithNameW` | `0x34800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `CreatePrivateObjectSecurity` | `0x34820` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1692 | `RemoteRegQueryInfoKeyWrapper` | `0x34B80` | 235 | UnwindData |  |
| 1240 | `DestroyPrivateObjectSecurity` | `0x34D70` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1621 | `RegDeleteValueA` | `0x34F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1393 | `IsValidSecurityDescriptor` | `0x34F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1644 | `RegOpenCurrentUser` | `0x34F90` | 5,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `CreateRestrictedToken` | `0x36320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1458 | `LsaOpenPolicy` | `0x36340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `GetSecurityDescriptorGroup` | `0x36350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1216 | `CryptGetKeyParam` | `0x36370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1634 | `RegGetKeySecurity` | `0x36390` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1734 | `SetNamedSecurityInfoW` | `0x365C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1568 | `PrivilegeCheck` | `0x365E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1417 | `LsaClose` | `0x36660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1260 | `EnumerateTraceGuidsEx` | `0x36670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `AddAccessAllowedAceEx` | `0x36690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1197 | `CryptContextAddRef` | `0x366B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `ConvertSecurityDescriptorToStringSecurityDescriptorA` | `0x366D0` | 498 | UnwindData |  |
| 1306 | `GetFileSecurityW` | `0x368D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1591 | `QueryTraceW` | `0x368F0` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1140 | `CreateProcessAsUserA` | `0x36C10` | 107 | UnwindData |  |
| 1014 | `AccessCheckByTypeResultListAndAuditAlarmA` | `0x36C90` | 484 | UnwindData |  |
| 1342 | `GetServiceKeyNameW` | `0x36E80` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1673 | `RegSetKeyValueW` | `0x37030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1246 | `EnableTraceEx2` | `0x37050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | *Ordinal Only* | `0x37070` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1529 | `OpenSCManagerA` | `0x370D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `RegLoadMUIStringW` | `0x370F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1377 | `ImpersonateSelf` | `0x37110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1382 | `InitiateShutdownW` | `0x37130` | 271 | UnwindData |  |
| 1531 | `OpenServiceA` | `0x37270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1108 | `ControlService` | `0x37290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1504 | `MakeAbsoluteSD` | `0x372B0` | 109 | UnwindData |  |
| 1395 | `IsWellKnownSid` | `0x37330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1613 | `RegDeleteKeyExW` | `0x37350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `GetLocalManagedApplicationData` | `0x37370` | 633 | UnwindData |  |
| 1580 | `QueryServiceConfig2W` | `0x375F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1615 | `RegDeleteKeyTransactedW` | `0x37610` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1205 | `CryptEncrypt` | `0x37650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1389 | `IsTokenRestricted` | `0x37670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `FlushTraceW` | `0x37690` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1581 | `QueryServiceConfigA` | `0x376E0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1139 | `CreatePrivateObjectSecurityWithMultipleInheritance` | `0x37880` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1625 | `RegDisableReflectionKey` | `0x37960` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1626 | `RegEnableReflectionKey` | `0x37960` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1740 | `SetSecurityDescriptorGroup` | `0x37D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1340 | `GetServiceDisplayNameW` | `0x37D50` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1155 | `CredEnumerateW` | `0x37F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1158 | `CredFree` | `0x37F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1307 | `GetInformationCodeAuthzLevelW` | `0x37F60` | 183 | UnwindData |  |
| 1705 | `SaferGetLevelInformation` | `0x37F60` | 183 | UnwindData |  |
| 1727 | `SetFileSecurityW` | `0x383D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1237 | `DeleteAce` | `0x383F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1224 | `CryptSetKeyParam` | `0x38410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1200 | `CryptDeriveKey` | `0x38430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1343 | `GetSidIdentifierAuthority` | `0x38450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1536 | `OpenTraceW` | `0x38470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1147 | `CreateServiceW` | `0x38490` | 130 | UnwindData |  |
| 1105 | `CloseTrace` | `0x38770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1214 | `CryptGetDefaultProviderW` | `0x38790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1760 | `StartTraceW` | `0x387B0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1656 | `RegQueryMultipleValuesW` | `0x38D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1095 | `ChangeServiceConfigW` | `0x38D80` | 109 | UnwindData |  |
| 1182 | `CredUnmarshalCredentialW` | `0x38E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1689 | `RegisterWaitChainCOMCallback` | `0x38E20` | 183 | UnwindData |  |
| 1600 | `RegConnectRegistryExA` | `0x38EE0` | 164 | UnwindData |  |
| 1601 | `RegConnectRegistryExW` | `0x38F90` | 261 | UnwindData |  |
| 1508 | `NotifyBootConfigStatus` | `0x390A0` | 102 | UnwindData |  |
| 1671 | `RegSetKeySecurity` | `0x39110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1741 | `SetSecurityDescriptorOwner` | `0x39130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1726 | `SetFileSecurityA` | `0x39150` | 176 | UnwindData |  |
| 1374 | `ImpersonateAnonymousToken` | `0x39210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1203 | `CryptDuplicateHash` | `0x39230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1815 | `UnregisterIdleTask` | `0x39250` | 17 | UnwindData |  |
| 1249 | `EncryptedFileKeyInfo` | `0x397F0` | 122 | UnwindData |  |
| 1447 | `LsaIsUserArsoEnabled` | `0x39870` | 99 | UnwindData |  |
| 1757 | `StartServiceCtrlDispatcherW` | `0x398E0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1252 | `EnumDependentServicesW` | `0x39B60` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1535 | `OpenTraceA` | `0x39C50` | 229 | UnwindData |  |
| 1401 | `LogonUserW` | `0x39E40` | 63 | UnwindData |  |
| 1470 | `LsaQueryInformationPolicy` | `0x39F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1633 | `RegFlushKey` | `0x39FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1233 | `CryptVerifySignatureW` | `0x39FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1743 | `SetSecurityDescriptorSacl` | `0x39FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1177 | `CredReadW` | `0x3A000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1311 | `GetKernelObjectSecurity` | `0x3A020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1762 | `StopTraceW` | `0x3A040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `AreAllAccessesGranted` | `0x3A060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1651 | `RegOpenUserClassesRoot` | `0x3A080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `CryptGetProvParam` | `0x3A0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `AuditQuerySystemPolicy` | `0x3A0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1758 | `StartServiceW` | `0x3A0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1446 | `LsaIsUserArsoAllowed` | `0x3A100` | 94 | UnwindData |  |
| 1376 | `ImpersonateNamedPipeClient` | `0x3A170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1677 | `RegSetValueW` | `0x3A190` | 367 | UnwindData |  |
| 1544 | `PerfDeleteCounters` | `0x3A310` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `CryptGenKey` | `0x3A3A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `RegisterServiceCtrlHandlerW` | `0x3A410` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `RegDeleteKeyValueW` | `0x3A4C0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1361 | `GetWindowsAccountDomainSid` | `0x3A660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `AddAccessDeniedAce` | `0x3A680` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `AuditQueryPerUserPolicy` | `0x3AA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1449 | `LsaLookupNames2` | `0x3AA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1204 | `CryptDuplicateKey` | `0x3AA60` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `AllocateLocallyUniqueId` | `0x3AB90` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1738 | `SetSecurityDescriptorControl` | `0x3ACB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1305 | `GetFileSecurityA` | `0x3ACD0` | 201 | UnwindData |  |
| 1699 | `ReportEventW` | `0x3ADA0` | 534 | UnwindData |  |
| 1043 | `AuditFree` | `0x3B170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `CryptVerifySignatureA` | `0x3B190` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1513 | `NpGetUserName` | `0x3B4E0` | 354 | UnwindData |  |
| 1218 | `CryptGetUserKey` | `0x3B650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1188 | `CredWriteW` | `0x3B670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1296 | `GetCurrentHwProfileA` | `0x3B690` | 303 | UnwindData |  |
| 1429 | `LsaEnumerateAccountsWithUserRight` | `0x3B7D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1391 | `IsValidAcl` | `0x3B7E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1685 | `RegisterServiceCtrlHandlerExW` | `0x3B800` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1511 | `NotifyServiceStatusChangeA` | `0x3BB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1604 | `RegCopyTreeW` | `0x3BB30` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1455 | `LsaManageSidNameMapping` | `0x3BCF0` | 281 | UnwindData |  |
| 1512 | `NotifyServiceStatusChangeW` | `0x3BE10` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1396 | `LockServiceDatabase` | `0x3BEB0` | 110 | UnwindData |  |
| 1612 | `RegDeleteKeyExA` | `0x3BF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1670 | `RegSaveKeyW` | `0x3BF50` | 384 | UnwindData |  |
| 1730 | `SetKernelObjectSecurity` | `0x3C0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1093 | `ChangeServiceConfig2W` | `0x3C100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1152 | `CredDeleteW` | `0x3C120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1256 | `EnumServicesStatusExA` | `0x3C140` | 589 | UnwindData |  |
| 1432 | `LsaEnumerateTrustedDomains` | `0x3C540` | 203 | UnwindData |  |
| 1575 | `QueryAllTracesW` | `0x3CEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1280 | `FileEncryptionStatusW` | `0x3CED0` | 75 | UnwindData |  |
| 1408 | `LookupPrivilegeNameA` | `0x3CF50` | 433 | UnwindData |  |
| 1599 | `RegConnectRegistryA` | `0x3D110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1208 | `CryptEnumProvidersA` | `0x3D130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1448 | `LsaLookupNames` | `0x3D150` | 392 | UnwindData |  |
| 1059 | `AuditSetSystemPolicy` | `0x3D440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1652 | `RegOverridePredefKey` | `0x3D460` | 102 | UnwindData |  |
| 1264 | `EventAccessControl` | `0x3D630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1225 | `CryptSetProvParam` | `0x3D650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1827 | `WmiExecuteMethodW` | `0x3D670` | 876 | UnwindData |  |
| 1062 | `BaseRegCloseKey` | `0x3DB50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1285 | `FreeEncryptedFileKeyInfo` | `0x3DB80` | 38 | UnwindData |  |
| 1287 | `FreeEncryptionCertificateHashList` | `0x3DBB0` | 35 | UnwindData |  |
| 1672 | `RegSetKeyValueA` | `0x3DCB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1755 | `StartServiceA` | `0x3DCD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1238 | `DeleteService` | `0x3DCF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `GetExplicitEntriesFromAclA` | `0x3DD10` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `GetExplicitEntriesFromAclW` | `0x3DD10` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1579 | `QueryServiceConfig2A` | `0x3E090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1756 | `StartServiceCtrlDispatcherA` | `0x3E0B0` | 3,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1262 | `EqualPrefixSid` | `0x3EE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1185 | `CredWriteA` | `0x3EE60` | 1,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1682 | `RegisterIdleTask` | `0x3F500` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1640 | `RegLoadKeyW` | `0x3F5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1092 | `ChangeServiceConfig2A` | `0x3F5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1748 | `SetServiceObjectSecurity` | `0x3F5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1586 | `QueryServiceObjectSecurity` | `0x3F610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `CredDeleteA` | `0x3F630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `AddAuditAccessAce` | `0x3F650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `AuditSetGlobalSaclW` | `0x3F670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `CryptEnumProvidersW` | `0x3F690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1638 | `RegLoadAppKeyW` | `0x3F6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `CredReadA` | `0x3F6D0` | 1,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1427 | `LsaEnumerateAccountRights` | `0x3FC50` | 2,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1111 | `ControlTraceA` | `0x40540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1574 | `QueryAllTracesA` | `0x40550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1759 | `StartTraceA` | `0x40560` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1510 | `NotifyServiceStatusChange` | `0x406D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `CreateServiceEx` | `0x406E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1367 | `I_ScReparseServiceDatabase` | `0x406F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1576 | `QueryLocalUserServiceName` | `0x40700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1592 | `QueryUserServiceName` | `0x40710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `QueryUserServiceNameForContext` | `0x40720` | 5,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1030 | `AddUsersToEncryptedFile` | `0x41D30` | 106 | UnwindData |  |
| 1031 | `AddUsersToEncryptedFileEx` | `0x41DA0` | 141 | UnwindData |  |
| 1101 | `CloseEncryptedFileRaw` | `0x41E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1235 | `DecryptFileA` | `0x41E60` | 199 | UnwindData |  |
| 1236 | `DecryptFileW` | `0x41F30` | 124 | UnwindData |  |
| 1241 | `DuplicateEncryptionInfoFile` | `0x41FC0` | 148 | UnwindData |  |
| 1247 | `EncryptFileA` | `0x42060` | 183 | UnwindData |  |
| 1248 | `EncryptFileW` | `0x42120` | 110 | UnwindData |  |
| 1250 | `EncryptionDisable` | `0x421A0` | 73 | UnwindData |  |
| 1279 | `FileEncryptionStatusA` | `0x421F0` | 201 | UnwindData |  |
| 1282 | `FlushEfsCache` | `0x422C0` | 133 | UnwindData |  |
| 1286 | `FreeEncryptedFileMetadata` | `0x42350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1301 | `GetEncryptedFileMetadata` | `0x42360` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `I_ScGetCurrentGroupStateW` | `0x42360` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1719 | `SetEncryptedFileMetadata` | `0x42360` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1524 | `OpenEncryptedFileRawA` | `0x424A0` | 183 | UnwindData |  |
| 1525 | `OpenEncryptedFileRawW` | `0x42560` | 103 | UnwindData |  |
| 1577 | `QueryRecoveryAgentsOnEncryptedFile` | `0x425D0` | 106 | UnwindData |  |
| 1594 | `QueryUsersOnEncryptedFile` | `0x42640` | 106 | UnwindData |  |
| 1595 | `ReadEncryptedFileRaw` | `0x426B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1697 | `RemoveUsersFromEncryptedFile` | `0x426D0` | 106 | UnwindData |  |
| 1753 | `SetUserFileEncryptionKey` | `0x42740` | 80 | UnwindData |  |
| 1754 | `SetUserFileEncryptionKeyEx` | `0x427A0` | 115 | UnwindData |  |
| 1819 | `UsePinForEncryptedFilesA` | `0x42820` | 127 | UnwindData |  |
| 1820 | `UsePinForEncryptedFilesW` | `0x428B0` | 151 | UnwindData |  |
| 1851 | `WriteEncryptedFileRaw` | `0x42950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `AccessCheckAndAuditAlarmW` | `0x42970` | 107 | UnwindData |  |
| 1012 | `AccessCheckByTypeAndAuditAlarmW` | `0x429F0` | 170 | UnwindData |  |
| 1016 | `AccessCheckByTypeResultListAndAuditAlarmByHandleW` | `0x42AA0` | 182 | UnwindData |  |
| 1017 | `AccessCheckByTypeResultListAndAuditAlarmW` | `0x42B60` | 170 | UnwindData |  |
| 1013 | `AccessCheckByTypeResultList` | `0x42C10` | 108 | UnwindData |  |
| 1010 | `AccessCheckByType` | `0x42C90` | 108 | UnwindData |  |
| 1020 | `AddAccessAllowedObjectAce` | `0x42D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `AddAccessDeniedAceEx` | `0x42D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `AddAccessDeniedObjectAce` | `0x42D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `AddAuditAccessAceEx` | `0x42D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `AddAuditAccessObjectAce` | `0x42D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `AdjustTokenGroups` | `0x42DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `AreAnyAccessesGranted` | `0x42DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `AuditComputeEffectivePolicyBySid` | `0x42DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1040 | `AuditEnumerateCategories` | `0x42E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | `AuditEnumeratePerUserPolicy` | `0x42E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1042 | `AuditEnumerateSubCategories` | `0x42E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1047 | `AuditLookupCategoryNameW` | `0x42E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1049 | `AuditLookupSubCategoryNameW` | `0x42E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1051 | `AuditQueryGlobalSaclW` | `0x42EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1053 | `AuditQuerySecurity` | `0x42ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `AuditSetPerUserPolicy` | `0x42EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `AuditSetSecurity` | `0x42F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1094 | `ChangeServiceConfigA` | `0x42F30` | 109 | UnwindData |  |
| 1109 | `ControlServiceExA` | `0x42FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1110 | `ControlServiceExW` | `0x42FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1134 | `ConvertToAutoInheritPrivateObjectSecurity` | `0x42FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `CreatePrivateObjectSecurityEx` | `0x43010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `CreateServiceA` | `0x43030` | 130 | UnwindData |  |
| 1150 | `CredBackupCredentials` | `0x430C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1153 | `CredEncryptAndMarshalBinaryBlob` | `0x430E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1154 | `CredEnumerateA` | `0x43100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1156 | `CredFindBestCredentialA` | `0x43120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1157 | `CredFindBestCredentialW` | `0x43140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1159 | `CredGetSessionTypes` | `0x43160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1160 | `CredGetTargetInfoA` | `0x43180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1161 | `CredGetTargetInfoW` | `0x431A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1163 | `CredIsMarshaledCredentialW` | `0x431C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1164 | `CredIsProtectedA` | `0x431E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1165 | `CredIsProtectedW` | `0x43200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1166 | `CredMarshalCredentialA` | `0x43220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `CredMarshalCredentialW` | `0x43240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1169 | `CredProfileLoadedEx` | `0x43260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1168 | `CredProfileLoaded` | `0x43280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1170 | `CredProfileUnloaded` | `0x432A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `CredProtectA` | `0x432C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1172 | `CredProtectW` | `0x432E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `CredReadByTokenHandle` | `0x43300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `CredReadDomainCredentialsA` | `0x43320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1176 | `CredReadDomainCredentialsW` | `0x43340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `CredRestoreCredentials` | `0x43360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1181 | `CredUnmarshalCredentialA` | `0x43380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1183 | `CredUnprotectA` | `0x433A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1184 | `CredUnprotectW` | `0x433C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1186 | `CredWriteDomainCredentialsA` | `0x433E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `CredWriteDomainCredentialsW` | `0x43400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1189 | `CredpConvertCredential` | `0x43420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1190 | `CredpConvertOneCredentialSize` | `0x43440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1191 | `CredpConvertTargetInfo` | `0x43460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1192 | `CredpDecodeCredential` | `0x43480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `CredpEncodeCredential` | `0x434A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1194 | `CredpEncodeSecret` | `0x434C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1206 | `CryptEnumProviderTypesA` | `0x434E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `CryptEnumProviderTypesW` | `0x43500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `CryptGetDefaultProviderA` | `0x43520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `CryptHashSessionKey` | `0x43540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `CryptSetProviderA` | `0x43560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `CryptSetProviderExA` | `0x43580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1228 | `CryptSetProviderExW` | `0x435A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1229 | `CryptSetProviderW` | `0x435C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `CryptSignHashA` | `0x435E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `CryptSignHashW` | `0x43600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `EnumDynamicTimeZoneInformation` | `0x43620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1261 | `EqualDomainSid` | `0x43640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1265 | `EventAccessQuery` | `0x43660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1266 | `EventAccessRemove` | `0x43680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1281 | `FindFirstFreeAce` | `0x436A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1298 | `GetDynamicTimeZoneInformationEffectiveYears` | `0x436C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `GetPrivateObjectSecurity` | `0x436E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `GetSecurityDescriptorRMControl` | `0x43700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1370 | `I_ScSetServiceBitsA` | `0x43720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1371 | `I_ScSetServiceBitsW` | `0x43740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1399 | `LogonUserExExW` | `0x43760` | 108 | UnwindData |  |
| 1414 | `LsaAddAccountRights` | `0x437E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1420 | `LsaCreateSecret` | `0x437F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1423 | `LsaDelete` | `0x43800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1441 | `LsaICLookupNames` | `0x43810` | 88 | UnwindData |  |
| 1442 | `LsaICLookupNamesWithCreds` | `0x43870` | 111 | UnwindData |  |
| 1443 | `LsaICLookupSids` | `0x438F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `LsaICLookupSidsWithCreds` | `0x43900` | 111 | UnwindData |  |
| 1454 | `LsaLookupSids2` | `0x43980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1460 | `LsaOpenSecret` | `0x43990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1473 | `LsaQuerySecret` | `0x439A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1477 | `LsaRemoveAccountRights` | `0x439B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `LsaRetrievePrivateData` | `0x439C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1484 | `LsaSetInformationPolicy` | `0x439D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1488 | `LsaSetSecret` | `0x439E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1493 | `LsaStorePrivateData` | `0x439F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `MakeAbsoluteSD2` | `0x43A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1515 | `ObjectCloseAuditAlarmW` | `0x43A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1517 | `ObjectDeleteAuditAlarmW` | `0x43A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1519 | `ObjectOpenAuditAlarmW` | `0x43A60` | 117 | UnwindData |  |
| 1521 | `ObjectPrivilegeAuditAlarmW` | `0x43AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1570 | `PrivilegedServiceAuditAlarmW` | `0x43B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1578 | `QuerySecurityAccessMask` | `0x43B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1583 | `QueryServiceDynamicInformation` | `0x43B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1590 | `QueryTraceProcessingHandle` | `0x43B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1616 | `RegDeleteKeyValueA` | `0x43B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1619 | `RegDeleteTreeA` | `0x43BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1624 | `RegDisablePredefinedCacheEx` | `0x43BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1637 | `RegLoadAppKeyA` | `0x43BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1639 | `RegLoadKeyA` | `0x43C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1641 | `RegLoadMUIStringA` | `0x43C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1655 | `RegQueryMultipleValuesA` | `0x43C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1665 | `RegRestoreKeyA` | `0x43C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1666 | `RegRestoreKeyW` | `0x43C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `RegSaveKeyExA` | `0x43CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1669 | `RegSaveKeyExW` | `0x43CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1678 | `RegUnLoadKeyA` | `0x43CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1679 | `RegUnLoadKeyW` | `0x43D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1683 | `RegisterServiceCtrlHandlerA` | `0x43D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1684 | `RegisterServiceCtrlHandlerExA` | `0x43D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1718 | `SetAclInformation` | `0x43D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1736 | `SetPrivateObjectSecurityEx` | `0x43D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1735 | `SetPrivateObjectSecurity` | `0x43DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1737 | `SetSecurityAccessMask` | `0x43DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1742 | `SetSecurityDescriptorRMControl` | `0x43DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1806 | `TraceSetInformation` | `0x43E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1821 | `WaitServiceState` | `0x43E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1502 | `MSChapSrvChangePassword` | `0x43E40` | 712 | UnwindData |  |
| 1503 | `MSChapSrvChangePassword2` | `0x44110` | 249 | UnwindData |  |
| 1657 | `RegQueryReflectionKey` | `0x44460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1571 | `ProcessIdleTasks` | `0x44470` | 60 | UnwindData |  |
| 1572 | `ProcessIdleTasksW` | `0x444C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1779 | `SystemFunction017` | `0x444D0` | 80 | UnwindData |  |
| 1781 | `SystemFunction019` | `0x44530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `AuditComputeEffectivePolicyByToken` | `0x44540` | 346 | UnwindData |  |
| 1044 | `AuditLookupCategoryGuidFromCategoryId` | `0x446A0` | 56 | UnwindData |  |
| 1045 | `AuditLookupCategoryIdFromCategoryGuid` | `0x446E0` | 103 | UnwindData |  |
| 1046 | `AuditLookupCategoryNameA` | `0x44750` | 157 | UnwindData |  |
| 1048 | `AuditLookupSubCategoryNameA` | `0x44800` | 157 | UnwindData |  |
| 1050 | `AuditQueryGlobalSaclA` | `0x448B0` | 176 | UnwindData |  |
| 1055 | `AuditSetGlobalSaclA` | `0x44970` | 176 | UnwindData |  |
| 1162 | `CredIsMarshaledCredentialA` | `0x44D00` | 68 | UnwindData |  |
| 1178 | `CredRenameA` | `0x44D50` | 29 | UnwindData |  |
| 1179 | `CredRenameW` | `0x44D50` | 29 | UnwindData |  |
| 1415 | `LsaAddPrivilegesToAccount` | `0x44D80` | 104 | UnwindData |  |
| 1416 | `LsaClearAuditLog` | `0x44DF0` | 99 | UnwindData |  |
| 1418 | `LsaConfigureAutoLogonCredentials` | `0x44E60` | 86 | UnwindData |  |
| 1419 | `LsaCreateAccount` | `0x44EC0` | 229 | UnwindData |  |
| 1421 | `LsaCreateTrustedDomain` | `0x44FB0` | 229 | UnwindData |  |
| 1425 | `LsaDisableUserArso` | `0x450A0` | 91 | UnwindData |  |
| 1426 | `LsaEnableUserArso` | `0x45110` | 91 | UnwindData |  |
| 1428 | `LsaEnumerateAccounts` | `0x45180` | 188 | UnwindData |  |
| 1430 | `LsaEnumeratePrivileges` | `0x45250` | 188 | UnwindData |  |
| 1431 | `LsaEnumeratePrivilegesOfAccount` | `0x45320` | 108 | UnwindData |  |
| 1435 | `LsaGetAppliedCAPIDs` | `0x453A0` | 271 | UnwindData |  |
| 1437 | `LsaGetQuotasForAccount` | `0x454C0` | 104 | UnwindData |  |
| 1438 | `LsaGetRemoteUserName` | `0x45530` | 290 | UnwindData |  |
| 1439 | `LsaGetSystemAccessAccount` | `0x45660` | 104 | UnwindData |  |
| 1445 | `LsaInvokeTrustScanner` | `0x456D0` | 102 | UnwindData |  |
| 1450 | `LsaLookupPrivilegeDisplayName` | `0x45740` | 733 | UnwindData |  |
| 1457 | `LsaOpenAccount` | `0x45A30` | 229 | UnwindData |  |
| 1459 | `LsaOpenPolicySce` | `0x45B20` | 224 | UnwindData |  |
| 1461 | `LsaOpenTrustedDomain` | `0x45C10` | 229 | UnwindData |  |
| 1463 | `LsaProfileDeleted` | `0x45D00` | 91 | UnwindData |  |
| 1464 | `LsaPurgeLocalSystemAccessTable` | `0x45D70` | 146 | UnwindData |  |
| 1465 | `LsaQueryCAPs` | `0x45E10` | 273 | UnwindData |  |
| 1469 | `LsaQueryInfoTrustedDomain` | `0x45F30` | 222 | UnwindData |  |
| 1471 | `LsaQueryLocalSystemAccess` | `0x46020` | 174 | UnwindData |  |
| 1472 | `LsaQueryLocalSystemAccessAll` | `0x460E0` | 158 | UnwindData |  |
| 1474 | `LsaQuerySecurityObject` | `0x46190` | 168 | UnwindData |  |
| 1478 | `LsaRemovePrivilegesFromAccount` | `0x46240` | 111 | UnwindData |  |
| 1480 | `LsaSetCAPs` | `0x462C0` | 217 | UnwindData |  |
| 1485 | `LsaSetInformationTrustedDomain` | `0x463A0` | 859 | UnwindData |  |
| 1486 | `LsaSetLocalSystemAccess` | `0x46710` | 154 | UnwindData |  |
| 1487 | `LsaSetQuotasForAccount` | `0x467B0` | 104 | UnwindData |  |
| 1489 | `LsaSetSecurityObject` | `0x46820` | 303 | UnwindData |  |
| 1490 | `LsaSetSystemAccessAccount` | `0x46960` | 103 | UnwindData |  |
| 1494 | `LsaValidateProcUniqueLuid` | `0x469D0` | 91 | UnwindData |  |
| 1422 | `LsaCreateTrustedDomainEx` | `0x46AA0` | 443 | UnwindData |  |
| 1424 | `LsaDeleteTrustedDomain` | `0x46C70` | 104 | UnwindData |  |
| 1433 | `LsaEnumerateTrustedDomainsEx` | `0x46CE0` | 203 | UnwindData |  |
| 1462 | `LsaOpenTrustedDomainByName` | `0x46DC0` | 229 | UnwindData |  |
| 1466 | `LsaQueryDomainInformationPolicy` | `0x46EB0` | 133 | UnwindData |  |
| 1467 | `LsaQueryForestTrustInformation` | `0x46F40` | 133 | UnwindData |  |
| 1468 | `LsaQueryForestTrustInformation2` | `0x46FD0` | 145 | UnwindData |  |
| 1475 | `LsaQueryTrustedDomainInfo` | `0x47070` | 234 | UnwindData |  |
| 1476 | `LsaQueryTrustedDomainInfoByName` | `0x47160` | 150 | UnwindData |  |
| 1481 | `LsaSetDomainInformationPolicy` | `0x47200` | 125 | UnwindData |  |
| 1482 | `LsaSetForestTrustInformation` | `0x47290` | 163 | UnwindData |  |
| 1483 | `LsaSetForestTrustInformation2` | `0x47340` | 178 | UnwindData |  |
| 1491 | `LsaSetTrustedDomainInfoByName` | `0x47400` | 877 | UnwindData |  |
| 1492 | `LsaSetTrustedDomainInformation` | `0x47780` | 238 | UnwindData |  |
| 1436 | `LsaGetDeviceRegistrationInfo` | `0x48630` | 103 | UnwindData |  |
| 1314 | `GetLocalManagedApplications` | `0x48890` | 807 | UnwindData |  |
| 1315 | `GetManagedApplicationCategories` | `0x48BC0` | 101 | UnwindData |  |
| 1316 | `GetManagedApplications` | `0x48C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1387 | `InstallApplication` | `0x48C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1813 | `UninstallApplication` | `0x48C50` | 77 | UnwindData |  |
| 1390 | `IsTokenUntrusted` | `0x49BE0` | 725 | UnwindData |  |
| 1710 | `SaferSetPolicyInformation` | `0x4A500` | 149 | UnwindData |  |
| 1729 | `SetInformationCodeAuthzPolicyW` | `0x4A500` | 149 | UnwindData |  |
| 1708 | `SaferRecordEventLogEntry` | `0x4A890` | 549 | UnwindData |  |
| 1716 | `SaferiRecordEventLogEntry` | `0x4A890` | 549 | UnwindData |  |
| 1709 | `SaferSetLevelInformation` | `0x4AFA0` | 177 | UnwindData |  |
| 1728 | `SetInformationCodeAuthzLevelW` | `0x4AFA0` | 177 | UnwindData |  |
| 1715 | `SaferiPopulateDefaultsInRegistry` | `0x4C1A0` | 1,690 | UnwindData |  |
| 1077 | `BuildImpersonateExplicitAccessWithNameA` | `0x4DEA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `BuildImpersonateExplicitAccessWithNameW` | `0x4DEA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1081 | `BuildSecurityDescriptorA` | `0x4DED0` | 406 | UnwindData |  |
| 1288 | `FreeInheritedFromArray` | `0x4E070` | 65 | UnwindData |  |
| 1294 | `GetAuditedPermissionsFromAclA` | `0x4E0C0` | 131 | UnwindData |  |
| 1295 | `GetAuditedPermissionsFromAclW` | `0x4E150` | 154 | UnwindData |  |
| 1299 | `GetEffectiveRightsFromAclA` | `0x4E1F0` | 122 | UnwindData |  |
| 1309 | `GetInheritanceSourceA` | `0x4E270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1807 | `TreeResetNamedSecurityInfoA` | `0x4E270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1809 | `TreeSetNamedSecurityInfoA` | `0x4E270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1310 | `GetInheritanceSourceW` | `0x4E280` | 180 | UnwindData |  |
| 1412 | `LookupSecurityDescriptorPartsA` | `0x4E340` | 769 | UnwindData |  |
| 1413 | `LookupSecurityDescriptorPartsW` | `0x4E650` | 663 | UnwindData |  |
| 1079 | `BuildImpersonateTrusteeA` | `0x4E8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1080 | `BuildImpersonateTrusteeW` | `0x4E8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `BuildTrusteeWithObjectsAndNameA` | `0x4E910` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1086 | `BuildTrusteeWithObjectsAndNameW` | `0x4E910` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1087 | `BuildTrusteeWithObjectsAndSidA` | `0x4E970` | 121 | UnwindData |  |
| 1088 | `BuildTrusteeWithObjectsAndSidW` | `0x4E970` | 121 | UnwindData |  |
| 1317 | `GetMultipleTrusteeA` | `0x4E9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `GetMultipleTrusteeW` | `0x4E9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1318 | `GetMultipleTrusteeOperationA` | `0x4EA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1319 | `GetMultipleTrusteeOperationW` | `0x4EA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1353 | `GetTrusteeFormA` | `0x4EA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1354 | `GetTrusteeFormW` | `0x4EA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1355 | `GetTrusteeNameA` | `0x4EA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1356 | `GetTrusteeNameW` | `0x4EA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1357 | `GetTrusteeTypeA` | `0x4EA60` | 1,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1358 | `GetTrusteeTypeW` | `0x4EA60` | 1,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1091 | `CancelOverlappedAccess` | `0x4F090` | 99 | UnwindData |  |
| 1113 | `ConvertAccessToSecurityDescriptorA` | `0x4F100` | 371 | UnwindData |  |
| 1114 | `ConvertAccessToSecurityDescriptorW` | `0x4F280` | 126 | UnwindData |  |
| 1118 | `ConvertSecurityDescriptorToAccessA` | `0x4F310` | 57 | UnwindData |  |
| 1119 | `ConvertSecurityDescriptorToAccessNamedA` | `0x4F310` | 57 | UnwindData |  |
| 1120 | `ConvertSecurityDescriptorToAccessNamedW` | `0x4F350` | 57 | UnwindData |  |
| 1121 | `ConvertSecurityDescriptorToAccessW` | `0x4F350` | 57 | UnwindData |  |
| 1290 | `GetAccessPermissionsForObjectA` | `0x4F390` | 852 | UnwindData |  |
| 1291 | `GetAccessPermissionsForObjectW` | `0x4F6F0` | 307 | UnwindData |  |
| 1322 | `GetNamedSecurityInfoExA` | `0x4F830` | 675 | UnwindData |  |
| 1323 | `GetNamedSecurityInfoExW` | `0x4FAE0` | 806 | UnwindData |  |
| 1327 | `GetOverlappedAccessResults` | `0x4FE10` | 310 | UnwindData |  |
| 1337 | `GetSecurityInfoExA` | `0x4FF50` | 631 | UnwindData |  |
| 1338 | `GetSecurityInfoExW` | `0x501D0` | 812 | UnwindData |  |
| 1720 | `SetEntriesInAccessListA` | `0x50510` | 70 | UnwindData |  |
| 1721 | `SetEntriesInAccessListW` | `0x50560` | 70 | UnwindData |  |
| 1724 | `SetEntriesInAuditListA` | `0x505B0` | 46 | UnwindData |  |
| 1725 | `SetEntriesInAuditListW` | `0x505F0` | 46 | UnwindData |  |
| 1732 | `SetNamedSecurityInfoExA` | `0x50630` | 1,188 | UnwindData |  |
| 1733 | `SetNamedSecurityInfoExW` | `0x50AE0` | 827 | UnwindData |  |
| 1745 | `SetSecurityInfoExA` | `0x50E30` | 1,097 | UnwindData |  |
| 1746 | `SetSecurityInfoExW` | `0x51280` | 844 | UnwindData |  |
| 1811 | `TrusteeAccessToObjectA` | `0x515E0` | 616 | UnwindData |  |
| 1812 | `TrusteeAccessToObjectW` | `0x51850` | 250 | UnwindData |  |
| 1283 | `FlushTraceA` | `0x52C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1589 | `QueryTraceA` | `0x52C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1761 | `StopTraceA` | `0x52C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1817 | `UpdateTraceA` | `0x52CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1818 | `UpdateTraceW` | `0x52CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `AbortSystemShutdownA` | `0x52CF0` | 167 | UnwindData |  |
| 1006 | `AbortSystemShutdownW` | `0x52DA0` | 116 | UnwindData |  |
| 1381 | `InitiateShutdownA` | `0x52E20` | 320 | UnwindData |  |
| 1383 | `InitiateSystemShutdownA` | `0x52F70` | 334 | UnwindData |  |
| 1384 | `InitiateSystemShutdownExA` | `0x530D0` | 341 | UnwindData |  |
| 1386 | `InitiateSystemShutdownW` | `0x53230` | 286 | UnwindData |  |
| 1063 | `BaseRegCreateKey` | `0x53360` | 101 | UnwindData |  |
| 1064 | `BaseRegDeleteKeyEx` | `0x533D0` | 54 | UnwindData |  |
| 1065 | `BaseRegDeleteValue` | `0x53410` | 44 | UnwindData |  |
| 1066 | `BaseRegFlushKey` | `0x53450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `BaseRegGetVersion` | `0x53480` | 44 | UnwindData |  |
| 1068 | `BaseRegLoadKey` | `0x534C0` | 49 | UnwindData |  |
| 1069 | `BaseRegOpenKey` | `0x53500` | 63 | UnwindData |  |
| 1070 | `BaseRegRestoreKey` | `0x53590` | 49 | UnwindData |  |
| 1071 | `BaseRegSaveKeyEx` | `0x53600` | 54 | UnwindData |  |
| 1072 | `BaseRegSetKeySecurity` | `0x53640` | 48 | UnwindData |  |
| 1073 | `BaseRegSetValue` | `0x53680` | 62 | UnwindData |  |
| 1074 | `BaseRegUnLoadKey` | `0x536D0` | 44 | UnwindData |  |
| 1701 | `SafeBaseRegGetKeySecurity` | `0x53710` | 53 | UnwindData |  |
| 1603 | `RegCopyTreeA` | `0x53B90` | 118 | UnwindData |  |
| 1608 | `RegCreateKeyTransactedA` | `0x53C10` | 142 | UnwindData |  |
| 1648 | `RegOpenKeyTransactedA` | `0x53CB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1662 | `RegRenameKey` | `0x53CF0` | 160 | UnwindData |  |
| 1614 | `RegDeleteKeyTransactedA` | `0x53DA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1690 | `RemoteRegEnumKeyWrapper` | `0x53DE0` | 356 | UnwindData |  |
| 1691 | `RemoteRegEnumValueWrapper` | `0x53F50` | 287 | UnwindData |  |
| 1695 | `RemoteRegQueryValueWrapper` | `0x54080` | 149 | UnwindData |  |
| 1663 | `RegReplaceKeyA` | `0x54120` | 568 | UnwindData |  |
| 1667 | `RegSaveKeyA` | `0x54360` | 444 | UnwindData |  |
| 1674 | `RegSetValueA` | `0x54530` | 356 | UnwindData |  |
| 1693 | `RemoteRegQueryMultipleValues2Wrapper` | `0x546A0` | 363 | UnwindData |  |
| 1694 | `RemoteRegQueryMultipleValuesWrapper` | `0x54820` | 350 | UnwindData |  |
| 1385 | `InitiateSystemShutdownExW` | `0x54990` | 305 | UnwindData |  |
| 1664 | `RegReplaceKeyW` | `0x54AD0` | 393 | UnwindData |  |
| 1251 | `EnumDependentServicesA` | `0x54D70` | 430 | UnwindData |  |
| 1339 | `GetServiceDisplayNameA` | `0x54F30` | 140 | UnwindData |  |
| 1341 | `GetServiceKeyNameA` | `0x54FD0` | 140 | UnwindData |  |
| 1584 | `QueryServiceLockStatusA` | `0x55070` | 238 | UnwindData |  |
| 1585 | `QueryServiceLockStatusW` | `0x55170` | 238 | UnwindData |  |
| 1747 | `SetServiceBits` | `0x55420` | 57 | UnwindData |  |
| 1814 | `UnlockServiceDatabase` | `0x55460` | 106 | UnwindData |  |
| 1008 | `AccessCheckAndAuditAlarmA` | `0x554D0` | 430 | UnwindData |  |
| 1011 | `AccessCheckByTypeAndAuditAlarmA` | `0x55690` | 475 | UnwindData |  |
| 1015 | `AccessCheckByTypeResultListAndAuditAlarmByHandleA` | `0x55880` | 490 | UnwindData |  |
| 1406 | `LookupPrivilegeDisplayNameA` | `0x55A70` | 525 | UnwindData |  |
| 1407 | `LookupPrivilegeDisplayNameW` | `0x55C90` | 413 | UnwindData |  |
| 1514 | `ObjectCloseAuditAlarmA` | `0x55E40` | 148 | UnwindData |  |
| 1516 | `ObjectDeleteAuditAlarmA` | `0x55EE0` | 148 | UnwindData |  |
| 1518 | `ObjectOpenAuditAlarmA` | `0x55F80` | 435 | UnwindData |  |
| 1520 | `ObjectPrivilegeAuditAlarmA` | `0x56140` | 181 | UnwindData |  |
| 1569 | `PrivilegedServiceAuditAlarmA` | `0x56200` | 250 | UnwindData |  |
| 1142 | `CreateProcessWithLogonW` | `0x56300` | 116 | UnwindData |  |
| 1397 | `LogonUserA` | `0x56850` | 63 | UnwindData |  |
| 1398 | `LogonUserExA` | `0x56A40` | 89 | UnwindData |  |
| 1400 | `LogonUserExW` | `0x56AA0` | 89 | UnwindData |  |
| 1028 | `AddConditionalAce` | `0x56B00` | 728 | UnwindData |  |
| 1347 | `GetStringConditionFromBinary` | `0x56DE0` | 77 | UnwindData |  |
| 1115 | `ConvertSDToStringSDDomainW` | `0x57300` | 135 | UnwindData |  |
| 1116 | `ConvertSDToStringSDRootDomainA` | `0x57390` | 372 | UnwindData |  |
| 1117 | `ConvertSDToStringSDRootDomainW` | `0x57510` | 120 | UnwindData |  |
| 1126 | `ConvertStringSDToSDDomainA` | `0x57590` | 316 | UnwindData |  |
| 1127 | `ConvertStringSDToSDDomainW` | `0x576E0` | 198 | UnwindData |  |
| 1128 | `ConvertStringSDToSDRootDomainA` | `0x577B0` | 215 | UnwindData |  |
| 1129 | `ConvertStringSDToSDRootDomainW` | `0x57890` | 105 | UnwindData |  |
| 1060 | `BackupEventLogA` | `0x595D0` | 198 | UnwindData |  |
| 1061 | `BackupEventLogW` | `0x596A0` | 185 | UnwindData |  |
| 1098 | `ClearEventLogA` | `0x597A0` | 198 | UnwindData |  |
| 1099 | `ClearEventLogW` | `0x59870` | 185 | UnwindData |  |
| 1102 | `CloseEventLog` | `0x59930` | 65 | UnwindData |  |
| 1239 | `DeregisterEventSource` | `0x59980` | 65 | UnwindData |  |
| 1302 | `GetEventLogInformation` | `0x599D0` | 75 | UnwindData |  |
| 1325 | `GetNumberOfEventLogRecords` | `0x59A30` | 65 | UnwindData |  |
| 1326 | `GetOldestEventLogRecord` | `0x59A80` | 65 | UnwindData |  |
| 1509 | `NotifyChangeEventLog` | `0x59AD0` | 65 | UnwindData |  |
| 1522 | `OpenBackupEventLogA` | `0x59B20` | 284 | UnwindData |  |
| 1523 | `OpenBackupEventLogW` | `0x59C50` | 221 | UnwindData |  |
| 1526 | `OpenEventLogA` | `0x59D40` | 113 | UnwindData |  |
| 1527 | `OpenEventLogW` | `0x59DC0` | 113 | UnwindData |  |
| 1596 | `ReadEventLogA` | `0x59E40` | 146 | UnwindData |  |
| 1597 | `ReadEventLogW` | `0x59EE0` | 148 | UnwindData |  |
| 1680 | `RegisterEventSourceA` | `0x59F80` | 113 | UnwindData |  |
| 1681 | `RegisterEventSourceW` | `0x5A000` | 113 | UnwindData |  |
| 1698 | `ReportEventA` | `0x5A080` | 716 | UnwindData |  |
| 1556 | `PerfRegEnumKey` | `0x5C440` | 84 | UnwindData |  |
| 1557 | `PerfRegEnumValue` | `0x5C4A0` | 404 | UnwindData |  |
| 1560 | `PerfRegSetValue` | `0x5C640` | 1,220 | UnwindData |  |
| 1822 | `WmiCloseBlock` | `0x5E2F0` | 115 | UnwindData |  |
| 1823 | `WmiDevInstToInstanceNameA` | `0x5E370` | 218 | UnwindData |  |
| 1824 | `WmiDevInstToInstanceNameW` | `0x5E450` | 218 | UnwindData |  |
| 1825 | `WmiEnumerateGuids` | `0x5E530` | 488 | UnwindData |  |
| 1826 | `WmiExecuteMethodA` | `0x5E720` | 244 | UnwindData |  |
| 1828 | `WmiFileHandleToInstanceNameA` | `0x5E820` | 613 | UnwindData |  |
| 1829 | `WmiFileHandleToInstanceNameW` | `0x5EA90` | 516 | UnwindData |  |
| 1830 | `WmiFreeBuffer` | `0x5ECA0` | 67 | UnwindData |  |
| 1833 | `WmiNotificationRegistrationA` | `0x5ECF0` | 123 | UnwindData |  |
| 1834 | `WmiNotificationRegistrationW` | `0x5ED80` | 123 | UnwindData |  |
| 1836 | `WmiQueryAllDataA` | `0x5EE10` | 106 | UnwindData |  |
| 1837 | `WmiQueryAllDataMultipleA` | `0x5EE80` | 124 | UnwindData |  |
| 1838 | `WmiQueryAllDataMultipleW` | `0x5EF10` | 554 | UnwindData |  |
| 1839 | `WmiQueryAllDataW` | `0x5F140` | 623 | UnwindData |  |
| 1840 | `WmiQueryGuidInformation` | `0x5F3C0` | 183 | UnwindData |  |
| 1841 | `WmiQuerySingleInstanceA` | `0x5F480` | 220 | UnwindData |  |
| 1842 | `WmiQuerySingleInstanceMultipleA` | `0x5F570` | 415 | UnwindData |  |
| 1843 | `WmiQuerySingleInstanceMultipleW` | `0x5F720` | 603 | UnwindData |  |
| 1844 | `WmiQuerySingleInstanceW` | `0x5F990` | 651 | UnwindData |  |
| 1845 | `WmiReceiveNotificationsA` | `0x5FC30` | 113 | UnwindData |  |
| 1846 | `WmiReceiveNotificationsW` | `0x5FCB0` | 113 | UnwindData |  |
| 1847 | `WmiSetSingleInstanceA` | `0x5FD30` | 202 | UnwindData |  |
| 1848 | `WmiSetSingleInstanceW` | `0x5FE00` | 468 | UnwindData |  |
| 1849 | `WmiSetSingleItemA` | `0x5FFE0` | 210 | UnwindData |  |
| 1850 | `WmiSetSingleItemW` | `0x600C0` | 483 | UnwindData |  |
| 1831 | `WmiMofEnumerateResourcesA` | `0x60590` | 562 | UnwindData |  |
| 1832 | `WmiMofEnumerateResourcesW` | `0x607D0` | 939 | UnwindData |  |
| 1104 | `CloseThreadWaitChainSession` | `0x66CC0` | 215 | UnwindData |  |
| 1348 | `GetThreadWaitChain` | `0x66DA0` | 658 | UnwindData |  |
| 1534 | `OpenThreadWaitChainSession` | `0x67040` | 392 | UnwindData |  |
