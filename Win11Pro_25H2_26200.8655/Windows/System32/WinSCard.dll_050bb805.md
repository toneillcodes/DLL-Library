# Binary Specification: WinSCard.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WinSCard.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `050bb805be1a82b73b03d0e205562fdc5856f505a8f6a7514524c6b11eef52cf`
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
| 47 | `SCardIsValidContext` | `0x16910` | 290 | UnwindData |  |
| 26 | `SCardFreeMemory` | `0x171E0` | 371 | UnwindData |  |
| 73 | `SCardStatusA` | `0x18C80` | 420 | UnwindData |  |
| 1 | `ClassInstall32` | `0x1BB40` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SCardAccessNewReaderEvent` | `0x1BF50` | 95 | UnwindData |  |
| 3 | `SCardPciRaw` | `0x1BFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SCardPciT0` | `0x1BFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SCardPciT1` | `0x1BFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SCardReleaseAllEvents` | `0x1BFF0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SCardReleaseNewReaderEvent` | `0x1BFF0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `SCardAudit` | `0x1C520` | 347 | UnwindData |  |
| 27 | `SCardGetAttrib` | `0x1C690` | 1,475 | UnwindData |  |
| 40 | `SCardGetTransmitCount` | `0x1CC60` | 210 | UnwindData |  |
| 64 | `SCardReconnect` | `0x1CD40` | 186 | UnwindData |  |
| 69 | `SCardSetAttrib` | `0x1CE00` | 150 | UnwindData |  |
| 72 | `SCardState` | `0x1CEA0` | 349 | UnwindData |  |
| 9 | `SCardAddReaderToGroupA` | `0x1E1B0` | 417 | UnwindData |  |
| 20 | `SCardForgetCardTypeA` | `0x1E360` | 182 | UnwindData |  |
| 22 | `SCardForgetReaderA` | `0x1E420` | 305 | UnwindData |  |
| 23 | `SCardForgetReaderGroupA` | `0x1E560` | 305 | UnwindData |  |
| 28 | `SCardGetCardTypeProviderNameA` | `0x1E6A0` | 286 | UnwindData |  |
| 30 | `SCardGetDeviceTypeIdA` | `0x1E7D0` | 318 | UnwindData |  |
| 32 | `SCardGetProviderIdA` | `0x1E920` | 331 | UnwindData |  |
| 34 | `SCardGetReaderDeviceInstanceIdA` | `0x1EA80` | 393 | UnwindData |  |
| 36 | `SCardGetReaderIconA` | `0x1EC10` | 376 | UnwindData |  |
| 41 | `SCardIntroduceCardTypeA` | `0x1ED90` | 263 | UnwindData |  |
| 43 | `SCardIntroduceReaderA` | `0x1EEA0` | 417 | UnwindData |  |
| 44 | `SCardIntroduceReaderGroupA` | `0x1F050` | 287 | UnwindData |  |
| 48 | `SCardListCardsA` | `0x1F180` | 243 | UnwindData |  |
| 50 | `SCardListInterfacesA` | `0x1F280` | 362 | UnwindData |  |
| 52 | `SCardListReaderGroupsA` | `0x1F3F0` | 295 | UnwindData |  |
| 56 | `SCardListReadersWithDeviceInstanceIdA` | `0x1F520` | 783 | UnwindData |  |
| 58 | `SCardLocateCardsA` | `0x1F840` | 1,302 | UnwindData |  |
| 59 | `SCardLocateCardsByATRA` | `0x1FD60` | 357 | UnwindData |  |
| 62 | `SCardReadCacheA` | `0x1FED0` | 40 | UnwindData |  |
| 67 | `SCardRemoveReaderFromGroupA` | `0x1FF00` | 417 | UnwindData |  |
| 70 | `SCardSetCardTypeProviderNameA` | `0x200B0` | 293 | UnwindData |  |
| 76 | `SCardWriteCacheA` | `0x201E0` | 38 | UnwindData |  |
| 10 | `SCardAddReaderToGroupW` | `0x204F0` | 420 | UnwindData |  |
| 21 | `SCardForgetCardTypeW` | `0x206A0` | 182 | UnwindData |  |
| 24 | `SCardForgetReaderGroupW` | `0x20760` | 308 | UnwindData |  |
| 25 | `SCardForgetReaderW` | `0x208A0` | 308 | UnwindData |  |
| 33 | `SCardGetProviderIdW` | `0x209E0` | 331 | UnwindData |  |
| 35 | `SCardGetReaderDeviceInstanceIdW` | `0x20B40` | 300 | UnwindData |  |
| 42 | `SCardIntroduceCardTypeW` | `0x20C80` | 263 | UnwindData |  |
| 45 | `SCardIntroduceReaderGroupW` | `0x20D90` | 290 | UnwindData |  |
| 46 | `SCardIntroduceReaderW` | `0x20EC0` | 420 | UnwindData |  |
| 51 | `SCardListInterfacesW` | `0x21070` | 362 | UnwindData |  |
| 53 | `SCardListReaderGroupsW` | `0x211E0` | 298 | UnwindData |  |
| 57 | `SCardListReadersWithDeviceInstanceIdW` | `0x21310` | 649 | UnwindData |  |
| 60 | `SCardLocateCardsByATRW` | `0x215A0` | 357 | UnwindData |  |
| 61 | `SCardLocateCardsW` | `0x21710` | 1,098 | UnwindData |  |
| 68 | `SCardRemoveReaderFromGroupW` | `0x21B60` | 420 | UnwindData |  |
| 71 | `SCardSetCardTypeProviderNameW` | `0x21D10` | 293 | UnwindData |  |
| 79 | `g_rgSCardT0Pci` | `0x31F08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `g_rgSCardT1Pci` | `0x31F10` | 1,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `g_rgSCardRawPci` | `0x32308` | 0 | Indeterminate |  |
