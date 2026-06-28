# Binary Specification: shell32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\shell32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `603a982048f5336ae8b0e0319c90d4ff31491dc268a4ea0a6108b8bd0c37fb09`
* **Total Exported Functions:** 842

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 102 | `SHCoCreateInstance` | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-shell-shellcom-l1-1-0.SHCoCreateInstance` |
| 332 | `SHCoCreateInstanceWorker` | `0x0` | - | Forwarded | Forwarded to: `ext-ms-win-shell32-shellcom-l1-1-0.SHCoCreateInstanceWorker` |
| 183 | `ShellMessageBoxA` | `0x0` | - | Forwarded | Forwarded to: `shlwapi.ShellMessageBoxA` |
| 182 | `ShellMessageBoxW` | `0x0` | - | Forwarded | Forwarded to: `shlwapi.ShellMessageBoxW` |
| 5 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#35` |
| 7 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#192` |
| 8 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#193` |
| 26 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#36` |
| 30 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathBuildRootW` |
| 31 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathFindExtensionW` |
| 32 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathAddBackslashW` |
| 33 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathRemoveBlanksW` |
| 34 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathFindFileNameW` |
| 37 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathCombineW` |
| 38 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathStripPathW` |
| 39 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathIsUNCW` |
| 40 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathIsRelativeW` |
| 46 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathMatchSpecW` |
| 48 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathSetDlgItemPathW` |
| 50 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathStripToRootW` |
| 52 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathGetArgsW` |
| 53 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#388` |
| 55 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathQuoteSpacesW` |
| 56 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathUnquoteSpacesW` |
| 57 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathGetDriveNumberW` |
| 78 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#37` |
| 79 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#38` |
| 82 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#39` |
| 84 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#40` |
| 86 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#41` |
| 87 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#42` |
| 93 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shcore.Win32CreateDirectory` |
| 96 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#43` |
| 101 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#1` |
| 104 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#2` |
| 105 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#3` |
| 106 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#4` |
| 107 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#5` |
| 108 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#6` |
| 109 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#7` |
| 110 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#8` |
| 111 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#9` |
| 112 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#10` |
| 113 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#11` |
| 114 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#12` |
| 115 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#13` |
| 116 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#14` |
| 117 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#15` |
| 118 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#16` |
| 120 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#17` |
| 121 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#44` |
| 122 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#45` |
| 123 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#46` |
| 124 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#18` |
| 126 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#47` |
| 127 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#371` |
| 130 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#48` |
| 140 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#19` |
| 141 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#20` |
| 142 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#21` |
| 143 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#22` |
| 144 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#23` |
| 145 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathFindOnPathW` |
| 146 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#49` |
| 148 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#50` |
| 151 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#51` |
| 158 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#389` |
| 159 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathIsDirectoryW` |
| 161 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#214` |
| 163 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#52` |
| 166 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#53` |
| 177 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#54` |
| 185 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#390` |
| 187 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#235` |
| 197 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#55` |
| 198 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#56` |
| 202 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#57` |
| 216 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#24` |
| 217 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#25` |
| 218 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#26` |
| 219 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#27` |
| 220 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#28` |
| 221 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#29` |
| 222 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#30` |
| 223 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#31` |
| 224 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#32` |
| 225 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#33` |
| 227 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#34` |
| 230 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#372` |
| 233 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#58` |
| 234 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#59` |
| 235 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#212` |
| 242 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#373` |
| 243 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#374` |
| 246 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#375` |
| 247 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#376` |
| 248 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#377` |
| 249 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathParseIconLocationW` |
| 250 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathRemoveExtensionW` |
| 251 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathRemoveArgsW` |
| 252 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `api-ms-win-core-url-l1-1-0.PathIsURLW` |
| 253 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#378` |
| 520 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#60` |
| 521 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#61` |
| 522 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#62` |
| 523 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#63` |
| 525 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#234` |
| 640 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#64` |
| 641 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#65` |
| 643 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#66` |
| 646 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#67` |
| 648 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#379` |
| 650 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `shlwapi.PathIsSameRootW` |
| 653 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#68` |
| 681 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#428` |
| 691 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#216` |
| 700 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#380` |
| 703 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHLWAPI.#269` |
| 704 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHLWAPI.#270` |
| 707 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#69` |
| 708 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#70` |
| 712 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#71` |
| 715 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#191` |
| 719 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#478` |
| 720 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#72` |
| 721 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#73` |
| 722 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#236` |
| 724 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#381` |
| 725 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#74` |
| 726 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#75` |
| 731 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#479` |
| 732 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#480` |
| 745 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#382` |
| 749 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#76` |
| 756 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#77` |
| 762 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#383` |
| 766 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#385` |
| 786 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#237` |
| 820 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#249` |
| 821 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#250` |
| 822 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#251` |
| 826 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#252` |
| 827 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#253` |
| 832 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#387` |
| 834 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#254` |
| 835 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#255` |
| 836 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#256` |
| 837 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#257` |
| 838 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#258` |
| 839 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#259` |
| 841 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#424` |
| 842 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#425` |
| 843 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#386` |
| 852 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#391` |
| 854 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#260` |
| 856 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#423` |
| 857 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#426` |
| 858 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#392` |
| 861 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#261` |
| 863 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#262` |
| 867 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#263` |
| 868 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#264` |
| 869 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#384` |
| 872 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#265` |
| 889 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#474` |
| 890 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#475` |
| 892 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#476` |
| 902 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#473` |
| 909 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#477` |
| 702 | *Ordinal Only* | `0xCDC0` | 224 | UnwindData |  |
| 584 | `Shell_NotifyIconW` | `0x10F10` | 1,940 | UnwindData |  |
| 757 | *Ordinal Only* | `0x135C0` | 160 | UnwindData |  |
| 893 | *Ordinal Only* | `0x1B2E0` | 365 | UnwindData |  |
| 441 | `SHELL32_LookupBackIconIndex` | `0x35350` | 922 | UnwindData |  |
| 585 | `StateRepoNewMenuCache_EnsureCacheAsync` | `0x49CB0` | 57 | UnwindData |  |
| 280 | `DllGetClassObject` | `0x4A4B0` | 988 | UnwindData |  |
| 128 | *Ordinal Only* | `0x4A4B0` | 988 | UnwindData |  |
| 943 | *Ordinal Only* | `0x4EA20` | 18 | UnwindData |  |
| 907 | *Ordinal Only* | `0x54EF0` | 120 | UnwindData |  |
| 355 | `SHELL32_AddToBackIconTable` | `0x56190` | 121 | UnwindData |  |
| 319 | `SHAppBarMessage` | `0x5A490` | 997 | UnwindData |  |
| 390 | `SHELL32_CNetFolderUI_CreateInstance` | `0x7F420` | 207 | UnwindData |  |
| 336 | `SHCreateDefaultContextMenu` | `0x898B0` | 161 | UnwindData |  |
| 759 | *Ordinal Only* | `0x8D200` | 378 | UnwindData |  |
| 915 | *Ordinal Only* | `0x8D3F0` | 114 | UnwindData |  |
| 758 | *Ordinal Only* | `0x8DAE0` | 127 | UnwindData |  |
| 530 | `SHGetPropertyStoreForWindow` | `0x8EE70` | 233 | UnwindData |  |
| 878 | *Ordinal Only* | `0xAA180` | 132 | UnwindData |  |
| 134 | `DAD_DragMove` | `0xB46B0` | 165 | UnwindData |  |
| 939 | *Ordinal Only* | `0xB6DD0` | 37 | UnwindData |  |
| 200 | *Ordinal Only* | `0xB7BB0` | 307 | UnwindData |  |
| 425 | `SHELL32_GetThumbnailAdornerFromFactory2` | `0xBC1E0` | 151 | UnwindData |  |
| 256 | `SHCreateShellFolderView` | `0xBE830` | 163 | UnwindData |  |
| 825 | *Ordinal Only* | `0xC4190` | 403 | UnwindData |  |
| 847 | *Ordinal Only* | `0xC4330` | 300 | UnwindData |  |
| 611 | `UsersLibrariesFolderUI_CreateInstance` | `0xCC720` | 293 | UnwindData |  |
| 508 | `SHGetIconOverlayIndexW` | `0xCEBC0` | 292 | UnwindData |  |
| 420 | `SHELL32_GetIconOverlayManager` | `0xCECF0` | 111 | UnwindData |  |
| 885 | *Ordinal Only* | `0xE2320` | 203 | UnwindData |  |
| 471 | `SHELL32_SendToMenu_VerifyTargetedCommand` | `0xF0A60` | 108 | UnwindData |  |
| 434 | `SHELL32_IconCache_RememberRecentlyExtractedIconsW` | `0x101490` | 271 | UnwindData |  |
| 553 | `SHQueryUserNotificationState` | `0x108B20` | 167 | UnwindData |  |
| 278 | `DllCanUnloadNow` | `0x11A280` | 98 | UnwindData |  |
| 438 | `SHELL32_IsValidLinkInfo` | `0x11A2F0` | 47,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `SHELL32_IconCache_ExpandEnvAndSearchPath` | `0x125D00` | 130 | UnwindData |  |
| 341 | `SHCreateDrvExtIcon` | `0x126B10` | 184 | UnwindData |  |
| 437 | `SHELL32_IsSystemUpgradeInProgress` | `0x137A60` | 44 | UnwindData |  |
| 514 | `SHGetKnownFolderPath` | `0x140390` | 9,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `SHELL32_CallFileCopyHooks` | `0x142850` | 81 | UnwindData |  |
| 881 | *Ordinal Only* | `0x153F80` | 164 | UnwindData |  |
| 103 | `SignalFileOpen` | `0x154770` | 306 | UnwindData |  |
| 505 | `SHGetFolderPathW` | `0x1568E0` | 31,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `SHChangeNotify` | `0x15E460` | 2,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `SHGetSpecialFolderPathW` | `0x15EF00` | 2,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | *Ordinal Only* | `0x15EF00` | 2,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `CommandLineToArgvW` | `0x15F800` | 4,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 581 | `Shell_NotifyIcon` | `0x160B20` | 493 | UnwindData |  |
| 582 | `Shell_NotifyIconA` | `0x160B20` | 493 | UnwindData |  |
| 814 | *Ordinal Only* | `0x1637B0` | 153 | UnwindData |  |
| 875 | *Ordinal Only* | `0x166190` | 81 | UnwindData |  |
| 901 | *Ordinal Only* | `0x1666C0` | 180 | UnwindData |  |
| 882 | *Ordinal Only* | `0x169790` | 368 | UnwindData |  |
| 644 | `SHChangeNotification_Lock` | `0x16A380` | 1,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `SHELL32_IconOverlayManagerInit` | `0x16A770` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2002 | *Ordinal Only* | `0x16B670` | 19,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | *Ordinal Only* | `0x170100` | 51 | UnwindData |  |
| 900 | *Ordinal Only* | `0x1702E0` | 358 | UnwindData |  |
| 397 | `SHELL32_CanDisplayWin8CopyDialog` | `0x1712C0` | 46 | UnwindData |  |
| 475 | `SHELL32_SuspendUndo` | `0x173F70` | 8,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 685 | `SHPropStgCreate` | `0x175FE0` | 10,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | *Ordinal Only* | `0x1788A0` | 159 | UnwindData |  |
| 405 | `SHELL32_CreateLinkInfoW` | `0x17AF00` | 9,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `SHELL32_LookupFrontIconIndex` | `0x17D430` | 3,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 480 | `SHEnableServiceObject` | `0x17E0D0` | 5,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 925 | `CreateStorageItemFromShellItem_FullTrustCaller_ForPackage` | `0x17F6A0` | 15,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `SHELL32_CDefFolderMenu_Create2Ex` | `0x183290` | 96 | UnwindData |  |
| 916 | *Ordinal Only* | `0x1836A0` | 209 | UnwindData |  |
| 409 | `SHELL32_DestroyLinkInfo` | `0x185290` | 23,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `SHGetFolderPathEx` | `0x18AD10` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `SHGetFileInfoW` | `0x18B580` | 2,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 492 | `SHGetDesktopFolder` | `0x18BF80` | 2,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | *Ordinal Only* | `0x18C8C0` | 43 | UnwindData |  |
| 188 | *Ordinal Only* | `0x18D840` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `SHELL32_AreAllItemsAvailable` | `0x18DC20` | 1,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `SHELL32_IconCache_DoneExtractingIcons` | `0x18E250` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 645 | `SHChangeNotification_Unlock` | `0x18F700` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `SHELL32_IsGetKeyboardLayoutPresent` | `0x18FA20` | 6,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | *Ordinal Only* | `0x18FA20` | 6,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 500 | `SHGetFolderLocation` | `0x191430` | 5,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SHChangeNotifyRegister` | `0x192AC0` | 19,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `SHGetFolderPathA` | `0x1975F0` | 9,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `SHELL32_SHCreateDefaultContextMenu` | `0x199930` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `SHELL32_IconCache_AboutToExtractIcons` | `0x199B60` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `SHCreateShellItemArray` | `0x199CC0` | 2,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `SHGetSpecialFolderLocation` | `0x19A800` | 5,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `SHELL32_CFSDropTarget_CreateInstance` | `0x19BDC0` | 2,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `SHCreateShellItemArrayFromDataObject` | `0x19C5E0` | 4,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `DllRegisterServer` | `0x19D920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `DllUnregisterServer` | `0x19D920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `PifMgr_GetProperties` | `0x19D920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `PifMgr_OpenProperties` | `0x19D920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `PifMgr_SetProperties` | `0x19D920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `SHELL32_CopySecondaryTiles` | `0x19D920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `SHELL32_PifMgr_GetProperties` | `0x19D920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `SHELL32_PifMgr_OpenProperties` | `0x19D920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 448 | `SHELL32_PifMgr_SetProperties` | `0x19D920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | `ShellHookProc` | `0x19D920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | *Ordinal Only* | `0x19D920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | *Ordinal Only* | `0x19D920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `SHCreateLocalServerRunDll` | `0x19DA50` | 85 | UnwindData |  |
| 428 | `SHELL32_IconCacheDestroy` | `0x19E140` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | *Ordinal Only* | `0x19E670` | 56 | UnwindData |  |
| 4 | `SHChangeNotifyDeregister` | `0x19F270` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `SHGetKnownFolderIDList` | `0x19F490` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 477 | `SHELL32_VerifySaferTrust` | `0x19F930` | 2,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `OpenAs_RunDLL` | `0x1A0300` | 12,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `OpenAs_RunDLLA` | `0x1A0300` | 12,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `SHELL32_SHAddSparseIcon` | `0x1A3210` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `SHELL32_CreateQosRecorder` | `0x1A3560` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 586 | `StateRepoNewMenuCache_RebuildCacheAsync` | `0x1A35A0` | 135 | UnwindData |  |
| 308 | `InitNetworkAddressControl` | `0x1A3EA0` | 234 | UnwindData |  |
| 356 | `SHELL32_AddToFrontIconTable` | `0x1A5310` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `SHELL32_CDBurn_GetStagingPathOrNormalPath` | `0x1A5930` | 12,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `SHELL32_CDrivesDropTarget_Create` | `0x1A8BA0` | 3,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `SHELL32_CFSFolderCallback_Create` | `0x1A9A50` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `SHChangeNotifyRegisterThread` | `0x1A9B50` | 7,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `SHELL32_NotifyLinkTrackingServiceOfMove` | `0x1AB6E0` | 5,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | *Ordinal Only* | `0x1ACC40` | 92 | UnwindData |  |
| 688 | `SHPropStgReadMultiple` | `0x1ACCD0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `SHELL32_ResolveLinkInfoW` | `0x1ACF30` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `SHELL32_SHCreateShellFolderView` | `0x1AD200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `SHELL32_CMountPoint_IsAutoRunDriveAndEnabledByPolicy` | `0x1AD210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 923 | *Ordinal Only* | `0x1AD230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `SHELL32_GetDPIAdjustedLogicalSize` | `0x1AD250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `SHAddToRecentDocs` | `0x1AD260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `SHHandleUpdateImage` | `0x1AD280` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `GetCurrentProcessExplicitAppUserModelID` | `0x1AD2B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `SHELL32_IconCacheHandleAssociationChanged` | `0x1AD310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `SHELL32_CDBurn_GetCDInfo` | `0x1AD320` | 17,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 513 | `SHGetKnownFolderItem` | `0x1B1790` | 15,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `Shell_NotifyIconGetRect` | `0x1B55A0` | 513 | UnwindData |  |
| 391 | `SHELL32_CPL_CategoryIdArrayFromVariant` | `0x1E2750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `SHELL32_CDBurn_GetLiveFSDiscInfo` | `0x1E2760` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `SetCurrentProcessExplicitAppUserModelID` | `0x1E27F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 487 | `SHFileOperationW` | `0x1E2810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `SHELL32_CDefFolderMenu_MergeMenu` | `0x1E2830` | 2,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | *Ordinal Only* | `0x1E3300` | 18,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | *Ordinal Only* | `0x1E7C50` | 185 | UnwindData |  |
| 754 | *Ordinal Only* | `0x1EAEC0` | 108 | UnwindData |  |
| 876 | *Ordinal Only* | `0x1EE330` | 562 | UnwindData |  |
| 462 | `SHELL32_SHGetThreadUndoManager` | `0x1F3150` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `SHELL32_CLocationContextMenu_Create` | `0x1F33D0` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 543 | `SHLoadInProc` | `0x1F33D0` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `SHELL32_StampIconForFile` | `0x1F3D20` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `DriveType` | `0x1F4150` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `RealDriveType` | `0x1F4150` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `SHGetInstanceExplorer` | `0x1F4460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `SHGetFolderPathAndSubDirW` | `0x1F4480` | 13,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 587 | `StrChrA` | `0x1F7AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `StrChrIA` | `0x1F7B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 589 | `StrChrIW` | `0x1F7B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 590 | `StrChrW` | `0x1F7B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 591 | `StrCmpNA` | `0x1F7B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `StrCmpNIA` | `0x1F7B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `StrCmpNIW` | `0x1F7B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `StrCmpNW` | `0x1F7B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 599 | `StrRChrA` | `0x1F7B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 600 | `StrRChrIA` | `0x1F7B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `StrRChrIW` | `0x1F7B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `StrRChrW` | `0x1F7BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 604 | `StrRStrIA` | `0x1F7BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `StrRStrIW` | `0x1F7BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `StrStrA` | `0x1F7BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `StrStrIA` | `0x1F7BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `StrStrIW` | `0x1F7BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 610 | `StrStrW` | `0x1F7C00` | 9,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `AssocCreateForClasses` | `0x1F9F30` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `AssocGetDetailsOfPropKey` | `0x1F9FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `SHAssocEnumHandlers` | `0x1F9FF0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `SHAssocEnumHandlersForProtocolByApplication` | `0x1FA090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | *Ordinal Only* | `0x1FA0B0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `PathCleanupSpec` | `0x1FA340` | 27,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 914 | *Ordinal Only* | `0x200DC0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `RealShellExecuteA` | `0x200E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `RealShellExecuteExA` | `0x200E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `RealShellExecuteExW` | `0x200EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `RealShellExecuteW` | `0x200EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | *Ordinal Only* | `0x200EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | *Ordinal Only* | `0x200F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | *Ordinal Only* | `0x200F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | *Ordinal Only* | `0x200F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | *Ordinal Only* | `0x200F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `AssocElemCreateForKey` | `0x200F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 778 | *Ordinal Only* | `0x200FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 971 | *Ordinal Only* | `0x200FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `CheckEscapesW` | `0x200FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 711 | *Ordinal Only* | `0x201000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | *Ordinal Only* | `0x201020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 910 | *Ordinal Only* | `0x201040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | *Ordinal Only* | `0x201060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | *Ordinal Only* | `0x201080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | *Ordinal Only* | `0x2010A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | *Ordinal Only* | `0x2010C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `DAD_AutoScroll` | `0x2010E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `DAD_DragEnterEx` | `0x201100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `DAD_SetDragImage` | `0x201120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `DAD_ShowDragImage` | `0x201140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `DoEnvironmentSubstA` | `0x201160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `DoEnvironmentSubstW` | `0x201180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `DragAcceptFiles` | `0x2011A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `DragFinish` | `0x2011C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `DragQueryFile` | `0x2011E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `DragQueryFileA` | `0x2011E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `DragQueryFileAorW` | `0x201200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `DragQueryFileW` | `0x201220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | *Ordinal Only* | `0x201240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `DragQueryPoint` | `0x201260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `DuplicateIcon` | `0x201280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `ExtractAssociatedIconA` | `0x2012A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `ExtractAssociatedIconExA` | `0x2012C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `ExtractAssociatedIconExW` | `0x2012E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `ExtractAssociatedIconW` | `0x201300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `ExtractIconA` | `0x201320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `ExtractIconEx` | `0x201340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `ExtractIconExA` | `0x201340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `ExtractIconExW` | `0x201360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `ExtractIconW` | `0x201380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | *Ordinal Only* | `0x2013A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `FindExecutableA` | `0x2013C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `FindExecutableW` | `0x2013E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `FreeIconList` | `0x201400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 906 | *Ordinal Only* | `0x201420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `ILAppendID` | `0x201440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ILClone` | `0x201460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | *Ordinal Only* | `0x201460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `ILCloneFirst` | `0x201480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `ILCombine` | `0x2014A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `ILCreateFromPath` | `0x2014C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `ILCreateFromPathW` | `0x2014C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `ILCreateFromPathA` | `0x2014E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `ILFindChild` | `0x201500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ILFindLastID` | `0x201520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `ILFree` | `0x201540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | *Ordinal Only* | `0x201540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | *Ordinal Only* | `0x201560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | *Ordinal Only* | `0x201580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `ILGetNext` | `0x2015A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `ILGetSize` | `0x2015C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `ILIsEqual` | `0x2015E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `ILIsParent` | `0x201600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `ILLoadFromStreamEx` | `0x201620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `ILRemoveLastID` | `0x201640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `ILSaveToStream` | `0x201660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | *Ordinal Only* | `0x201680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `InternalExtractIconListA` | `0x2016A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `InternalExtractIconListW` | `0x2016C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | *Ordinal Only* | `0x2016E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | *Ordinal Only* | `0x201700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 942 | `IsDesktopExplorerProcess` | `0x201720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | *Ordinal Only* | `0x201740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `IsLFNDrive` | `0x201760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `IsLFNDriveW` | `0x201760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `IsLFNDriveA` | `0x201780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 941 | `IsProcessAnExplorer` | `0x2017A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | *Ordinal Only* | `0x2017C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 651 | *Ordinal Only* | `0x2017E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `OpenRegStream` | `0x201800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | *Ordinal Only* | `0x201820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | *Ordinal Only* | `0x201840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | *Ordinal Only* | `0x201860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | *Ordinal Only* | `0x201880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | *Ordinal Only* | `0x2018A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | *Ordinal Only* | `0x2018C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `PathGetShortPath` | `0x2018E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 755 | *Ordinal Only* | `0x201900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `PathIsExe` | `0x201920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | *Ordinal Only* | `0x201940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `PathIsSlowA` | `0x201960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `PathIsSlowW` | `0x201980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 713 | *Ordinal Only* | `0x2019A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | *Ordinal Only* | `0x2019C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `PathMakeUniqueName` | `0x2019E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `PathQualify` | `0x201A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | *Ordinal Only* | `0x201A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `PathResolve` | `0x201A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 970 | *Ordinal Only* | `0x201A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `PathYetAnotherMakeUniqueName` | `0x201A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `ReadCabinetState` | `0x201AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `SHAddDefaultPropertiesByExt` | `0x201AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `SHAlloc` | `0x201AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | *Ordinal Only* | `0x201B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `SHBindToFolderIDListParent` | `0x201B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `SHBindToFolderIDListParentEx` | `0x201B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `SHBindToObject` | `0x201B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `SHBindToParent` | `0x201B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `SHCLSIDFromString` | `0x201BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `SHCloneSpecialIDList` | `0x201BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 862 | *Ordinal Only* | `0x201BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `SHCreateAssociationRegistration` | `0x201C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `SHCreateDataObject` | `0x201C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `SHCreateDefaultExtractIcon` | `0x201C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `SHCreateDefaultPropertiesOp` | `0x201C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | *Ordinal Only* | `0x201C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `SHCreateDirectory` | `0x201CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `SHCreateDirectoryExA` | `0x201CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `SHCreateDirectoryExW` | `0x201CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | *Ordinal Only* | `0x201D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 743 | `SHCreateFileExtractIconW` | `0x201D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | *Ordinal Only* | `0x201D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `SHCreateItemFromIDList` | `0x201D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `SHCreateItemFromParsingName` | `0x201D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `SHCreateItemFromRelativeName` | `0x201DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `SHCreateItemInKnownFolder` | `0x201DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `SHCreateItemWithParent` | `0x201DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | *Ordinal Only* | `0x201E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 898 | *Ordinal Only* | `0x201E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | *Ordinal Only* | `0x201E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `SHCreateProcessAsUserW` | `0x201E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 791 | *Ordinal Only* | `0x201E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 788 | *Ordinal Only* | `0x201EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | *Ordinal Only* | `0x201EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 723 | *Ordinal Only* | `0x201EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `SHCreateShellItem` | `0x201F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `SHCreateShellItemArrayFromIDLists` | `0x201F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `SHCreateShellItemArrayFromShellItem` | `0x201F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `SHCreateStdEnumFmtEtc` | `0x201F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | *Ordinal Only* | `0x201F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SHDefExtractIconA` | `0x201FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SHDefExtractIconW` | `0x201FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 481 | `SHEnumerateUnreadMailAccountsW` | `0x201FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `SHEvaluateSystemCommandTemplate` | `0x202000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | *Ordinal Only* | `0x202020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | *Ordinal Only* | `0x202040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `SHExtractIconsW` | `0x202060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | *Ordinal Only* | `0x202080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `SHFindFiles` | `0x2020A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | `SHFlushSFCache` | `0x2020C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `SHFree` | `0x2020E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 777 | *Ordinal Only* | `0x202100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `SHGetAttributesFromDataObject` | `0x202120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | *Ordinal Only* | `0x202140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 860 | *Ordinal Only* | `0x202160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `SHGetDataFromIDListA` | `0x202180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `SHGetDataFromIDListW` | `0x2021A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `SHGetDiskFreeSpaceA` | `0x2021C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `SHGetDiskFreeSpaceExA` | `0x2021C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `SHGetDiskFreeSpaceExW` | `0x2021E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 497 | `SHGetFileInfo` | `0x202200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `SHGetFileInfoA` | `0x202200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 823 | *Ordinal Only* | `0x202220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | *Ordinal Only* | `0x202240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 506 | `SHGetIDListFromObject` | `0x202260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 727 | `SHGetImageList` | `0x202280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `SHGetItemFromDataObject` | `0x2022A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `SHGetItemFromObject` | `0x2022C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 515 | `SHGetLocalizedName` | `0x2022E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 946 | *Ordinal Only* | `0x202300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `SHGetMalloc` | `0x202320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | `SHGetNameFromIDList` | `0x202340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | *Ordinal Only* | `0x202360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `SHGetNewLinkInfo` | `0x202380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `SHGetNewLinkInfoA` | `0x202380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `SHGetNewLinkInfoW` | `0x2023A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 848 | *Ordinal Only* | `0x2023C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `SHGetPathFromIDList` | `0x2023E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `SHGetPathFromIDListA` | `0x2023E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | *Ordinal Only* | `0x202400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `SHGetPathFromIDListEx` | `0x202420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 529 | `SHGetPathFromIDListW` | `0x202440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 531 | `SHGetPropertyStoreFromIDList` | `0x202460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 532 | `SHGetPropertyStoreFromParsingName` | `0x202480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `SHGetRealIDL` | `0x2024A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `SHGetSetFolderCustomSettings` | `0x2024C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `SHGetSetSettings` | `0x2024E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 533 | `SHGetSettings` | `0x202500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `SHGetStockIconInfo` | `0x202520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `SHGetTemporaryPropertyForItem` | `0x202540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | *Ordinal Only* | `0x202560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `SHGetUnreadMailCountW` | `0x202580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | *Ordinal Only* | `0x2025A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `SHILCreateFromPath` | `0x2025C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | *Ordinal Only* | `0x2025E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `SHIsFileAvailableOffline` | `0x202600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | *Ordinal Only* | `0x202620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 544 | `SHLoadNonloadedIconOverlayIdentifiers` | `0x202640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | *Ordinal Only* | `0x202660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 790 | *Ordinal Only* | `0x202680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 787 | *Ordinal Only* | `0x2026A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 792 | *Ordinal Only* | `0x2026C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `SHMapPIDLToSystemImageListIndex` | `0x2026E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | *Ordinal Only* | `0x202700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `SHParseDisplayName` | `0x202720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 551 | `SHQueryRecycleBinA` | `0x202740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `SHQueryRecycleBinW` | `0x202760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 922 | *Ordinal Only* | `0x202780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `SHRemoveLocalizedName` | `0x2027A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | *Ordinal Only* | `0x2027C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `SHRestricted` | `0x2027E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 556 | `SHSetDefaultProperties` | `0x202800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `SHSetLocalizedName` | `0x202820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 559 | `SHSetTemporaryPropertyForItem` | `0x202840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `SHSetUnreadMailCountW` | `0x202860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | *Ordinal Only* | `0x202880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | *Ordinal Only* | `0x2028A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `SHSimpleIDListFromPath` | `0x2028C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | *Ordinal Only* | `0x2028E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `SHTestTokenMembership` | `0x202900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | *Ordinal Only* | `0x202920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 562 | `SHUpdateRecycleBinIcon` | `0x202940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `SHValidateUNC` | `0x202960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | *Ordinal Only* | `0x202980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 899 | *Ordinal Only* | `0x2029A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | *Ordinal Only* | `0x2029C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | *Ordinal Only* | `0x2029E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `ShellExec_RunDLL` | `0x202A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `ShellExec_RunDLLA` | `0x202A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 572 | `ShellExec_RunDLLW` | `0x202A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 573 | `ShellExecuteA` | `0x202A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 574 | `ShellExecuteEx` | `0x202A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 575 | `ShellExecuteExA` | `0x202A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 576 | `ShellExecuteExW` | `0x202A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 577 | `ShellExecuteW` | `0x202AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `Shell_GetCachedImageIndex` | `0x202AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 579 | `Shell_GetCachedImageIndexA` | `0x202AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `Shell_GetCachedImageIndexW` | `0x202B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `Shell_GetImageLists` | `0x202B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `Shell_MergeMenus` | `0x202B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | *Ordinal Only* | `0x202B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 682 | `StgMakeUniqueName` | `0x202B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 612 | `WOWShellExecute` | `0x202BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `Win32DeleteFile` | `0x202BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | *Ordinal Only* | `0x202BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `WriteCabinetState` | `0x202C00` | 6,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | *Ordinal Only* | `0x204550` | 174 | UnwindData |  |
| 595 | `StrNCmpA` | `0x204610` | 187 | UnwindData |  |
| 596 | `StrNCmpIA` | `0x2046E0` | 187 | UnwindData |  |
| 597 | `StrNCmpIW` | `0x2047B0` | 196 | UnwindData |  |
| 598 | `StrNCmpW` | `0x204880` | 220 | UnwindData |  |
| 603 | `StrRStrA` | `0x204970` | 205 | UnwindData |  |
| 606 | `StrRStrW` | `0x204A50` | 214 | UnwindData |  |
| 62 | `PickIconDlg` | `0x205140` | 38 | UnwindData |  |
| 13 | `PifMgr_CloseProperties` | `0x205FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `SHELL32_PifMgr_CloseProperties` | `0x205FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 564 | `SheChangeDirA` | `0x205FD0` | 117 | UnwindData |  |
| 565 | `SheChangeDirExW` | `0x206050` | 776 | UnwindData |  |
| 566 | `SheGetDirA` | `0x2065D0` | 177 | UnwindData |  |
| 567 | `SheSetCurDrive` | `0x206830` | 112 | UnwindData |  |
| 315 | `RegenerateUserEnvironment` | `0x207430` | 1,188 | UnwindData |  |
| 311 | `LaunchMSHelp_RunDLLW` | `0x20A2E0` | 210 | UnwindData |  |
| 316 | `RunAsNewUser_RunDLLW` | `0x20B6F0` | 223 | UnwindData |  |
| 871 | *Ordinal Only* | `0x20EAD0` | 111 | UnwindData |  |
| 133 | `OpenAs_RunDLLW` | `0x2101C0` | 275 | UnwindData |  |
| 547 | `SHOpenWithDialog` | `0x210EA0` | 515 | UnwindData |  |
| 135 | `PrepareDiscForBurnRunDllW` | `0x214510` | 397 | UnwindData |  |
| 138 | `PrintersGetCommand_RunDLL` | `0x2218A0` | 225 | UnwindData |  |
| 139 | `PrintersGetCommand_RunDLLA` | `0x2218A0` | 225 | UnwindData |  |
| 150 | `PrintersGetCommand_RunDLLW` | `0x221990` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | *Ordinal Only* | `0x2221F0` | 334 | UnwindData |  |
| 205 | *Ordinal Only* | `0x222350` | 370 | UnwindData |  |
| 211 | *Ordinal Only* | `0x222570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | *Ordinal Only* | `0x222590` | 285 | UnwindData |  |
| 214 | *Ordinal Only* | `0x2226C0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `SHInvokePrinterCommandA` | `0x2227A0` | 219 | UnwindData |  |
| 541 | `SHInvokePrinterCommandW` | `0x222890` | 501 | UnwindData |  |
| 228 | `SHHelpShortcuts_RunDLL` | `0x222A90` | 158 | UnwindData |  |
| 229 | `SHHelpShortcuts_RunDLLA` | `0x222A90` | 158 | UnwindData |  |
| 238 | `SHHelpShortcuts_RunDLLW` | `0x222B40` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `SHObjectProperties` | `0x222CC0` | 333 | UnwindData |  |
| 924 | *Ordinal Only* | `0x222E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 937 | `CStorageItem_GetValidatedStorageItemObject` | `0x222E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 896 | *Ordinal Only* | `0x222E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 935 | `CreateStorageItemFromPath_FullTrustCaller` | `0x222E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 936 | `CreateStorageItemFromPath_FullTrustCaller_ForPackage` | `0x222EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `CreateStorageItemFromPath_PartialTrustCaller` | `0x222EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 921 | `CreateStorageItemFromShellItem_FullTrustCaller` | `0x222EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 929 | `CreateStorageItemFromShellItem_FullTrustCaller_ForPackage_WithProcessHandle` | `0x222F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 931 | `CreateStorageItemFromShellItem_FullTrustCaller_UseImplicitFlagsAndPackage` | `0x222F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `GetSystemPersistedStorageItemList` | `0x222F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | *Ordinal Only* | `0x222F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 940 | *Ordinal Only* | `0x222F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 760 | *Ordinal Only* | `0x222FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `SHFileOperation` | `0x222FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `SHFileOperationA` | `0x222FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 489 | `SHFreeNameMappings` | `0x222FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 933 | *Ordinal Only* | `0x223000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `SHPathPrepareForWriteA` | `0x223020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `SHPathPrepareForWriteW` | `0x223040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 932 | *Ordinal Only* | `0x223060` | 24,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `AppCompat_RunDLLW` | `0x229000` | 169 | UnwindData |  |
| 488 | `SHFormatDrive` | `0x229470` | 794 | UnwindData |  |
| 701 | `CDefFolderMenu_Create2` | `0x233AF0` | 214 | UnwindData |  |
| 828 | *Ordinal Only* | `0x233C60` | 695 | UnwindData |  |
| 829 | *Ordinal Only* | `0x234050` | 226 | UnwindData |  |
| 269 | `CallFileCopyHook` | `0x2344C0` | 197 | UnwindData |  |
| 953 | *Ordinal Only* | `0x234CE0` | 67 | UnwindData |  |
| 952 | *Ordinal Only* | `0x234EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 950 | *Ordinal Only* | `0x234F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 951 | *Ordinal Only* | `0x234F30` | 38 | UnwindData |  |
| 949 | *Ordinal Only* | `0x234F60` | 38 | UnwindData |  |
| 948 | *Ordinal Only* | `0x234F90` | 25 | UnwindData |  |
| 947 | *Ordinal Only* | `0x234FB0` | 25 | UnwindData |  |
| 733 | *Ordinal Only* | `0x240790` | 69 | UnwindData |  |
| 274 | `Control_RunDLL` | `0x242A30` | 114 | UnwindData |  |
| 275 | `Control_RunDLLA` | `0x242A30` | 114 | UnwindData |  |
| 276 | `Control_RunDLLAsUserW` | `0x242AB0` | 23 | UnwindData |  |
| 44 | *Ordinal Only* | `0x242AD0` | 23 | UnwindData |  |
| 277 | `Control_RunDLLW` | `0x242AF0` | 482 | UnwindData |  |
| 912 | *Ordinal Only* | `0x24CF20` | 210 | UnwindData |  |
| 744 | *Ordinal Only* | `0x24DA60` | 40 | UnwindData |  |
| 763 | *Ordinal Only* | `0x24DA90` | 27 | UnwindData |  |
| 22 | `DAD_DragEnterEx2` | `0x24ECE0` | 126 | UnwindData |  |
| 132 | `DAD_DragLeave` | `0x24EE10` | 47 | UnwindData |  |
| 88 | `SHDoDragDrop` | `0x24EEF0` | 421 | UnwindData |  |
| 884 | *Ordinal Only* | `0x24F0A0` | 437 | UnwindData |  |
| 254 | *Ordinal Only* | `0x24F6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | *Ordinal Only* | `0x24F6E0` | 75 | UnwindData |  |
| 54 | *Ordinal Only* | `0x24F740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `RestartDialog` | `0x24F760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `RestartDialogEx` | `0x24F770` | 225 | UnwindData |  |
| 279 | `DllGetActivationFactory` | `0x2500C0` | 45 | UnwindData |  |
| 281 | `DllGetVersion` | `0x25A680` | 198 | UnwindData |  |
| 282 | `DllInstall` | `0x25A750` | 815 | UnwindData |  |
| 613 | `WaitForExplorerRestartW` | `0x25AA90` | 324 | UnwindData |  |
| 905 | *Ordinal Only* | `0x261C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `IsNetDrive` | `0x261CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `IsUserAnAdmin` | `0x261CC0` | 66 | UnwindData |  |
| 502 | `SHGetFolderPathAndSubDirA` | `0x261D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | `SHGetSpecialFolderPathA` | `0x261D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 690 | *Ordinal Only* | `0x261D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | *Ordinal Only* | `0x261D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `SHOpenFolderAndSelectItems` | `0x261D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 689 | `SHPropStgWriteMultiple` | `0x261DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 555 | `SHResolveLibrary` | `0x261DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `SHSetFolderPathA` | `0x261DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `SHSetFolderPathW` | `0x261E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `SHSetInstanceExplorer` | `0x261E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `SHSetKnownFolderPath` | `0x261E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | *Ordinal Only* | `0x261E70` | 17,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `SHELL32_CFillPropertiesTask_CreateInstance` | `0x266160` | 70,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | *Ordinal Only* | `0x277590` | 168 | UnwindData |  |
| 469 | `SHELL32_SHUICommandFromGUID` | `0x277640` | 240 | UnwindData |  |
| 63 | `GetFileNameFromBrowse` | `0x280740` | 67 | UnwindData |  |
| 61 | *Ordinal Only* | `0x280790` | 680 | UnwindData |  |
| 782 | *Ordinal Only* | `0x280A40` | 346 | UnwindData |  |
| 864 | *Ordinal Only* | `0x281BF0` | 66 | UnwindData |  |
| 507 | `SHGetIconOverlayIndexA` | `0x288730` | 108 | UnwindData |  |
| 258 | *Ordinal Only* | `0x288B70` | 184 | UnwindData |  |
| 891 | *Ordinal Only* | `0x28AA70` | 151 | UnwindData |  |
| 181 | *Ordinal Only* | `0x28AB10` | 162 | UnwindData |  |
| 945 | *Ordinal Only* | `0x291520` | 637 | UnwindData |  |
| 2000 | *Ordinal Only* | `0x2917B0` | 185 | UnwindData |  |
| 938 | *Ordinal Only* | `0x291D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | *Ordinal Only* | `0x291DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `SHChangeNotifySuspendResume` | `0x291DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `SHUpdateImageA` | `0x291DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `SHUpdateImageW` | `0x291E10` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `SHAddFromPropSheetExtArray` | `0x291F60` | 128 | UnwindData |  |
| 168 | `SHCreatePropSheetExtArray` | `0x291FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | *Ordinal Only* | `0x292000` | 460 | UnwindData |  |
| 169 | `SHDestroyPropSheetExtArray` | `0x2921E0` | 67 | UnwindData |  |
| 170 | `SHReplaceFromPropSheetExtArray` | `0x292230` | 127 | UnwindData |  |
| 326 | `SHBrowseForFolder` | `0x296C80` | 821 | UnwindData |  |
| 327 | `SHBrowseForFolderA` | `0x296C80` | 821 | UnwindData |  |
| 328 | `SHBrowseForFolderW` | `0x296FC0` | 625 | UnwindData |  |
| 334 | `SHCreateCategoryEnum` | `0x299450` | 316 | UnwindData |  |
| 830 | *Ordinal Only* | `0x2B9280` | 162 | UnwindData |  |
| 349 | `SHCreateQueryCancelAutoPlayMoniker` | `0x2C0B50` | 2,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `SHCreateShellFolderViewEx` | `0x2C1330` | 146 | UnwindData |  |
| 73 | `SHShellFolderView_Message` | `0x2C13D0` | 123 | UnwindData |  |
| 358 | `SHELL32_CCommonPlacesFolder_CreateInstance` | `0x2C23C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `SHELL32_CDBurn_CloseSession` | `0x2C23D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `SHELL32_CDBurn_DriveSupportedForDataBurn` | `0x2C23E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `SHELL32_CDBurn_Erase` | `0x2C23F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `SHELL32_CDBurn_GetTaskInfo` | `0x2C2400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `SHELL32_CDBurn_IsBlankDisc` | `0x2C2410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `SHELL32_CDBurn_IsBlankDisc2` | `0x2C2420` | 83 | UnwindData |  |
| 368 | `SHELL32_CDBurn_IsLiveFS` | `0x2C2480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `SHELL32_CDBurn_OnDeviceChange` | `0x2C2490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `SHELL32_CDBurn_OnEject` | `0x2C24A0` | 112 | UnwindData |  |
| 371 | `SHELL32_CDBurn_OnMediaChange` | `0x2C2520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `SHELL32_CDefFolderMenu_Create2` | `0x2C2530` | 77 | UnwindData |  |
| 375 | `SHELL32_CDrivesContextMenu_Create` | `0x2C2590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `SHELL32_CDrives_CreateSFVCB` | `0x2C25A0` | 78 | UnwindData |  |
| 381 | `SHELL32_CLibraryDropTarget_CreateInstance` | `0x2C2600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `SHELL32_CLocationFolderUI_CreateInstance` | `0x2C2610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `SHELL32_CMountPoint_DoAutorun` | `0x2C2620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `SHELL32_CMountPoint_DoAutorunPrompt` | `0x2C2630` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `SHELL32_CMountPoint_ProcessAutoRunFile` | `0x2C2660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 388 | `SHELL32_CMountPoint_WantAutorunUI` | `0x2C2670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `SHELL32_CMountPoint_WantAutorunUIGetReady` | `0x2C2680` | 75 | UnwindData |  |
| 392 | `SHELL32_CPL_IsLegacyCanonicalNameListedUnderKey` | `0x2C26E0` | 18 | UnwindData |  |
| 393 | `SHELL32_CPL_ModifyWowDisplayName` | `0x2C2700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `SHELL32_CRecentDocsContextMenu_CreateInstance` | `0x2C2710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `SHELL32_CTransferConfirmation_CreateInstance` | `0x2C2720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `SHELL32_CloseAutoplayPrompt` | `0x2C2730` | 169 | UnwindData |  |
| 399 | `SHELL32_CommandLineFromMsiDescriptor` | `0x2C27E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `SHELL32_CreateConfirmationInterrupt` | `0x2C2800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `SHELL32_CreateConflictInterrupt` | `0x2C2810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `SHELL32_CreateDefaultOperationDataProvider` | `0x2C2820` | 210 | UnwindData |  |
| 404 | `SHELL32_CreateFileFolderContextMenu` | `0x2C2900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `SHELL32_CreateSharePointView` | `0x2C2910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `SHELL32_Create_IEnumUICommand` | `0x2C2920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `SHELL32_EncryptDirectory` | `0x2C2930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `SHELL32_EncryptedFileKeyInfo` | `0x2C2940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `SHELL32_EnumCommonTasks` | `0x2C2960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `SHELL32_FreeEncryptedFileKeyInfo` | `0x2C2970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `SHELL32_GenerateAppID` | `0x2C2990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `SHELL32_GetAppIDRoot` | `0x2C29A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `SHELL32_GetCommandProviderForFolderType` | `0x2C29B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `SHELL32_GetDiskCleanupPath` | `0x2C29D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `SHELL32_GetFileNameFromBrowse` | `0x2C29E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `SHELL32_GetLinkInfoData` | `0x2C29F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `SHELL32_GetRatingBucket` | `0x2C2A10` | 30 | UnwindData |  |
| 423 | `SHELL32_GetSqmableFileName` | `0x2C2A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `SHELL32_GetThumbnailAdornerFromFactory` | `0x2C2A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `SHELL32_HandleUnrecognizedFileSystem` | `0x2C2A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `SHELL32_IconCacheCreate` | `0x2C2A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `SHELL32_IconCacheRestore` | `0x2C2A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `SHELL32_LegacyEnumSpecialTasksByType` | `0x2C2A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `SHELL32_LegacyEnumTasks` | `0x2C2AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `SHELL32_NormalizeRating` | `0x2C2AB0` | 53 | UnwindData |  |
| 449 | `SHELL32_Printers_CreateBindInfo` | `0x2C2AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `SHELL32_Printjob_GetPidl` | `0x2C2B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `SHELL32_PurgeSystemIcon` | `0x2C2B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | `SHELL32_RefreshOverlayImages` | `0x2C2B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `SHELL32_SHCreateByValueOperationInterrupt` | `0x2C2B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `SHELL32_SHCreateLocalServer` | `0x2C2B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `SHELL32_SHDuplicateEncryptionInfoFile` | `0x2C2B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 460 | `SHELL32_SHEncryptFile` | `0x2C2B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 461 | `SHELL32_SHFormatDriveAsync` | `0x2C2B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `SHELL32_SHGetUserNameW` | `0x2C2B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `SHELL32_SHIsVirtualDevice` | `0x2C2BB0` | 92 | UnwindData |  |
| 465 | `SHELL32_SHLaunchPropSheet` | `0x2C2C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `SHELL32_SHLogILFromFSIL` | `0x2C2C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `SHELL32_SHOpenWithDialog` | `0x2C2C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `SHELL32_SHStartNetConnectionDialogW` | `0x2C2C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `SHStartNetConnectionDialogW` | `0x2C2C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | *Ordinal Only* | `0x2C2C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `SHELL32_ShowHideIconOnlyOnDesktop` | `0x2C2C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `SHELL32_SimpleRatingToFilterCondition` | `0x2C2C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 476 | `SHELL32_TryVirtualDiscImageDriveEject` | `0x2C2CA0` | 125 | UnwindData |  |
| 478 | `SHEmptyRecycleBinA` | `0x2C3100` | 150 | UnwindData |  |
| 479 | `SHEmptyRecycleBinW` | `0x2C31A0` | 118 | UnwindData |  |
| 483 | `SHExecuteErrorMessageBox` | `0x2C4BC0` | 157 | UnwindData |  |
| 149 | `SHFind_InitMenuPopup` | `0x2C5720` | 163 | UnwindData |  |
| 811 | *Ordinal Only* | `0x2C6170` | 444 | UnwindData |  |
| 261 | *Ordinal Only* | `0x2C6340` | 37 | UnwindData |  |
| 810 | *Ordinal Only* | `0x2C6370` | 779 | UnwindData |  |
| 262 | *Ordinal Only* | `0x2C6690` | 1,094 | UnwindData |  |
| 496 | `SHGetDriveMedia` | `0x2CA920` | 171 | UnwindData |  |
| 748 | *Ordinal Only* | `0x2CB110` | 84 | UnwindData |  |
| 747 | `SHLimitInputEdit` | `0x2CB170` | 211 | UnwindData |  |
| 888 | *Ordinal Only* | `0x2CB250` | 135 | UnwindData |  |
| 716 | `SHMultiFileProperties` | `0x2CBA60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `SHOpenPropSheetW` | `0x2CBA80` | 829 | UnwindData |  |
| 546 | `SHOpenOrGetFolderView` | `0x2CC0D0` | 313 | UnwindData |  |
| 944 | *Ordinal Only* | `0x2CC210` | 612 | UnwindData |  |
| 12 | *Ordinal Only* | `0x2CC6A0` | 141 | UnwindData |  |
| 271 | *Ordinal Only* | `0x2CC740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | *Ordinal Only* | `0x2CC760` | 12,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | *Ordinal Only* | `0x2CC760` | 12,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | *Ordinal Only* | `0x2CF660` | 660 | UnwindData |  |
| 568 | `ShellAboutA` | `0x2DD0F0` | 296 | UnwindData |  |
| 569 | `ShellAboutW` | `0x2DD220` | 204 | UnwindData |  |
| 2001 | *Ordinal Only* | `0x2DDDC0` | 84 | UnwindData |  |
| 859 | *Ordinal Only* | `0x2E3790` | 1,701,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | *Ordinal Only* | `0x482EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | *Ordinal Only* | `0x482EB0` | 181 | UnwindData |  |
| 312 | `Options_RunDLL` | `0x488420` | 79 | UnwindData |  |
| 313 | `Options_RunDLLA` | `0x488420` | 79 | UnwindData |  |
| 314 | `Options_RunDLLW` | `0x488480` | 79 | UnwindData |  |
| 470 | `SHELL32_SendToMenu_InvokeTargetedCommand` | `0x4893D0` | 171 | UnwindData |  |
| 561 | `SHShowManageLibraryUI` | `0x4D2830` | 115,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 883 | *Ordinal Only* | `0x4EED10` | 61 | UnwindData |  |
| 845 | *Ordinal Only* | `0x4EEFE0` | 867 | UnwindData |  |
| 816 | *Ordinal Only* | `0x4EF350` | 161 | UnwindData |  |
| 818 | *Ordinal Only* | `0x4EFE30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | *Ordinal Only* | `0x4EFE40` | 171 | UnwindData |  |
| 817 | *Ordinal Only* | `0x4F0920` | 229 | UnwindData |  |
| 812 | *Ordinal Only* | `0x4F2B00` | 154 | UnwindData |  |
| 813 | *Ordinal Only* | `0x4F2BA0` | 215 | UnwindData |  |
| 83 | `CIDLData_CreateFromIDArray` | `0x568520` | 42 | UnwindData |  |
