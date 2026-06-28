# Binary Specification: cryptngc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cryptngc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `57d613f1c9c1bc5a3ce5bd14e278b2665bd8f0afa3ebf1360b539cc02d05a8c2`
* **Total Exported Functions:** 59

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 18 | `NgcDecryptWithUserIdKeySilent` | `0x2830` | 50 | UnwindData |  |
| 48 | `NgcQueryEnabled` | `0x7530` | 1,009 | UnwindData |  |
| 45 | `NgcPackAuthBuffer` | `0x93A0` | 1,260 | UnwindData |  |
| 31 | `NgcGetKeyImplType` | `0x98A0` | 776 | UnwindData |  |
| 58 | `NgcUnpackCredData` | `0x17B80` | 148 | UnwindData |  |
| 25 | `NgcFreeEnumState` | `0x1FBC0` | 184 | UnwindData |  |
| 24 | `NgcEnumUserIdKeys` | `0x1FCC0` | 500 | UnwindData |  |
| 40 | `NgcGetUserIdKeyPublicKey` | `0x20B70` | 365 | UnwindData |  |
| 37 | `NgcGetUserIdKeyCertificate` | `0x20CF0` | 298 | UnwindData |  |
| 26 | `NgcGetDefaultDecryptionKeyName` | `0x21070` | 353 | UnwindData |  |
| 16 | `NgcCreateUserIdKeyHandle` | `0x21240` | 436 | UnwindData |  |
| 44 | `NgcOpenUserIdKey` | `0x22B60` | 85 | UnwindData |  |
| 47 | `NgcQueryEffectiveCertPolicy` | `0x23550` | 58 | UnwindData |  |
| 49 | `NgcQueryHardwarePolicy` | `0x23F70` | 59 | UnwindData |  |
| 27 | `NgcGetEventInterface` | `0x246E0` | 3,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `NgcEnumContainers` | `0x252E0` | 71 | UnwindData |  |
| 41 | `NgcIsAnyContainerInVsm` | `0x2B110` | 95 | UnwindData |  |
| 39 | `NgcGetUserIdKeyName` | `0x2BE30` | 97 | UnwindData |  |
| 1 | `FidoCreateCredential` | `0x32390` | 4,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `FidoGetCredential` | `0x32390` | 4,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `FidoSignWithCredential` | `0x32390` | 4,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `NgcGetKeyAttestationForContainerService` | `0x33340` | 662 | UnwindData |  |
| 29 | `NgcGetKeyAttestationForUserIdKey` | `0x335E0` | 73 | UnwindData |  |
| 30 | `NgcGetKeyAttestationForUserIdKey2` | `0x33630` | 649 | UnwindData |  |
| 46 | `NgcPackPasswordChangeAuthBuffer` | `0x34980` | 156 | UnwindData |  |
| 57 | `NgcUnpackAuthBuffer` | `0x34A30` | 206 | UnwindData |  |
| 59 | `NgcUnpackPasswordChangeAuthBuffer` | `0x34B10` | 206 | UnwindData |  |
| 43 | `NgcNotifyVscProvisioned` | `0x34CD0` | 280 | UnwindData |  |
| 4 | `NgcAddBioProtector` | `0x365B0` | 360 | UnwindData |  |
| 5 | `NgcAddCompanionDeviceProtector` | `0x36720` | 348 | UnwindData |  |
| 6 | `NgcAddPrebootProtector` | `0x36890` | 381 | UnwindData |  |
| 7 | `NgcCancelPendingUIRequest` | `0x36A20` | 318 | UnwindData |  |
| 8 | `NgcChangePin` | `0x36B70` | 348 | UnwindData |  |
| 9 | `NgcChangePinSilent` | `0x36CE0` | 368 | UnwindData |  |
| 10 | `NgcCreateContainer` | `0x36E60` | 1,081 | UnwindData |  |
| 11 | `NgcCreateContainerSilent` | `0x372A0` | 496 | UnwindData |  |
| 19 | `NgcDeleteContainer` | `0x374A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `NgcDeleteContainerEx` | `0x374B0` | 925 | UnwindData |  |
| 34 | `NgcGetPolicy` | `0x37860` | 368 | UnwindData |  |
| 42 | `NgcIsPinRemovable` | `0x379E0` | 660 | UnwindData |  |
| 50 | `NgcRemoveBioProtector` | `0x37C80` | 336 | UnwindData |  |
| 51 | `NgcRemoveCompanionDeviceProtector` | `0x37DE0` | 336 | UnwindData |  |
| 52 | `NgcRemovePrebootProtector` | `0x37F40` | 336 | UnwindData |  |
| 14 | `NgcCreateUserIdKey` | `0x3ADC0` | 481 | UnwindData |  |
| 15 | `NgcCreateUserIdKeyEx` | `0x3AFB0` | 498 | UnwindData |  |
| 21 | `NgcDeleteUserIdKey` | `0x3B1B0` | 286 | UnwindData |  |
| 32 | `NgcGetLogonDecryptionKeyName` | `0x3B2E0` | 298 | UnwindData |  |
| 33 | `NgcGetLogonDecryptionKeyNameForFirstLogonAfterUpgradeFromThreshold` | `0x3B410` | 298 | UnwindData |  |
| 35 | `NgcGetPregenKeyState` | `0x3B540` | 267 | UnwindData |  |
| 36 | `NgcGetPregenUserKey` | `0x3B660` | 349 | UnwindData |  |
| 38 | `NgcGetUserIdKeyContainerStatus` | `0x3B7D0` | 320 | UnwindData |  |
| 53 | `NgcSignWithUserIdKey` | `0x3B920` | 68 | UnwindData |  |
| 54 | `NgcSignWithUserIdKeyAndPadding` | `0x3B970` | 165 | UnwindData |  |
| 55 | `NgcSignWithUserIdKeyEx` | `0x3BA20` | 151 | UnwindData |  |
| 56 | `NgcSignWithUserIdKeySilent` | `0x3BAC0` | 87 | UnwindData |  |
| 17 | `NgcDecryptWithUserIdKey` | `0x3C2D0` | 52 | UnwindData |  |
| 22 | `NgcEncryptWithAsymmetricKey` | `0x3C310` | 327 | UnwindData |  |
| 12 | `NgcCreateTicketForSmartCardKeyOperation` | `0x3C460` | 117 | UnwindData |  |
| 13 | `NgcCreateTicketForSmartCardVpn` | `0x3C4E0` | 56,700 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
