# Binary Specification: WinSCard.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WinSCard.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `70c4f27059bfe8a2b7ea148c60183709e7102d0acee6c7f9963667e45d2d347c`
* **Total Exported Functions:** 80

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `SCardControl` | `0x14D0` | 325 | UnwindData |  |
| 37 | `SCardGetReaderIconW` | `0x1620` | 265 | UnwindData |  |
| 77 | `SCardWriteCacheW` | `0x19A0` | 41 | UnwindData |  |
| 31 | `SCardGetDeviceTypeIdW` | `0x1E00` | 223 | UnwindData |  |
| 15 | `SCardConnectW` | `0x2BD0` | 1,014 | UnwindData |  |
| 14 | `SCardConnectA` | `0x3120` | 1,162 | UnwindData |  |
| 29 | `SCardGetCardTypeProviderNameW` | `0x38E0` | 605 | UnwindData |  |
| 55 | `SCardListReadersW` | `0x4060` | 478 | UnwindData |  |
| 63 | `SCardReadCacheW` | `0x42C0` | 43 | UnwindData |  |
| 54 | `SCardListReadersA` | `0x4830` | 725 | UnwindData |  |
| 38 | `SCardGetStatusChangeA` | `0x5FA0` | 1,576 | UnwindData |  |
| 19 | `SCardEstablishContext` | `0xB2E0` | 3,541 | UnwindData |  |
| 8 | `SCardAccessStartedEvent` | `0xE0D0` | 9 | UnwindData |  |
| 66 | `SCardReleaseStartedEvent` | `0xE870` | 138 | UnwindData |  |
| 65 | `SCardReleaseContext` | `0xF800` | 726 | UnwindData |  |
| 39 | `SCardGetStatusChangeW` | `0xFDB0` | 639 | UnwindData |  |
| 75 | `SCardTransmit` | `0x11140` | 503 | UnwindData |  |
| 74 | `SCardStatusW` | `0x11AB0` | 637 | UnwindData |  |
| 17 | `SCardDisconnect` | `0x12310` | 349 | UnwindData |  |
| 12 | `SCardBeginTransaction` | `0x125A0` | 270 | UnwindData |  |
| 18 | `SCardEndTransaction` | `0x126C0` | 382 | UnwindData |  |
| 49 | `SCardListCardsW` | `0x12B80` | 261 | UnwindData |  |
| 13 | `SCardCancel` | `0x14920` | 266 | UnwindData |  |
| 47 | `SCardIsValidContext` | `0x168D0` | 290 | UnwindData |  |
| 26 | `SCardFreeMemory` | `0x171A0` | 371 | UnwindData |  |
| 73 | `SCardStatusA` | `0x18C40` | 420 | UnwindData |  |
| 1 | `ClassInstall32` | `0x1B400` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SCardAccessNewReaderEvent` | `0x1B810` | 95 | UnwindData |  |
| 3 | `SCardPciRaw` | `0x1B880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SCardPciT0` | `0x1B890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SCardPciT1` | `0x1B8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SCardReleaseAllEvents` | `0x1B8B0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SCardReleaseNewReaderEvent` | `0x1B8B0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `SCardAudit` | `0x1BDE0` | 347 | UnwindData |  |
| 27 | `SCardGetAttrib` | `0x1BF50` | 1,475 | UnwindData |  |
| 40 | `SCardGetTransmitCount` | `0x1C520` | 210 | UnwindData |  |
| 64 | `SCardReconnect` | `0x1C600` | 186 | UnwindData |  |
| 69 | `SCardSetAttrib` | `0x1C6C0` | 150 | UnwindData |  |
| 72 | `SCardState` | `0x1C760` | 349 | UnwindData |  |
| 9 | `SCardAddReaderToGroupA` | `0x1DA50` | 417 | UnwindData |  |
| 20 | `SCardForgetCardTypeA` | `0x1DC00` | 182 | UnwindData |  |
| 22 | `SCardForgetReaderA` | `0x1DCC0` | 305 | UnwindData |  |
| 23 | `SCardForgetReaderGroupA` | `0x1DE00` | 305 | UnwindData |  |
| 28 | `SCardGetCardTypeProviderNameA` | `0x1DF40` | 286 | UnwindData |  |
| 30 | `SCardGetDeviceTypeIdA` | `0x1E070` | 318 | UnwindData |  |
| 32 | `SCardGetProviderIdA` | `0x1E1C0` | 331 | UnwindData |  |
| 34 | `SCardGetReaderDeviceInstanceIdA` | `0x1E320` | 393 | UnwindData |  |
| 36 | `SCardGetReaderIconA` | `0x1E4B0` | 376 | UnwindData |  |
| 41 | `SCardIntroduceCardTypeA` | `0x1E630` | 263 | UnwindData |  |
| 43 | `SCardIntroduceReaderA` | `0x1E740` | 417 | UnwindData |  |
| 44 | `SCardIntroduceReaderGroupA` | `0x1E8F0` | 287 | UnwindData |  |
| 48 | `SCardListCardsA` | `0x1EA20` | 243 | UnwindData |  |
| 50 | `SCardListInterfacesA` | `0x1EB20` | 362 | UnwindData |  |
| 52 | `SCardListReaderGroupsA` | `0x1EC90` | 295 | UnwindData |  |
| 56 | `SCardListReadersWithDeviceInstanceIdA` | `0x1EDC0` | 783 | UnwindData |  |
| 58 | `SCardLocateCardsA` | `0x1F0E0` | 1,302 | UnwindData |  |
| 59 | `SCardLocateCardsByATRA` | `0x1F600` | 357 | UnwindData |  |
| 62 | `SCardReadCacheA` | `0x1F770` | 40 | UnwindData |  |
| 67 | `SCardRemoveReaderFromGroupA` | `0x1F7A0` | 417 | UnwindData |  |
| 70 | `SCardSetCardTypeProviderNameA` | `0x1F950` | 293 | UnwindData |  |
| 76 | `SCardWriteCacheA` | `0x1FA80` | 38 | UnwindData |  |
| 10 | `SCardAddReaderToGroupW` | `0x1FD90` | 420 | UnwindData |  |
| 21 | `SCardForgetCardTypeW` | `0x1FF40` | 182 | UnwindData |  |
| 24 | `SCardForgetReaderGroupW` | `0x20000` | 308 | UnwindData |  |
| 25 | `SCardForgetReaderW` | `0x20140` | 308 | UnwindData |  |
| 33 | `SCardGetProviderIdW` | `0x20280` | 331 | UnwindData |  |
| 35 | `SCardGetReaderDeviceInstanceIdW` | `0x203E0` | 300 | UnwindData |  |
| 42 | `SCardIntroduceCardTypeW` | `0x20520` | 263 | UnwindData |  |
| 45 | `SCardIntroduceReaderGroupW` | `0x20630` | 290 | UnwindData |  |
| 46 | `SCardIntroduceReaderW` | `0x20760` | 420 | UnwindData |  |
| 51 | `SCardListInterfacesW` | `0x20910` | 362 | UnwindData |  |
| 53 | `SCardListReaderGroupsW` | `0x20A80` | 298 | UnwindData |  |
| 57 | `SCardListReadersWithDeviceInstanceIdW` | `0x20BB0` | 649 | UnwindData |  |
| 60 | `SCardLocateCardsByATRW` | `0x20E40` | 357 | UnwindData |  |
| 61 | `SCardLocateCardsW` | `0x20FB0` | 1,098 | UnwindData |  |
| 68 | `SCardRemoveReaderFromGroupW` | `0x21400` | 420 | UnwindData |  |
| 71 | `SCardSetCardTypeProviderNameW` | `0x215B0` | 293 | UnwindData |  |
| 79 | `g_rgSCardT0Pci` | `0x31E88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `g_rgSCardT1Pci` | `0x31E90` | 1,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `g_rgSCardRawPci` | `0x32278` | 0 | Indeterminate |  |
