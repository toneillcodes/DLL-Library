# Binary Specification: MessageBus.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\Display.NvContainer\MessageBus.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1588f4e2298120143ca12389b8075959cbc3fb1acd32327ca83c8686c7c85cc3`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `generateMessageBusUniqueId` | `0x13FC60` | 220 | UnwindData |  |
| 2 | `getMessageBusInterface` | `0x13FD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `getMessageBusInterfaceWithConfig` | `0x13FD50` | 344 | UnwindData |  |
| 4 | `getSharedMessageBusInterface` | `0x13FEB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `getSharedMessageBusInterfaceWithConfig` | `0x13FEC0` | 1,064 | UnwindData |  |
| 12 | `releaseMessageBusInterface` | `0x1402F0` | 381 | UnwindData |  |
| 6 | `messageBusAddObserver` | `0x142930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `messageBusDelete` | `0x142940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `messageBusNew` | `0x142960` | 97 | UnwindData |  |
| 9 | `messageBusPostEncryptedMessage` | `0x1429D0` | 44 | UnwindData |  |
| 10 | `messageBusPostMessage` | `0x142A00` | 44 | UnwindData |  |
| 11 | `messageBusRemoveObserver` | `0x142A30` | 4,028,332 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
