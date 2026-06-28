# Binary Specification: netjoin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\netjoin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c6fbf9ff1ae64bdd73b3b62a6acdd7da82f35ce8c5e6c2b2aeebeaac686c8627`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `NetCreateProvisioningPackage` | `0x0` | - | Forwarded | Forwarded to: `NETPROVFW.NetCreateProvisioningPackage` |
| 4 | `NetRequestProvisioningPackageInstall` | `0x0` | - | Forwarded | Forwarded to: `NETPROVFW.NetRequestProvisioningPackageInstall` |
| 7 | `NetpAvoidNetlogonSpnSet` | `0x0` | - | Forwarded | Forwarded to: `JOINUTIL.NetpAvoidNetlogonSpnSet` |
| 13 | `NetpDomainJoinLicensingCheck` | `0x0` | - | Forwarded | Forwarded to: `NETPROVFW.NetpProvDomainJoinLicensingCheck` |
| 16 | `NetpGetLsaPrimaryDomain` | `0x0` | - | Forwarded | Forwarded to: `JOINUTIL.NetpGetLsaPrimaryDomain` |
| 9 | `NetpControlServices` | `0x1FB0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `NetpQueryService` | `0x2050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `NetpStopService` | `0x2070` | 9,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `NetpJoinProviderInitialize` | `0x4640` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `NetpJoinProvider2Initialize` | `0x4930` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `NetpJoinProvider3Initialize` | `0x4B80` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `NetpJoinProvider4Initialize` | `0x4E00` | 3,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `NetpCrackNamesStatus2Win32Error` | `0x5D30` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `NetpCreateComputerObjectInDs` | `0x5E50` | 1,815 | UnwindData |  |
| 15 | `NetpGetListOfJoinableOUs` | `0x8DE0` | 450 | UnwindData |  |
| 17 | `NetpGetMachineAccountName` | `0x96F0` | 220 | UnwindData |  |
| 25 | `NetpManageIPCConnect` | `0xA9E0` | 803 | UnwindData |  |
| 28 | `NetpSeparateUserAndDomain` | `0xBCB0` | 63 | UnwindData |  |
| 29 | `NetpSetComputerAccountPassword` | `0xBD00` | 856 | UnwindData |  |
| 32 | `NetpUpdateAutoenrolConfig` | `0xCE80` | 210 | UnwindData |  |
| 2 | `NetProvisionComputerAccount` | `0xD3D0` | 770 | UnwindData |  |
| 3 | `NetRequestOfflineDomainJoin` | `0xD6E0` | 136 | UnwindData |  |
| 8 | `NetpChangeMachineName` | `0xE510` | 2,050 | UnwindData |  |
| 12 | `NetpDoDomainJoin` | `0xF360` | 678 | UnwindData |  |
| 14 | `NetpGetJoinInformation` | `0xF8A0` | 216 | UnwindData |  |
| 18 | `NetpIsSetupInProgress` | `0xFB20` | 171 | UnwindData |  |
| 24 | `NetpMachineValidToJoin` | `0x10D80` | 372 | UnwindData |  |
| 26 | `NetpManageMachineAccountWithSid` | `0x10FB0` | 942 | UnwindData |  |
| 31 | `NetpUnJoinDomain` | `0x12100` | 647 | UnwindData |  |
| 33 | `NetpValidateName` | `0x125E0` | 1,018 | UnwindData |  |
| 5 | `NetSetuppCloseLog` | `0x13D60` | 126 | UnwindData |  |
| 6 | `NetSetuppOpenLog` | `0x13DF0` | 156 | UnwindData |  |
| 23 | `NetpLogPrintHelper` | `0x143F0` | 100 | UnwindData |  |
