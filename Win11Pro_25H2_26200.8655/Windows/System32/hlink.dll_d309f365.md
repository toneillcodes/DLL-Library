# Binary Specification: hlink.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\hlink.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d309f365ee80d85e4531c6a63771117169f33bfb03e1f796bb29f164b67a9a02`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `DllCanUnloadNow` | `0x2A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `DllGetClassObject` | `0x2AA0` | 23,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `HlinkClone` | `0x87D0` | 445 | UnwindData |  |
| 6 | `HlinkCreateBrowseContext` | `0x89A0` | 154 | UnwindData |  |
| 32 | `HlinkCreateExtensionServices` | `0x8A40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `HlinkCreateFromData` | `0x8A70` | 565 | UnwindData |  |
| 3 | `HlinkCreateFromMoniker` | `0x8CB0` | 113 | UnwindData |  |
| 4 | `HlinkCreateFromString` | `0x8D30` | 97 | UnwindData |  |
| 23 | `HlinkCreateShortcut` | `0x8DA0` | 255 | UnwindData |  |
| 29 | `HlinkCreateShortcutFromMoniker` | `0x8EB0` | 53 | UnwindData |  |
| 27 | `HlinkCreateShortcutFromString` | `0x8EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `HlinkGetSpecialReference` | `0x8F00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `HlinkGetValueFromParams` | `0x8F30` | 244 | UnwindData |  |
| 25 | `HlinkIsShortcut` | `0x9030` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `HlinkNavigate` | `0x90C0` | 331 | UnwindData |  |
| 8 | `HlinkNavigateToStringReference` | `0x9220` | 160 | UnwindData |  |
| 9 | `HlinkOnNavigate` | `0x92D0` | 130 | UnwindData |  |
| 12 | `HlinkOnRenameDocument` | `0x9360` | 127 | UnwindData |  |
| 18 | `HlinkParseDisplayName` | `0x93F0` | 101 | UnwindData |  |
| 33 | `HlinkPreprocessMoniker` | `0x9460` | 298 | UnwindData |  |
| 20 | `HlinkQueryCreateFromData` | `0x9590` | 246 | UnwindData |  |
| 14 | `HlinkResolveMonikerForData` | `0x9690` | 63 | UnwindData |  |
| 24 | `HlinkResolveShortcut` | `0x96E0` | 369 | UnwindData |  |
| 30 | `HlinkResolveShortcutToMoniker` | `0x9860` | 45 | UnwindData |  |
| 26 | `HlinkResolveShortcutToString` | `0x98A0` | 56 | UnwindData |  |
| 15 | `HlinkResolveStringForData` | `0x98E0` | 278 | UnwindData |  |
| 21 | `HlinkSetSpecialReference` | `0x9A00` | 593 | UnwindData |  |
| 11 | `HlinkUpdateStackItem` | `0x9C60` | 94 | UnwindData |  |
| 16 | `OleSaveToStreamEx` | `0x9CD0` | 243 | UnwindData |  |
| 19 | `DllRegisterServer` | `0xEC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `DllUnregisterServer` | `0xEC80` | 61 | UnwindData |  |
| 31 | `HlinkTranslateURL` | `0x10680` | 232 | UnwindData |  |
