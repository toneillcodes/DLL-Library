# Binary Specification: shell32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\shell32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `509f7f2fc54c7f176c169e2a2577a163aab420a3634195c665e0c462bef31da5`
* **Total Exported Functions:** 843

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
| 200 | *Ordinal Only* | `0xD810` | 307 | UnwindData |  |
| 939 | *Ordinal Only* | `0xF050` | 37 | UnwindData |  |
| 134 | `DAD_DragMove` | `0x10CB0` | 165 | UnwindData |  |
| 702 | *Ordinal Only* | `0x15320` | 224 | UnwindData |  |
| 585 | `Shell_NotifyIconW` | `0x17750` | 1,940 | UnwindData |  |
| 757 | *Ordinal Only* | `0x19E00` | 160 | UnwindData |  |
| 319 | `SHAppBarMessage` | `0x3F890` | 997 | UnwindData |  |
| 943 | *Ordinal Only* | `0x643C0` | 18 | UnwindData |  |
| 280 | `DllGetClassObject` | `0x6ABD0` | 778 | UnwindData |  |
| 128 | *Ordinal Only* | `0x6ABD0` | 778 | UnwindData |  |
| 893 | *Ordinal Only* | `0x71BF0` | 365 | UnwindData |  |
| 586 | `StateRepoNewMenuCache_EnsureCacheAsync` | `0x7A2A0` | 57 | UnwindData |  |
| 390 | `SHELL32_CNetFolderUI_CreateInstance` | `0x82900` | 207 | UnwindData |  |
| 336 | `SHCreateDefaultContextMenu` | `0x8B650` | 161 | UnwindData |  |
| 759 | *Ordinal Only* | `0x8EF70` | 378 | UnwindData |  |
| 915 | *Ordinal Only* | `0x8F160` | 114 | UnwindData |  |
| 758 | *Ordinal Only* | `0x8F850` | 127 | UnwindData |  |
| 531 | `SHGetPropertyStoreForWindow` | `0x90BD0` | 233 | UnwindData |  |
| 509 | `SHGetIconOverlayIndexW` | `0x95F30` | 292 | UnwindData |  |
| 420 | `SHELL32_GetIconOverlayManager` | `0x96060` | 111 | UnwindData |  |
| 878 | *Ordinal Only* | `0x982A0` | 132 | UnwindData |  |
| 907 | *Ordinal Only* | `0xA6180` | 120 | UnwindData |  |
| 355 | `SHELL32_AddToBackIconTable` | `0xA6910` | 121 | UnwindData |  |
| 442 | `SHELL32_LookupFrontIconIndex` | `0xA6A40` | 134 | UnwindData |  |
| 425 | `SHELL32_GetThumbnailAdornerFromFactory2` | `0xB4500` | 151 | UnwindData |  |
| 825 | *Ordinal Only* | `0xBA080` | 388 | UnwindData |  |
| 847 | *Ordinal Only* | `0xBA210` | 300 | UnwindData |  |
| 256 | `SHCreateShellFolderView` | `0xBFC60` | 163 | UnwindData |  |
| 612 | `UsersLibrariesFolderUI_CreateInstance` | `0xC61F0` | 293 | UnwindData |  |
| 441 | `SHELL32_LookupBackIconIndex` | `0xE1CD0` | 196 | UnwindData |  |
| 472 | `SHELL32_SendToMenu_VerifyTargetedCommand` | `0xE7FF0` | 108 | UnwindData |  |
| 434 | `SHELL32_IconCache_RememberRecentlyExtractedIconsW` | `0xFAE70` | 271 | UnwindData |  |
| 885 | *Ordinal Only* | `0x1007D0` | 203 | UnwindData |  |
| 554 | `SHQueryUserNotificationState` | `0x105A90` | 167 | UnwindData |  |
| 278 | `DllCanUnloadNow` | `0x1160E0` | 98 | UnwindData |  |
| 438 | `SHELL32_IsValidLinkInfo` | `0x116150` | 49,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `SHELL32_IconCache_ExpandEnvAndSearchPath` | `0x122200` | 130 | UnwindData |  |
| 341 | `SHCreateDrvExtIcon` | `0x123010` | 184 | UnwindData |  |
| 437 | `SHELL32_IsSystemUpgradeInProgress` | `0x132610` | 44 | UnwindData |  |
| 515 | `SHGetKnownFolderPath` | `0x13B430` | 9,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `SHELL32_CallFileCopyHooks` | `0x13D780` | 81 | UnwindData |  |
| 881 | *Ordinal Only* | `0x14EEA0` | 164 | UnwindData |  |
| 103 | `SignalFileOpen` | `0x14F690` | 306 | UnwindData |  |
| 506 | `SHGetFolderPathW` | `0x1514E0` | 29,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `SHChangeNotify` | `0x1587D0` | 2,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `SHGetSpecialFolderPathW` | `0x158FE0` | 3,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | *Ordinal Only* | `0x158FE0` | 3,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `CommandLineToArgvW` | `0x159CD0` | 5,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 582 | `Shell_NotifyIcon` | `0x15B260` | 493 | UnwindData |  |
| 583 | `Shell_NotifyIconA` | `0x15B260` | 493 | UnwindData |  |
| 814 | *Ordinal Only* | `0x15E020` | 153 | UnwindData |  |
| 875 | *Ordinal Only* | `0x160800` | 81 | UnwindData |  |
| 901 | *Ordinal Only* | `0x161000` | 180 | UnwindData |  |
| 882 | *Ordinal Only* | `0x163840` | 368 | UnwindData |  |
| 644 | `SHChangeNotification_Lock` | `0x1645B0` | 1,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `SHELL32_IconOverlayManagerInit` | `0x1649A0` | 4,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2002 | *Ordinal Only* | `0x1659D0` | 19,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | *Ordinal Only* | `0x16A610` | 51 | UnwindData |  |
| 900 | *Ordinal Only* | `0x16A660` | 358 | UnwindData |  |
| 397 | `SHELL32_CanDisplayWin8CopyDialog` | `0x16B520` | 46 | UnwindData |  |
| 476 | `SHELL32_SuspendUndo` | `0x16E3C0` | 8,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 685 | `SHPropStgCreate` | `0x1705E0` | 11,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | *Ordinal Only* | `0x1730E0` | 159 | UnwindData |  |
| 405 | `SHELL32_CreateLinkInfoW` | `0x175B10` | 11,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 481 | `SHEnableServiceObject` | `0x178860` | 7,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 925 | `CreateStorageItemFromShellItem_FullTrustCaller_ForPackage` | `0x17A6C0` | 14,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `SHELL32_CDefFolderMenu_Create2Ex` | `0x17E0B0` | 96 | UnwindData |  |
| 916 | *Ordinal Only* | `0x17E4C0` | 209 | UnwindData |  |
| 409 | `SHELL32_DestroyLinkInfo` | `0x17FF20` | 22,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `SHGetFolderPathEx` | `0x1857B0` | 2,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 500 | `SHGetFileInfoW` | `0x186120` | 2,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `SHGetDesktopFolder` | `0x186AB0` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | *Ordinal Only* | `0x187050` | 43 | UnwindData |  |
| 188 | *Ordinal Only* | `0x188100` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `SHELL32_AreAllItemsAvailable` | `0x1884B0` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `SHELL32_IconCache_DoneExtractingIcons` | `0x188A40` | 5,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 645 | `SHChangeNotification_Unlock` | `0x189E80` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `SHELL32_IsGetKeyboardLayoutPresent` | `0x18A1A0` | 6,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | *Ordinal Only* | `0x18A1A0` | 6,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `SHGetFolderLocation` | `0x18B910` | 4,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SHChangeNotifyRegister` | `0x18CC80` | 19,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `SHGetFolderPathA` | `0x191710` | 6,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `SHELL32_SHCreateDefaultContextMenu` | `0x192EF0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `SHELL32_IconCache_AboutToExtractIcons` | `0x1930D0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `SHCreateShellItemArray` | `0x1934A0` | 2,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | `SHGetSpecialFolderLocation` | `0x193FE0` | 7,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `SHELL32_CFSDropTarget_CreateInstance` | `0x195D70` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `SHCreateShellItemArrayFromDataObject` | `0x196640` | 4,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `DllRegisterServer` | `0x1978F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `DllUnregisterServer` | `0x1978F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `PifMgr_GetProperties` | `0x1978F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `PifMgr_OpenProperties` | `0x1978F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `PifMgr_SetProperties` | `0x1978F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `SHELL32_CopySecondaryTiles` | `0x1978F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `SHELL32_PifMgr_GetProperties` | `0x1978F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `SHELL32_PifMgr_OpenProperties` | `0x1978F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 448 | `SHELL32_PifMgr_SetProperties` | `0x1978F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 579 | `ShellHookProc` | `0x1978F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | *Ordinal Only* | `0x1978F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | *Ordinal Only* | `0x1978F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `SHCreateLocalServerRunDll` | `0x197A20` | 85 | UnwindData |  |
| 428 | `SHELL32_IconCacheDestroy` | `0x198110` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | *Ordinal Only* | `0x1985B0` | 56 | UnwindData |  |
| 4 | `SHChangeNotifyDeregister` | `0x1990A0` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 513 | `SHGetKnownFolderIDList` | `0x199360` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 478 | `SHELL32_VerifySaferTrust` | `0x199810` | 2,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `OpenAs_RunDLL` | `0x19A200` | 12,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `OpenAs_RunDLLA` | `0x19A200` | 12,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `SHELL32_SHAddSparseIcon` | `0x19D0E0` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `SHELL32_CreateQosRecorder` | `0x19D570` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 587 | `StateRepoNewMenuCache_RebuildCacheAsync` | `0x19D5B0` | 135 | UnwindData |  |
| 308 | `InitNetworkAddressControl` | `0x19DD00` | 234 | UnwindData |  |
| 356 | `SHELL32_AddToFrontIconTable` | `0x19F110` | 1,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `SHELL32_CDBurn_GetStagingPathOrNormalPath` | `0x19F870` | 12,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `SHELL32_CDrivesDropTarget_Create` | `0x1A28D0` | 3,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `SHELL32_CFSFolderCallback_Create` | `0x1A36F0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `SHChangeNotifyRegisterThread` | `0x1A37F0` | 6,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `SHELL32_NotifyLinkTrackingServiceOfMove` | `0x1A5000` | 5,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | *Ordinal Only* | `0x1A6540` | 92 | UnwindData |  |
| 688 | `SHPropStgReadMultiple` | `0x1A65D0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `SHELL32_ResolveLinkInfoW` | `0x1A6830` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `SHELL32_SHCreateShellFolderView` | `0x1A6B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `SHELL32_CMountPoint_IsAutoRunDriveAndEnabledByPolicy` | `0x1A6B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 923 | *Ordinal Only* | `0x1A6B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `SHELL32_GetDPIAdjustedLogicalSize` | `0x1A6B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `SHAddToRecentDocs` | `0x1A6B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `SHHandleUpdateImage` | `0x1A6B80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `GetCurrentProcessExplicitAppUserModelID` | `0x1A6BB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `SHELL32_IconCacheHandleAssociationChanged` | `0x1A6C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `SHELL32_CDBurn_GetCDInfo` | `0x1A6C20` | 15,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `SHGetKnownFolderItem` | `0x1AAA10` | 26,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `Shell_NotifyIconGetRect` | `0x1B1020` | 513 | UnwindData |  |
| 391 | `SHELL32_CPL_CategoryIdArrayFromVariant` | `0x1E19E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `SHELL32_CDBurn_GetLiveFSDiscInfo` | `0x1E19F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 564 | `SetCurrentProcessExplicitAppUserModelID` | `0x1E1A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `SHFileOperationW` | `0x1E1AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `SHELL32_CDefFolderMenu_MergeMenu` | `0x1E1AC0` | 2,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | *Ordinal Only* | `0x1E2590` | 18,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | *Ordinal Only* | `0x1E6C40` | 185 | UnwindData |  |
| 754 | *Ordinal Only* | `0x1E9BB0` | 108 | UnwindData |  |
| 876 | *Ordinal Only* | `0x1ED0D0` | 562 | UnwindData |  |
| 463 | `SHELL32_SHGetThreadUndoManager` | `0x1F1C10` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `SHELL32_CLocationContextMenu_Create` | `0x1F1E90` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 544 | `SHLoadInProc` | `0x1F1E90` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `SHELL32_StampIconForFile` | `0x1F27E0` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `DriveType` | `0x1F2C10` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `RealDriveType` | `0x1F2C10` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `SHGetInstanceExplorer` | `0x1F2F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `SHGetFolderPathAndSubDirW` | `0x1F2F40` | 13,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `StrChrA` | `0x1F65E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 589 | `StrChrIA` | `0x1F65F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 590 | `StrChrIW` | `0x1F6600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 591 | `StrChrW` | `0x1F6610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `StrCmpNA` | `0x1F6620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `StrCmpNIA` | `0x1F6630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `StrCmpNIW` | `0x1F6640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 595 | `StrCmpNW` | `0x1F6650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 600 | `StrRChrA` | `0x1F6660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `StrRChrIA` | `0x1F6670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `StrRChrIW` | `0x1F6680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `StrRChrW` | `0x1F6690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `StrRStrIA` | `0x1F66A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 606 | `StrRStrIW` | `0x1F66B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `StrStrA` | `0x1F66C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `StrStrIA` | `0x1F66D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 610 | `StrStrIW` | `0x1F66E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `StrStrW` | `0x1F66F0` | 9,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `AssocCreateForClasses` | `0x1F8A20` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `AssocGetDetailsOfPropKey` | `0x1F8AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `SHAssocEnumHandlers` | `0x1F8AE0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `SHAssocEnumHandlersForProtocolByApplication` | `0x1F8B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | *Ordinal Only* | `0x1F8BA0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `PathCleanupSpec` | `0x1F8E30` | 27,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 914 | *Ordinal Only* | `0x1FF8F0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `RealShellExecuteA` | `0x1FF990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `RealShellExecuteExA` | `0x1FF9B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `RealShellExecuteExW` | `0x1FF9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `RealShellExecuteW` | `0x1FF9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | *Ordinal Only* | `0x1FFA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | *Ordinal Only* | `0x1FFA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | *Ordinal Only* | `0x1FFA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | *Ordinal Only* | `0x1FFA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | *Ordinal Only* | `0x1FFA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `AssocElemCreateForKey` | `0x1FFAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 778 | *Ordinal Only* | `0x1FFAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 971 | *Ordinal Only* | `0x1FFAF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `CheckEscapesW` | `0x1FFB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 711 | *Ordinal Only* | `0x1FFB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | *Ordinal Only* | `0x1FFB50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 910 | *Ordinal Only* | `0x1FFB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | *Ordinal Only* | `0x1FFB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | *Ordinal Only* | `0x1FFBB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | *Ordinal Only* | `0x1FFBD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | *Ordinal Only* | `0x1FFBF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `DAD_AutoScroll` | `0x1FFC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `DAD_DragEnterEx` | `0x1FFC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `DAD_SetDragImage` | `0x1FFC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `DAD_ShowDragImage` | `0x1FFC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `DoEnvironmentSubstA` | `0x1FFC90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `DoEnvironmentSubstW` | `0x1FFCB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `DragAcceptFiles` | `0x1FFCD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `DragFinish` | `0x1FFCF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `DragQueryFile` | `0x1FFD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `DragQueryFileA` | `0x1FFD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `DragQueryFileAorW` | `0x1FFD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `DragQueryFileW` | `0x1FFD50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | *Ordinal Only* | `0x1FFD70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `DragQueryPoint` | `0x1FFD90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `DuplicateIcon` | `0x1FFDB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `ExtractAssociatedIconA` | `0x1FFDD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `ExtractAssociatedIconExA` | `0x1FFDF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `ExtractAssociatedIconExW` | `0x1FFE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `ExtractAssociatedIconW` | `0x1FFE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `ExtractIconA` | `0x1FFE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `ExtractIconEx` | `0x1FFE70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `ExtractIconExA` | `0x1FFE70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `ExtractIconExW` | `0x1FFE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `ExtractIconW` | `0x1FFEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | *Ordinal Only* | `0x1FFED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `FindExecutableA` | `0x1FFEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `FindExecutableW` | `0x1FFF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `FreeIconList` | `0x1FFF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 906 | *Ordinal Only* | `0x1FFF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `ILAppendID` | `0x1FFF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ILClone` | `0x1FFF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | *Ordinal Only* | `0x1FFF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `ILCloneFirst` | `0x1FFFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `ILCombine` | `0x1FFFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `ILCreateFromPath` | `0x1FFFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `ILCreateFromPathW` | `0x1FFFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `ILCreateFromPathA` | `0x200010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `ILFindChild` | `0x200030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ILFindLastID` | `0x200050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `ILFree` | `0x200070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | *Ordinal Only* | `0x200070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | *Ordinal Only* | `0x200090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | *Ordinal Only* | `0x2000B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `ILGetNext` | `0x2000D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `ILGetSize` | `0x2000F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `ILIsEqual` | `0x200110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `ILIsParent` | `0x200130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `ILLoadFromStreamEx` | `0x200150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `ILRemoveLastID` | `0x200170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `ILSaveToStream` | `0x200190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | *Ordinal Only* | `0x2001B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `InternalExtractIconListA` | `0x2001D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `InternalExtractIconListW` | `0x2001F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | *Ordinal Only* | `0x200210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | *Ordinal Only* | `0x200230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 942 | `IsDesktopExplorerProcess` | `0x200250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | *Ordinal Only* | `0x200270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `IsLFNDrive` | `0x200290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `IsLFNDriveW` | `0x200290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `IsLFNDriveA` | `0x2002B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 941 | `IsProcessAnExplorer` | `0x2002D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | *Ordinal Only* | `0x2002F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 651 | *Ordinal Only* | `0x200310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `OpenRegStream` | `0x200330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | *Ordinal Only* | `0x200350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | *Ordinal Only* | `0x200370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | *Ordinal Only* | `0x200390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | *Ordinal Only* | `0x2003B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | *Ordinal Only* | `0x2003D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | *Ordinal Only* | `0x2003F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `PathGetShortPath` | `0x200410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 755 | *Ordinal Only* | `0x200430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `PathIsExe` | `0x200450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | *Ordinal Only* | `0x200470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `PathIsSlowA` | `0x200490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `PathIsSlowW` | `0x2004B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 713 | *Ordinal Only* | `0x2004D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | *Ordinal Only* | `0x2004F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `PathMakeUniqueName` | `0x200510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `PathQualify` | `0x200530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | *Ordinal Only* | `0x200550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `PathResolve` | `0x200570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 970 | *Ordinal Only* | `0x200590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `PathYetAnotherMakeUniqueName` | `0x2005B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `ReadCabinetState` | `0x2005D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `SHAddDefaultPropertiesByExt` | `0x2005F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `SHAlloc` | `0x200610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | *Ordinal Only* | `0x200630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `SHBindToFolderIDListParent` | `0x200650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `SHBindToFolderIDListParentEx` | `0x200670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `SHBindToObject` | `0x200690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `SHBindToParent` | `0x2006B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `SHCLSIDFromString` | `0x2006D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `SHCloneSpecialIDList` | `0x2006F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 862 | *Ordinal Only* | `0x200710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `SHCreateAssociationRegistration` | `0x200730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `SHCreateDataObject` | `0x200750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `SHCreateDefaultExtractIcon` | `0x200770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `SHCreateDefaultPropertiesOp` | `0x200790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | *Ordinal Only* | `0x2007B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `SHCreateDirectory` | `0x2007D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `SHCreateDirectoryExA` | `0x2007F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `SHCreateDirectoryExW` | `0x200810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | *Ordinal Only* | `0x200830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 743 | `SHCreateFileExtractIconW` | `0x200850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | *Ordinal Only* | `0x200870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `SHCreateItemFromIDList` | `0x200890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `SHCreateItemFromParsingName` | `0x2008B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `SHCreateItemFromRelativeName` | `0x2008D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `SHCreateItemInKnownFolder` | `0x2008F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `SHCreateItemWithParent` | `0x200910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | *Ordinal Only* | `0x200930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 898 | *Ordinal Only* | `0x200950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | *Ordinal Only* | `0x200970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `SHCreateProcessAsUserW` | `0x200990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 791 | *Ordinal Only* | `0x2009B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 788 | *Ordinal Only* | `0x2009D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | *Ordinal Only* | `0x2009F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 723 | *Ordinal Only* | `0x200A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `SHCreateShellItem` | `0x200A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `SHCreateShellItemArrayFromIDLists` | `0x200A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `SHCreateShellItemArrayFromShellItem` | `0x200A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `SHCreateStdEnumFmtEtc` | `0x200A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | *Ordinal Only* | `0x200AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SHDefExtractIconA` | `0x200AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SHDefExtractIconW` | `0x200AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `SHEnumerateUnreadMailAccountsW` | `0x200B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `SHEvaluateSystemCommandTemplate` | `0x200B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | *Ordinal Only* | `0x200B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | *Ordinal Only* | `0x200B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `SHExtractIconsW` | `0x200B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | *Ordinal Only* | `0x200BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `SHFindFiles` | `0x200BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | `SHFlushSFCache` | `0x200BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `SHFree` | `0x200C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 777 | *Ordinal Only* | `0x200C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `SHGetAttributesFromDataObject` | `0x200C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | *Ordinal Only* | `0x200C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 860 | *Ordinal Only* | `0x200C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `SHGetDataFromIDListA` | `0x200CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 492 | `SHGetDataFromIDListW` | `0x200CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `SHGetDiskFreeSpaceA` | `0x200CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `SHGetDiskFreeSpaceExA` | `0x200CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | `SHGetDiskFreeSpaceExW` | `0x200D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `SHGetFileInfo` | `0x200D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `SHGetFileInfoA` | `0x200D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 823 | *Ordinal Only* | `0x200D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | *Ordinal Only* | `0x200D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `SHGetIDListFromObject` | `0x200D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 727 | `SHGetImageList` | `0x200DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `SHGetItemFromDataObject` | `0x200DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `SHGetItemFromObject` | `0x200DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `SHGetLocalizedName` | `0x200E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 946 | *Ordinal Only* | `0x200E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | `SHGetMalloc` | `0x200E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `SHGetNameFromIDList` | `0x200E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | *Ordinal Only* | `0x200E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `SHGetNewLinkInfo` | `0x200EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `SHGetNewLinkInfoA` | `0x200EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `SHGetNewLinkInfoW` | `0x200ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 848 | *Ordinal Only* | `0x200EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `SHGetPathFromIDList` | `0x200F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `SHGetPathFromIDListA` | `0x200F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | *Ordinal Only* | `0x200F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 529 | `SHGetPathFromIDListEx` | `0x200F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `SHGetPathFromIDListW` | `0x200F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 532 | `SHGetPropertyStoreFromIDList` | `0x200F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 533 | `SHGetPropertyStoreFromParsingName` | `0x200FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `SHGetRealIDL` | `0x200FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `SHGetSetFolderCustomSettings` | `0x200FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `SHGetSetSettings` | `0x201010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `SHGetSettings` | `0x201030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `SHGetStockIconInfo` | `0x201050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `SHGetTemporaryPropertyForItem` | `0x201070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | *Ordinal Only* | `0x201090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `SHGetUnreadMailCountW` | `0x2010B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | *Ordinal Only* | `0x2010D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `SHILCreateFromPath` | `0x2010F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | *Ordinal Only* | `0x201110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 543 | `SHIsFileAvailableOffline` | `0x201130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | *Ordinal Only* | `0x201150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `SHLoadNonloadedIconOverlayIdentifiers` | `0x201170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | *Ordinal Only* | `0x201190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 790 | *Ordinal Only* | `0x2011B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 787 | *Ordinal Only* | `0x2011D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 792 | *Ordinal Only* | `0x2011F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `SHMapPIDLToSystemImageListIndex` | `0x201210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | *Ordinal Only* | `0x201230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `SHParseDisplayName` | `0x201250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `SHQueryRecycleBinA` | `0x201270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `SHQueryRecycleBinW` | `0x201290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 922 | *Ordinal Only* | `0x2012B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 555 | `SHRemoveLocalizedName` | `0x2012D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | *Ordinal Only* | `0x2012F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `SHRestricted` | `0x201310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `SHSetDefaultProperties` | `0x201330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 559 | `SHSetLocalizedName` | `0x201350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `SHSetTemporaryPropertyForItem` | `0x201370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `SHSetUnreadMailCountW` | `0x201390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | *Ordinal Only* | `0x2013B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | *Ordinal Only* | `0x2013D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `SHSimpleIDListFromPath` | `0x2013F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | *Ordinal Only* | `0x201410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `SHTestTokenMembership` | `0x201430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | *Ordinal Only* | `0x201450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `SHUpdateRecycleBinIcon` | `0x201470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `SHValidateUNC` | `0x201490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | *Ordinal Only* | `0x2014B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 899 | *Ordinal Only* | `0x2014D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | *Ordinal Only* | `0x2014F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | *Ordinal Only* | `0x201510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `ShellExec_RunDLL` | `0x201530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 572 | `ShellExec_RunDLLA` | `0x201530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 573 | `ShellExec_RunDLLW` | `0x201550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 574 | `ShellExecuteA` | `0x201570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 575 | `ShellExecuteEx` | `0x201590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 576 | `ShellExecuteExA` | `0x201590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 577 | `ShellExecuteExW` | `0x2015B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | `ShellExecuteW` | `0x2015D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `Shell_GetCachedImageIndex` | `0x2015F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `Shell_GetCachedImageIndexA` | `0x201610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 581 | `Shell_GetCachedImageIndexW` | `0x201630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `Shell_GetImageLists` | `0x201650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `Shell_MergeMenus` | `0x201670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | *Ordinal Only* | `0x201690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 682 | `StgMakeUniqueName` | `0x2016B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 613 | `WOWShellExecute` | `0x2016D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `Win32DeleteFile` | `0x2016F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | *Ordinal Only* | `0x201710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `WriteCabinetState` | `0x201730` | 6,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | *Ordinal Only* | `0x203080` | 174 | UnwindData |  |
| 596 | `StrNCmpA` | `0x203140` | 187 | UnwindData |  |
| 597 | `StrNCmpIA` | `0x203210` | 187 | UnwindData |  |
| 598 | `StrNCmpIW` | `0x2032E0` | 196 | UnwindData |  |
| 599 | `StrNCmpW` | `0x2033B0` | 220 | UnwindData |  |
| 604 | `StrRStrA` | `0x2034A0` | 205 | UnwindData |  |
| 607 | `StrRStrW` | `0x203580` | 214 | UnwindData |  |
| 62 | `PickIconDlg` | `0x203C70` | 38 | UnwindData |  |
| 13 | `PifMgr_CloseProperties` | `0x204B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `SHELL32_PifMgr_CloseProperties` | `0x204B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 565 | `SheChangeDirA` | `0x204B50` | 117 | UnwindData |  |
| 566 | `SheChangeDirExW` | `0x204BD0` | 776 | UnwindData |  |
| 567 | `SheGetDirA` | `0x205150` | 177 | UnwindData |  |
| 568 | `SheSetCurDrive` | `0x2053B0` | 112 | UnwindData |  |
| 315 | `RegenerateUserEnvironment` | `0x205FB0` | 1,188 | UnwindData |  |
| 311 | `LaunchMSHelp_RunDLLW` | `0x209040` | 210 | UnwindData |  |
| 316 | `RunAsNewUser_RunDLLW` | `0x20A450` | 223 | UnwindData |  |
| 871 | *Ordinal Only* | `0x20C650` | 111 | UnwindData |  |
| 133 | `OpenAs_RunDLLW` | `0x20DD40` | 275 | UnwindData |  |
| 548 | `SHOpenWithDialog` | `0x20EA20` | 515 | UnwindData |  |
| 135 | `PrepareDiscForBurnRunDllW` | `0x212090` | 397 | UnwindData |  |
| 138 | `PrintersGetCommand_RunDLL` | `0x21F420` | 225 | UnwindData |  |
| 139 | `PrintersGetCommand_RunDLLA` | `0x21F420` | 225 | UnwindData |  |
| 150 | `PrintersGetCommand_RunDLLW` | `0x21F510` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | *Ordinal Only* | `0x21FD70` | 334 | UnwindData |  |
| 205 | *Ordinal Only* | `0x21FED0` | 370 | UnwindData |  |
| 211 | *Ordinal Only* | `0x2200F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | *Ordinal Only* | `0x220110` | 285 | UnwindData |  |
| 214 | *Ordinal Only* | `0x220240` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `SHInvokePrinterCommandA` | `0x220320` | 219 | UnwindData |  |
| 542 | `SHInvokePrinterCommandW` | `0x220410` | 501 | UnwindData |  |
| 228 | `SHHelpShortcuts_RunDLL` | `0x220610` | 158 | UnwindData |  |
| 229 | `SHHelpShortcuts_RunDLLA` | `0x220610` | 158 | UnwindData |  |
| 238 | `SHHelpShortcuts_RunDLLW` | `0x2206C0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `SHObjectProperties` | `0x220840` | 333 | UnwindData |  |
| 924 | *Ordinal Only* | `0x2209A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 937 | `CStorageItem_GetValidatedStorageItemObject` | `0x2209C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 896 | *Ordinal Only* | `0x2209E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 935 | `CreateStorageItemFromPath_FullTrustCaller` | `0x220A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 936 | `CreateStorageItemFromPath_FullTrustCaller_ForPackage` | `0x220A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `CreateStorageItemFromPath_PartialTrustCaller` | `0x220A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 921 | `CreateStorageItemFromShellItem_FullTrustCaller` | `0x220A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 929 | `CreateStorageItemFromShellItem_FullTrustCaller_ForPackage_WithProcessHandle` | `0x220A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 931 | `CreateStorageItemFromShellItem_FullTrustCaller_UseImplicitFlagsAndPackage` | `0x220AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `GetSystemPersistedStorageItemList` | `0x220AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | *Ordinal Only* | `0x220AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 940 | *Ordinal Only* | `0x220B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 760 | *Ordinal Only* | `0x220B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `SHFileOperation` | `0x220B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 487 | `SHFileOperationA` | `0x220B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `SHFreeNameMappings` | `0x220B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 933 | *Ordinal Only* | `0x220B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `SHPathPrepareForWriteA` | `0x220BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 551 | `SHPathPrepareForWriteW` | `0x220BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 932 | *Ordinal Only* | `0x220BE0` | 23,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `AppCompat_RunDLLW` | `0x226890` | 169 | UnwindData |  |
| 489 | `SHFormatDrive` | `0x226D00` | 794 | UnwindData |  |
| 701 | `CDefFolderMenu_Create2` | `0x2342F0` | 214 | UnwindData |  |
| 828 | *Ordinal Only* | `0x234460` | 695 | UnwindData |  |
| 829 | *Ordinal Only* | `0x234850` | 226 | UnwindData |  |
| 269 | `CallFileCopyHook` | `0x234CD0` | 197 | UnwindData |  |
| 953 | *Ordinal Only* | `0x2354F0` | 67 | UnwindData |  |
| 952 | *Ordinal Only* | `0x235750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 950 | *Ordinal Only* | `0x235770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 951 | *Ordinal Only* | `0x235790` | 38 | UnwindData |  |
| 949 | *Ordinal Only* | `0x2357C0` | 38 | UnwindData |  |
| 948 | *Ordinal Only* | `0x2357F0` | 25 | UnwindData |  |
| 947 | *Ordinal Only* | `0x235810` | 25 | UnwindData |  |
| 733 | *Ordinal Only* | `0x240F80` | 69 | UnwindData |  |
| 274 | `Control_RunDLL` | `0x244A80` | 114 | UnwindData |  |
| 275 | `Control_RunDLLA` | `0x244A80` | 114 | UnwindData |  |
| 276 | `Control_RunDLLAsUserW` | `0x244B00` | 40 | UnwindData |  |
| 44 | *Ordinal Only* | `0x244B30` | 40 | UnwindData |  |
| 277 | `Control_RunDLLW` | `0x244B60` | 497 | UnwindData |  |
| 912 | *Ordinal Only* | `0x24F3F0` | 210 | UnwindData |  |
| 744 | *Ordinal Only* | `0x24FF30` | 40 | UnwindData |  |
| 763 | *Ordinal Only* | `0x24FF60` | 27 | UnwindData |  |
| 22 | `DAD_DragEnterEx2` | `0x2514C0` | 126 | UnwindData |  |
| 132 | `DAD_DragLeave` | `0x2515F0` | 47 | UnwindData |  |
| 88 | `SHDoDragDrop` | `0x2516D0` | 421 | UnwindData |  |
| 884 | *Ordinal Only* | `0x251880` | 437 | UnwindData |  |
| 254 | *Ordinal Only* | `0x251EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | *Ordinal Only* | `0x251EC0` | 75 | UnwindData |  |
| 54 | *Ordinal Only* | `0x251F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `RestartDialog` | `0x251F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `RestartDialogEx` | `0x251F50` | 225 | UnwindData |  |
| 279 | `DllGetActivationFactory` | `0x252E20` | 45 | UnwindData |  |
| 281 | `DllGetVersion` | `0x25D180` | 198 | UnwindData |  |
| 282 | `DllInstall` | `0x25D250` | 815 | UnwindData |  |
| 614 | `WaitForExplorerRestartW` | `0x25D590` | 324 | UnwindData |  |
| 905 | *Ordinal Only* | `0x2657E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `IsNetDrive` | `0x265800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `IsUserAnAdmin` | `0x265820` | 66 | UnwindData |  |
| 503 | `SHGetFolderPathAndSubDirA` | `0x265870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `SHGetSpecialFolderPathA` | `0x265890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 690 | *Ordinal Only* | `0x2658B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | *Ordinal Only* | `0x2658D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 546 | `SHOpenFolderAndSelectItems` | `0x2658F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 689 | `SHPropStgWriteMultiple` | `0x265910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 556 | `SHResolveLibrary` | `0x265930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `SHSetFolderPathA` | `0x265950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `SHSetFolderPathW` | `0x265970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `SHSetInstanceExplorer` | `0x265990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `SHSetKnownFolderPath` | `0x2659B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | *Ordinal Only* | `0x2659D0` | 32,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `SHELL32_CFillPropertiesTask_CreateInstance` | `0x26D7A0` | 78,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | *Ordinal Only* | `0x280C30` | 168 | UnwindData |  |
| 470 | `SHELL32_SHUICommandFromGUID` | `0x280CE0` | 240 | UnwindData |  |
| 63 | `GetFileNameFromBrowse` | `0x28CEF0` | 67 | UnwindData |  |
| 61 | *Ordinal Only* | `0x28CF40` | 671 | UnwindData |  |
| 782 | *Ordinal Only* | `0x28D1F0` | 346 | UnwindData |  |
| 864 | *Ordinal Only* | `0x28EBF0` | 66 | UnwindData |  |
| 508 | `SHGetIconOverlayIndexA` | `0x295730` | 108 | UnwindData |  |
| 258 | *Ordinal Only* | `0x295B70` | 184 | UnwindData |  |
| 891 | *Ordinal Only* | `0x297A70` | 151 | UnwindData |  |
| 181 | *Ordinal Only* | `0x297B10` | 162 | UnwindData |  |
| 945 | *Ordinal Only* | `0x29E540` | 637 | UnwindData |  |
| 2000 | *Ordinal Only* | `0x29E7D0` | 185 | UnwindData |  |
| 938 | *Ordinal Only* | `0x29ED30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | *Ordinal Only* | `0x29ED50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `SHChangeNotifySuspendResume` | `0x29ED70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `SHUpdateImageA` | `0x29ED90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `SHUpdateImageW` | `0x29EDB0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `SHAddFromPropSheetExtArray` | `0x29EF00` | 128 | UnwindData |  |
| 168 | `SHCreatePropSheetExtArray` | `0x29EF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | *Ordinal Only* | `0x29EFA0` | 460 | UnwindData |  |
| 169 | `SHDestroyPropSheetExtArray` | `0x29F180` | 67 | UnwindData |  |
| 170 | `SHReplaceFromPropSheetExtArray` | `0x29F1D0` | 127 | UnwindData |  |
| 326 | `SHBrowseForFolder` | `0x2A3C20` | 821 | UnwindData |  |
| 327 | `SHBrowseForFolderA` | `0x2A3C20` | 821 | UnwindData |  |
| 328 | `SHBrowseForFolderW` | `0x2A3F60` | 625 | UnwindData |  |
| 334 | `SHCreateCategoryEnum` | `0x2A63F0` | 316 | UnwindData |  |
| 830 | *Ordinal Only* | `0x2D45F0` | 162 | UnwindData |  |
| 349 | `SHCreateQueryCancelAutoPlayMoniker` | `0x2DC080` | 2,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `SHCreateShellFolderViewEx` | `0x2DC860` | 146 | UnwindData |  |
| 73 | `SHShellFolderView_Message` | `0x2DC900` | 123 | UnwindData |  |
| 358 | `SHELL32_CCommonPlacesFolder_CreateInstance` | `0x2DDBA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `SHELL32_CDBurn_CloseSession` | `0x2DDBB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `SHELL32_CDBurn_DriveSupportedForDataBurn` | `0x2DDBC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `SHELL32_CDBurn_Erase` | `0x2DDBD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `SHELL32_CDBurn_GetTaskInfo` | `0x2DDBE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `SHELL32_CDBurn_IsBlankDisc` | `0x2DDBF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `SHELL32_CDBurn_IsBlankDisc2` | `0x2DDC00` | 83 | UnwindData |  |
| 368 | `SHELL32_CDBurn_IsLiveFS` | `0x2DDC60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `SHELL32_CDBurn_OnDeviceChange` | `0x2DDC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `SHELL32_CDBurn_OnEject` | `0x2DDC80` | 112 | UnwindData |  |
| 371 | `SHELL32_CDBurn_OnMediaChange` | `0x2DDD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `SHELL32_CDefFolderMenu_Create2` | `0x2DDD10` | 77 | UnwindData |  |
| 375 | `SHELL32_CDrivesContextMenu_Create` | `0x2DDD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `SHELL32_CDrives_CreateSFVCB` | `0x2DDD80` | 78 | UnwindData |  |
| 381 | `SHELL32_CLibraryDropTarget_CreateInstance` | `0x2DDDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `SHELL32_CLocationFolderUI_CreateInstance` | `0x2DDDF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `SHELL32_CMountPoint_DoAutorun` | `0x2DDE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `SHELL32_CMountPoint_DoAutorunPrompt` | `0x2DDE10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `SHELL32_CMountPoint_ProcessAutoRunFile` | `0x2DDE40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 388 | `SHELL32_CMountPoint_WantAutorunUI` | `0x2DDE50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `SHELL32_CMountPoint_WantAutorunUIGetReady` | `0x2DDE60` | 75 | UnwindData |  |
| 392 | `SHELL32_CPL_IsLegacyCanonicalNameListedUnderKey` | `0x2DDEC0` | 18 | UnwindData |  |
| 393 | `SHELL32_CPL_ModifyWowDisplayName` | `0x2DDEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `SHELL32_CRecentDocsContextMenu_CreateInstance` | `0x2DDEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `SHELL32_CTransferConfirmation_CreateInstance` | `0x2DDF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `SHELL32_CloseAutoplayPrompt` | `0x2DDF10` | 169 | UnwindData |  |
| 399 | `SHELL32_CommandLineFromMsiDescriptor` | `0x2DDFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `SHELL32_CreateConfirmationInterrupt` | `0x2DDFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `SHELL32_CreateConflictInterrupt` | `0x2DDFF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `SHELL32_CreateDefaultOperationDataProvider` | `0x2DE000` | 210 | UnwindData |  |
| 404 | `SHELL32_CreateFileFolderContextMenu` | `0x2DE0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `SHELL32_CreateSharePointView` | `0x2DE0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `SHELL32_Create_IEnumUICommand` | `0x2DE100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `SHELL32_EncryptDirectory` | `0x2DE110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `SHELL32_EncryptedFileKeyInfo` | `0x2DE120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `SHELL32_EnumCommonTasks` | `0x2DE140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `SHELL32_FreeEncryptedFileKeyInfo` | `0x2DE150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `SHELL32_GenerateAppID` | `0x2DE170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `SHELL32_GetAppIDRoot` | `0x2DE180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `SHELL32_GetCommandProviderForFolderType` | `0x2DE190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `SHELL32_GetDiskCleanupPath` | `0x2DE1B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `SHELL32_GetFileNameFromBrowse` | `0x2DE1C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `SHELL32_GetLinkInfoData` | `0x2DE1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `SHELL32_GetRatingBucket` | `0x2DE1F0` | 30 | UnwindData |  |
| 423 | `SHELL32_GetSqmableFileName` | `0x2DE220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `SHELL32_GetThumbnailAdornerFromFactory` | `0x2DE230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `SHELL32_HandleUnrecognizedFileSystem` | `0x2DE240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `SHELL32_IconCacheCreate` | `0x2DE250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `SHELL32_IconCacheRestore` | `0x2DE260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `SHELL32_LegacyEnumSpecialTasksByType` | `0x2DE270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `SHELL32_LegacyEnumTasks` | `0x2DE280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `SHELL32_NormalizeRating` | `0x2DE290` | 53 | UnwindData |  |
| 449 | `SHELL32_Printers_CreateBindInfo` | `0x2DE2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `SHELL32_Printjob_GetPidl` | `0x2DE2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `SHELL32_PurgeSystemIcon` | `0x2DE2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | `SHELL32_RefreshOverlayImages` | `0x2DE300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `SHELL32_RegenerateUserEnvironment` | `0x2DE310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `SHELL32_SHCreateByValueOperationInterrupt` | `0x2DE320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `SHELL32_SHCreateLocalServer` | `0x2DE330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 460 | `SHELL32_SHDuplicateEncryptionInfoFile` | `0x2DE340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 461 | `SHELL32_SHEncryptFile` | `0x2DE360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `SHELL32_SHFormatDriveAsync` | `0x2DE370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `SHELL32_SHGetUserNameW` | `0x2DE380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `SHELL32_SHIsVirtualDevice` | `0x2DE3A0` | 92 | UnwindData |  |
| 466 | `SHELL32_SHLaunchPropSheet` | `0x2DE410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `SHELL32_SHLogILFromFSIL` | `0x2DE420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `SHELL32_SHOpenWithDialog` | `0x2DE440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `SHELL32_SHStartNetConnectionDialogW` | `0x2DE450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `SHStartNetConnectionDialogW` | `0x2DE450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | *Ordinal Only* | `0x2DE450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `SHELL32_ShowHideIconOnlyOnDesktop` | `0x2DE470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `SHELL32_SimpleRatingToFilterCondition` | `0x2DE480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 477 | `SHELL32_TryVirtualDiscImageDriveEject` | `0x2DE490` | 125 | UnwindData |  |
| 479 | `SHEmptyRecycleBinA` | `0x2DE8F0` | 150 | UnwindData |  |
| 480 | `SHEmptyRecycleBinW` | `0x2DE990` | 118 | UnwindData |  |
| 484 | `SHExecuteErrorMessageBox` | `0x2E03F0` | 157 | UnwindData |  |
| 149 | `SHFind_InitMenuPopup` | `0x2E0F50` | 163 | UnwindData |  |
| 811 | *Ordinal Only* | `0x2E19A0` | 444 | UnwindData |  |
| 261 | *Ordinal Only* | `0x2E1B70` | 37 | UnwindData |  |
| 810 | *Ordinal Only* | `0x2E1BA0` | 779 | UnwindData |  |
| 262 | *Ordinal Only* | `0x2E1EC0` | 1,094 | UnwindData |  |
| 497 | `SHGetDriveMedia` | `0x2E6E70` | 171 | UnwindData |  |
| 748 | *Ordinal Only* | `0x2E7660` | 84 | UnwindData |  |
| 747 | `SHLimitInputEdit` | `0x2E76C0` | 211 | UnwindData |  |
| 888 | *Ordinal Only* | `0x2E77A0` | 135 | UnwindData |  |
| 716 | `SHMultiFileProperties` | `0x2E7FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `SHOpenPropSheetW` | `0x2E7FD0` | 829 | UnwindData |  |
| 547 | `SHOpenOrGetFolderView` | `0x2E8620` | 313 | UnwindData |  |
| 944 | *Ordinal Only* | `0x2E8760` | 612 | UnwindData |  |
| 12 | *Ordinal Only* | `0x2E8BF0` | 141 | UnwindData |  |
| 271 | *Ordinal Only* | `0x2E8C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | *Ordinal Only* | `0x2E8CB0` | 12,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | *Ordinal Only* | `0x2E8CB0` | 12,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | *Ordinal Only* | `0x2EBBB0` | 660 | UnwindData |  |
| 569 | `ShellAboutA` | `0x2F95F0` | 296 | UnwindData |  |
| 570 | `ShellAboutW` | `0x2F9720` | 204 | UnwindData |  |
| 2001 | *Ordinal Only* | `0x2FA2C0` | 84 | UnwindData |  |
| 859 | *Ordinal Only* | `0x2FFCC0` | 1,732,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | *Ordinal Only* | `0x4A6B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | *Ordinal Only* | `0x4A6B10` | 181 | UnwindData |  |
| 312 | `Options_RunDLL` | `0x4ABCB0` | 79 | UnwindData |  |
| 313 | `Options_RunDLLA` | `0x4ABCB0` | 79 | UnwindData |  |
| 314 | `Options_RunDLLW` | `0x4ABD10` | 79 | UnwindData |  |
| 471 | `SHELL32_SendToMenu_InvokeTargetedCommand` | `0x4ADA60` | 171 | UnwindData |  |
| 562 | `SHShowManageLibraryUI` | `0x4F8840` | 114,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 883 | *Ordinal Only* | `0x5146B0` | 61 | UnwindData |  |
| 818 | *Ordinal Only* | `0x515120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | *Ordinal Only* | `0x515130` | 171 | UnwindData |  |
| 845 | *Ordinal Only* | `0x5157F0` | 867 | UnwindData |  |
| 816 | *Ordinal Only* | `0x515F00` | 161 | UnwindData |  |
| 817 | *Ordinal Only* | `0x5162A0` | 229 | UnwindData |  |
| 812 | *Ordinal Only* | `0x518480` | 154 | UnwindData |  |
| 813 | *Ordinal Only* | `0x518520` | 215 | UnwindData |  |
| 83 | `CIDLData_CreateFromIDArray` | `0x58F120` | 42 | UnwindData |  |
