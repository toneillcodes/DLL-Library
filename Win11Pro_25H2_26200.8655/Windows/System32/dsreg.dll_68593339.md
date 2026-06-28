# Binary Specification: dsreg.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dsreg.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `685933395e85713725a571d5bef0ec3ed8eaed620fbd411129c127c2ffa29244`
* **Total Exported Functions:** 55

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 34 | `DsrIsWorkplaceJoined` | `0x4510` | 681 | UnwindData |  |
| 33 | `DsrIsDeviceJoinedEx` | `0x47C0` | 758 | UnwindData |  |
| 32 | `DsrIsDeviceJoined` | `0x5010` | 57 | UnwindData |  |
| 28 | `DsrGetJoinInfo` | `0x52F0` | 513 | UnwindData |  |
| 29 | `DsrGetJoinInfoEx` | `0x5500` | 2,300 | UnwindData |  |
| 24 | `DsrFreeJoinInfoEx` | `0x6F60` | 927 | UnwindData |  |
| 23 | `DsrFreeJoinInfo` | `0xB980` | 276 | UnwindData |  |
| 49 | `NgcNeedProvision` | `0xBE70` | 370 | UnwindData |  |
| 40 | `DsrWriteAutoJoinSvcDebugEvent` | `0x10C60` | 82 | UnwindData |  |
| 8 | `DsrBeginDiscover` | `0x18F30` | 26 | UnwindData |  |
| 41 | `DsrWriteAutoJoinSvcTriggerEvent` | `0x1BD80` | 226 | UnwindData |  |
| 30 | `DsrGetPrtAuthorityInfo` | `0x209E0` | 218 | UnwindData |  |
| 1 | `DsrBeginDelegatedWorkplaceJoin` | `0x2C3B0` | 567 | UnwindData |  |
| 2 | `DsrBeginDeviceAndResourceAccountJoin` | `0x2C5F0` | 75 | UnwindData |  |
| 3 | `DsrBeginDeviceAndResourceAccountJoinEx` | `0x2C650` | 907 | UnwindData |  |
| 4 | `DsrBeginDeviceJoin` | `0x2C9F0` | 209 | UnwindData |  |
| 5 | `DsrBeginDeviceJoinEx` | `0x2CAD0` | 678 | UnwindData |  |
| 6 | `DsrBeginDeviceUnjoin` | `0x2CD80` | 113 | UnwindData |  |
| 7 | `DsrBeginDeviceUpdate` | `0x2CE00` | 44 | UnwindData |  |
| 9 | `DsrBeginPreprovisionedDeviceJoin` | `0x2CE40` | 57 | UnwindData |  |
| 10 | `DsrBeginPreprovisionedDeviceJoinEx` | `0x2CE80` | 786 | UnwindData |  |
| 11 | `DsrBeginRecovery` | `0x2D1A0` | 1,389 | UnwindData |  |
| 12 | `DsrBeginWorkplaceJoin` | `0x2D720` | 605 | UnwindData |  |
| 13 | `DsrBeginWorkplaceUnjoin` | `0x2D990` | 33 | UnwindData |  |
| 14 | `DsrBeginWorkplaceUpdate` | `0x2DA90` | 46 | UnwindData |  |
| 17 | `DsrCanCurrentUserProvisionNgcKey` | `0x2DAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `DsrCanCurrentUserResetNgcKey` | `0x2DAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `DsrDeviceHostNameUpdate` | `0x2DAF0` | 22 | UnwindData |  |
| 20 | `DsrEndRecovery` | `0x2DB10` | 1,145 | UnwindData |  |
| 25 | `DsrGetCurrentUserNgcProvisionStatus` | `0x2DF90` | 137 | UnwindData |  |
| 27 | `DsrGetDomainRegistrationConfig` | `0x2E020` | 289 | UnwindData |  |
| 35 | `DsrProvisionResourceAccountCredentials` | `0x2E150` | 125 | UnwindData |  |
| 36 | `DsrRemoveResourceAccountCredentials` | `0x2E1E0` | 68 | UnwindData |  |
| 39 | `DsrWriteAutoJoinSvcAdminEvent` | `0x2E230` | 85 | UnwindData |  |
| 42 | `FidoDeregisterKey` | `0x2EA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `FidoRegisterKey` | `0x2EA40` | 167 | UnwindData |  |
| 44 | `NgcDeregisterKey` | `0x2EAF0` | 61 | UnwindData |  |
| 45 | `NgcGetKeyId` | `0x2EB40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `NgcGetLogonCertPolicy` | `0x2EB50` | 427 | UnwindData |  |
| 47 | `NgcGetStatistics` | `0x2ED10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `NgcIncrementPinRetryAttempts` | `0x2ED20` | 113 | UnwindData |  |
| 50 | `NgcNeedProvisionForAccount` | `0x2EDA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `NgcReadRegistryValue` | `0x2EDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `NgcRegisterKey` | `0x2EDC0` | 165 | UnwindData |  |
| 53 | `NgcResetPinRetryAttempts` | `0x2EE70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `NgcUpdateCertEnrollStatistics` | `0x2EE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `NgcUpdateStatistics` | `0x2EE90` | 132,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `DsrFreeDiscoveryMetadata` | `0x4F3E0` | 38 | UnwindData |  |
| 21 | `DsrFreeCxhScenarioInfo` | `0x76310` | 79 | UnwindData |  |
| 26 | `DsrGetCxhScenarioInfo` | `0x76370` | 866 | UnwindData |  |
| 31 | `DsrGetResourceAccount` | `0x76810` | 453 | UnwindData |  |
| 37 | `DsrSaveDeviceTokenProperties` | `0x769E0` | 120 | UnwindData |  |
| 38 | `DsrSaveWorkplaceTokenProperties` | `0x76A60` | 117 | UnwindData |  |
| 16 | `DsrCLI` | `0x8FE70` | 15,069 | UnwindData |  |
| 15 | `DsrBeginWorkplaceUpdateAik` | `0xBB170` | 36 | UnwindData |  |
