# Binary Specification: ngcutils.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ngcutils.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f7d40a821f1a3f1a047765114e1e5a2ce3b0b7c24838adca1235feca9a1939a7`
* **Total Exported Functions:** 34

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x11770` | 141 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x11810` | 617 | UnwindData |  |
| 3 | `NgcAreCacheTypeApiFlagsValid` | `0x11B20` | 84 | UnwindData |  |
| 4 | `NgcAreNCryptCacheTypeApiFlagsValid` | `0x11B80` | 84 | UnwindData |  |
| 5 | `NgcAreStringsEqual` | `0x11BE0` | 191 | UnwindData |  |
| 6 | `NgcBuildDefaultDecryptionKeyNameString` | `0x11CB0` | 748 | UnwindData |  |
| 7 | `NgcBuildKeyNameString` | `0x11FB0` | 1,118 | UnwindData |  |
| 8 | `NgcCallerIsAppContainer` | `0x12420` | 90 | UnwindData |  |
| 9 | `NgcCoMemAllocCopy` | `0x12480` | 143 | UnwindData |  |
| 10 | `NgcCoMemResourceStringAllocCopy` | `0x12520` | 157 | UnwindData |  |
| 11 | `NgcDeviceLockIsEnforcementPending` | `0x125D0` | 129 | UnwindData |  |
| 12 | `NgcGetAttestationStatement` | `0x12660` | 517 | UnwindData |  |
| 13 | `NgcGetAuthPackageId` | `0x12870` | 167 | UnwindData |  |
| 14 | `NgcGetCallerAppContainerSid` | `0x12920` | 424 | UnwindData |  |
| 15 | `NgcGetCallerSid` | `0x12AD0` | 424 | UnwindData |  |
| 16 | `NgcGetCryptoRegistryLocation` | `0x12C80` | 170 | UnwindData |  |
| 17 | `NgcGetNCryptBinaryBlob` | `0x12D30` | 340 | UnwindData |  |
| 18 | `NgcGetSmartCardReaderAndContainerName` | `0x12E90` | 444 | UnwindData |  |
| 19 | `NgcGetUserNameAndDomain` | `0x13060` | 575 | UnwindData |  |
| 20 | `NgcGetUserSid` | `0x132B0` | 456 | UnwindData |  |
| 21 | `NgcIsCertTrustEnabled` | `0x13480` | 158 | UnwindData |  |
| 22 | `NgcIsCloudTrustEnabled` | `0x13530` | 129 | UnwindData |  |
| 23 | `NgcIsConsumerUser` | `0x135C0` | 129 | UnwindData |  |
| 24 | `NgcIsInsecureTpm` | `0x13650` | 129 | UnwindData |  |
| 25 | `NgcIsPolicyEnabled` | `0x136E0` | 195 | UnwindData |  |
| 26 | `NgcIsPostLogonCachingDisabled` | `0x137B0` | 153 | UnwindData |  |
| 27 | `NgcPackGestureCollectionInputSerializationBuffer` | `0x13850` | 1,406 | UnwindData |  |
| 28 | `NgcSetBioProtectorUpdateNeeded` | `0x13DE0` | 61 | UnwindData |  |
| 29 | `NgcSetNCryptBoolProperty` | `0x13E30` | 158 | UnwindData |  |
| 30 | `NgcSetNCryptDwordProperty` | `0x13EE0` | 153 | UnwindData |  |
| 31 | `NgcSetNCryptUiPolicy` | `0x13F80` | 144 | UnwindData |  |
| 32 | `NgcSetNCryptWindowHandle` | `0x14020` | 126 | UnwindData |  |
| 33 | `NgcUnpackGestureCollectionInputSerializationBuffer` | `0x140B0` | 850 | UnwindData |  |
| 34 | `NgcUnpackNegotiateInputSerializationBuffer` | `0x14410` | 793 | UnwindData |  |
