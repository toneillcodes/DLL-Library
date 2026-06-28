# Binary Specification: dsreg.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dsreg.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `27966ebfda6645dce288186436a3fe0bca5fef148dbc36a7d36b8b1f41d98f3d`
* **Total Exported Functions:** 53

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 34 | `DsrIsWorkplaceJoined` | `0x6310` | 681 | UnwindData |  |
| 33 | `DsrIsDeviceJoinedEx` | `0x65C0` | 758 | UnwindData |  |
| 32 | `DsrIsDeviceJoined` | `0x7420` | 57 | UnwindData |  |
| 24 | `DsrFreeJoinInfoEx` | `0x9630` | 891 | UnwindData |  |
| 28 | `DsrGetJoinInfo` | `0xA010` | 513 | UnwindData |  |
| 29 | `DsrGetJoinInfoEx` | `0xA220` | 2,227 | UnwindData |  |
| 47 | `NgcNeedProvision` | `0xEF20` | 370 | UnwindData |  |
| 38 | `DsrWriteAutoJoinSvcDebugEvent` | `0x15D70` | 82 | UnwindData |  |
| 23 | `DsrFreeJoinInfo` | `0x19170` | 276 | UnwindData |  |
| 8 | `DsrBeginDiscover` | `0x1C350` | 26 | UnwindData |  |
| 39 | `DsrWriteAutoJoinSvcTriggerEvent` | `0x1F030` | 226 | UnwindData |  |
| 30 | `DsrGetPrtAuthorityInfo` | `0x213A0` | 218 | UnwindData |  |
| 1 | `DsrBeginDelegatedWorkplaceJoin` | `0x2DB90` | 567 | UnwindData |  |
| 2 | `DsrBeginDeviceAndResourceAccountJoin` | `0x2DDD0` | 75 | UnwindData |  |
| 3 | `DsrBeginDeviceAndResourceAccountJoinEx` | `0x2DE30` | 907 | UnwindData |  |
| 4 | `DsrBeginDeviceJoin` | `0x2E1D0` | 209 | UnwindData |  |
| 5 | `DsrBeginDeviceJoinEx` | `0x2E2B0` | 678 | UnwindData |  |
| 6 | `DsrBeginDeviceUnjoin` | `0x2E560` | 113 | UnwindData |  |
| 7 | `DsrBeginDeviceUpdate` | `0x2E5E0` | 44 | UnwindData |  |
| 9 | `DsrBeginPreprovisionedDeviceJoin` | `0x2E620` | 57 | UnwindData |  |
| 10 | `DsrBeginPreprovisionedDeviceJoinEx` | `0x2E660` | 786 | UnwindData |  |
| 11 | `DsrBeginRecovery` | `0x2E980` | 1,389 | UnwindData |  |
| 12 | `DsrBeginWorkplaceJoin` | `0x2EF00` | 605 | UnwindData |  |
| 13 | `DsrBeginWorkplaceUnjoin` | `0x2F170` | 33 | UnwindData |  |
| 14 | `DsrBeginWorkplaceUpdate` | `0x2F270` | 46 | UnwindData |  |
| 17 | `DsrCanCurrentUserProvisionNgcKey` | `0x2F2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `DsrCanCurrentUserResetNgcKey` | `0x2F2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `DsrDeviceHostNameUpdate` | `0x2F2D0` | 22 | UnwindData |  |
| 20 | `DsrEndRecovery` | `0x2F2F0` | 1,139 | UnwindData |  |
| 25 | `DsrGetCurrentUserNgcProvisionStatus` | `0x2F770` | 137 | UnwindData |  |
| 27 | `DsrGetDomainRegistrationConfig` | `0x2F800` | 289 | UnwindData |  |
| 37 | `DsrWriteAutoJoinSvcAdminEvent` | `0x2F930` | 85 | UnwindData |  |
| 40 | `FidoDeregisterKey` | `0x30130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `FidoRegisterKey` | `0x30140` | 167 | UnwindData |  |
| 42 | `NgcDeregisterKey` | `0x301F0` | 61 | UnwindData |  |
| 43 | `NgcGetKeyId` | `0x30240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `NgcGetLogonCertPolicy` | `0x30250` | 427 | UnwindData |  |
| 45 | `NgcGetStatistics` | `0x30410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `NgcIncrementPinRetryAttempts` | `0x30420` | 113 | UnwindData |  |
| 48 | `NgcNeedProvisionForAccount` | `0x304A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `NgcReadRegistryValue` | `0x304B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `NgcRegisterKey` | `0x304C0` | 165 | UnwindData |  |
| 51 | `NgcResetPinRetryAttempts` | `0x30570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `NgcUpdateCertEnrollStatistics` | `0x30580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `NgcUpdateStatistics` | `0x30590` | 126,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `DsrFreeDiscoveryMetadata` | `0x4F390` | 38 | UnwindData |  |
| 21 | `DsrFreeCxhScenarioInfo` | `0x75640` | 79 | UnwindData |  |
| 26 | `DsrGetCxhScenarioInfo` | `0x756A0` | 866 | UnwindData |  |
| 31 | `DsrGetResourceAccount` | `0x75B40` | 380 | UnwindData |  |
| 35 | `DsrSaveDeviceTokenProperties` | `0x75CD0` | 120 | UnwindData |  |
| 36 | `DsrSaveWorkplaceTokenProperties` | `0x75D50` | 117 | UnwindData |  |
| 16 | `DsrCLI` | `0x8C6E0` | 14,551 | UnwindData |  |
| 15 | `DsrBeginWorkplaceUpdateAik` | `0xB5D80` | 36 | UnwindData |  |
