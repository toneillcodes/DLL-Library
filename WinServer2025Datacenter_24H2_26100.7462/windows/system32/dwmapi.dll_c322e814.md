# Binary Specification: dwmapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dwmapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c322e81433047cb334eff32a112d72b91a3e3739b4e24d69f456908db6c2d42a`
* **Total Exported Functions:** 112

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 136 | `DwmpAllocateSecurityDescriptor` | `0x1170` | 493 | UnwindData |  |
| 204 | `DwmSetIconicThumbnail` | `0x14C0` | 953 | UnwindData |  |
| 163 | *Ordinal Only* | `0x1880` | 484 | UnwindData |  |
| 131 | `DwmpSetColorizationParameters` | `0x1CB0` | 402 | UnwindData |  |
| 159 | *Ordinal Only* | `0x2010` | 161 | UnwindData |  |
| 114 | *Ordinal Only* | `0x20C0` | 209 | UnwindData |  |
| 123 | `DwmGetColorizationColor` | `0x2410` | 197 | UnwindData |  |
| 146 | `DwmInvalidateIconicBitmaps` | `0x24E0` | 235 | UnwindData |  |
| 211 | `DwmUpdateThumbnailProperties` | `0x2600` | 402 | UnwindData |  |
| 149 | `DwmIsCompositionEnabled` | `0x27A0` | 211 | UnwindData |  |
| 125 | `DwmGetCompositionTimingInfo` | `0x28F0` | 17 | UnwindData |  |
| 132 | *Ordinal Only* | `0x2970` | 833 | UnwindData |  |
| 147 | *Ordinal Only* | `0x2CD0` | 779 | UnwindData |  |
| 127 | `DwmpGetColorizationParameters` | `0x2FF0` | 200 | UnwindData |  |
| 169 | *Ordinal Only* | `0x30C0` | 1,117 | UnwindData |  |
| 207 | `DwmShowContact` | `0x3680` | 213 | UnwindData |  |
| 210 | `DwmUnregisterThumbnail` | `0x3760` | 256 | UnwindData |  |
| 121 | `DwmExtendFrameIntoClientArea` | `0x3A30` | 613 | UnwindData |  |
| 162 | *Ordinal Only* | `0x3CA0` | 183 | UnwindData |  |
| 117 | `DwmDefWindowProc` | `0x3F30` | 119 | UnwindData |  |
| 100 | `DwmpDxGetWindowSharedSurface` | `0x4200` | 1,861 | UnwindData |  |
| 122 | `DwmFlush` | `0x5480` | 271 | UnwindData |  |
| 206 | `DwmSetWindowAttribute` | `0x5F50` | 84 | UnwindData |  |
| 134 | `DwmGetWindowAttribute` | `0x63B0` | 90 | UnwindData |  |
| 170 | *Ordinal Only* | `0x7AC0` | 398 | UnwindData |  |
| 179 | *Ordinal Only* | `0x7C80` | 447 | UnwindData |  |
| 128 | `DwmpDxgiIsThreadDesktopComposited` | `0x8B80` | 59 | UnwindData |  |
| 186 | *Ordinal Only* | `0x9750` | 1,124 | UnwindData |  |
| 199 | `DwmQueryThumbnailSourceSize` | `0x9FC0` | 323 | UnwindData |  |
| 113 | *Ordinal Only* | `0xA160` | 48 | UnwindData |  |
| 187 | *Ordinal Only* | `0xA1A0` | 770 | UnwindData |  |
| 139 | *Ordinal Only* | `0xA510` | 38 | UnwindData |  |
| 141 | *Ordinal Only* | `0xA540` | 210 | UnwindData |  |
| 198 | `DwmModifyPreviousDxFrameDuration` | `0xA760` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `DwmSetDxFrameDuration` | `0xA760` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `DwmSetPresentParameters` | `0xA760` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | *Ordinal Only* | `0xA760` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | *Ordinal Only* | `0xA760` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `DwmEnableBlurBehindWindow` | `0xA7B0` | 908 | UnwindData |  |
| 185 | *Ordinal Only* | `0xAD30` | 120 | UnwindData |  |
| 140 | *Ordinal Only* | `0xADD0` | 146 | UnwindData |  |
| 148 | *Ordinal Only* | `0xAE90` | 268 | UnwindData |  |
| 138 | *Ordinal Only* | `0xB080` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `DwmRegisterThumbnail` | `0xB0D0` | 192 | UnwindData |  |
| 124 | *Ordinal Only* | `0xB1A0` | 320 | UnwindData |  |
| 120 | `DwmEnableMMCSS` | `0xB2F0` | 165 | UnwindData |  |
| 161 | *Ordinal Only* | `0xB450` | 188 | UnwindData |  |
| 145 | *Ordinal Only* | `0xB6C0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | *Ordinal Only* | `0xB830` | 117 | UnwindData |  |
| 183 | `DwmpUpdateProxyWindowForCapture` | `0xB8B0` | 121 | UnwindData |  |
| 137 | `DwmpFreeSecurityDescriptor` | `0xB9B0` | 46 | UnwindData |  |
| 174 | *Ordinal Only* | `0xBA30` | 97 | UnwindData |  |
| 173 | *Ordinal Only* | `0xBAA0` | 97 | UnwindData |  |
| 180 | *Ordinal Only* | `0xBB10` | 131 | UnwindData |  |
| 164 | *Ordinal Only* | `0xBBA0` | 545 | UnwindData |  |
| 102 | `DwmEnableComposition` | `0xC450` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `DwmTetherTextContact` | `0xC450` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `DwmpDxUpdateWindowSharedSurface` | `0xC450` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `DwmpEnableDDASupport` | `0xC450` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | *Ordinal Only* | `0xC450` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | *Ordinal Only* | `0xC450` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `DwmAttachMilContent` | `0xC780` | 21,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `DwmDetachMilContent` | `0xC780` | 21,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `DwmGetGraphicsStreamClient` | `0xC780` | 21,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `DwmGetGraphicsStreamTransformHint` | `0xC780` | 21,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | *Ordinal Only* | `0xC780` | 21,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | *Ordinal Only* | `0xC780` | 21,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | *Ordinal Only* | `0xC780` | 21,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | *Ordinal Only* | `0x119A0` | 119 | UnwindData |  |
| 150 | *Ordinal Only* | `0x11A20` | 119 | UnwindData |  |
| 152 | *Ordinal Only* | `0x11AA0` | 116 | UnwindData |  |
| 153 | *Ordinal Only* | `0x11B20` | 172 | UnwindData |  |
| 155 | *Ordinal Only* | `0x11BE0` | 166 | UnwindData |  |
| 178 | *Ordinal Only* | `0x11C90` | 170 | UnwindData |  |
| 154 | *Ordinal Only* | `0x11D40` | 151 | UnwindData |  |
| 107 | *Ordinal Only* | `0x11DE0` | 281 | UnwindData |  |
| 192 | *Ordinal Only* | `0x149D0` | 124 | UnwindData |  |
| 190 | *Ordinal Only* | `0x14A60` | 97 | UnwindData |  |
| 181 | *Ordinal Only* | `0x14AD0` | 97 | UnwindData |  |
| 194 | *Ordinal Only* | `0x14B40` | 462 | UnwindData |  |
| 189 | *Ordinal Only* | `0x14D20` | 102 | UnwindData |  |
| 106 | *Ordinal Only* | `0x14D90` | 158 | UnwindData |  |
| 197 | *Ordinal Only* | `0x14E40` | 197 | UnwindData |  |
| 157 | *Ordinal Only* | `0x14F10` | 76 | UnwindData |  |
| 195 | *Ordinal Only* | `0x14F70` | 187 | UnwindData |  |
| 171 | *Ordinal Only* | `0x15040` | 124 | UnwindData |  |
| 191 | *Ordinal Only* | `0x150D0` | 117 | UnwindData |  |
| 182 | *Ordinal Only* | `0x15150` | 117 | UnwindData |  |
| 176 | *Ordinal Only* | `0x151D0` | 117 | UnwindData |  |
| 158 | *Ordinal Only* | `0x15250` | 162 | UnwindData |  |
| 196 | *Ordinal Only* | `0x15300` | 198 | UnwindData |  |
| 193 | *Ordinal Only* | `0x153D0` | 120 | UnwindData |  |
| 175 | *Ordinal Only* | `0x15450` | 121 | UnwindData |  |
| 184 | *Ordinal Only* | `0x154D0` | 120 | UnwindData |  |
| 167 | *Ordinal Only* | `0x15B90` | 213 | UnwindData |  |
| 165 | *Ordinal Only* | `0x15C70` | 61 | UnwindData |  |
| 201 | `DwmRenderGesture` | `0x15D40` | 518 | UnwindData |  |
| 208 | `DwmTetherContact` | `0x15F50` | 266 | UnwindData |  |
| 135 | `DwmpRenderFlick` | `0x16060` | 283 | UnwindData |  |
| 130 | `DwmGetTransportAttributes` | `0x16190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `DwmGetUnmetTabRequirements` | `0x161B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | *Ordinal Only* | `0x161C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `DwmSetIconicLivePreviewBitmap` | `0x161E0` | 788 | UnwindData |  |
| 166 | *Ordinal Only* | `0x16500` | 568 | UnwindData |  |
| 160 | *Ordinal Only* | `0x16740` | 1,581 | UnwindData |  |
| 142 | *Ordinal Only* | `0x16D80` | 158 | UnwindData |  |
| 209 | `DwmTransitionOwnedWindow` | `0x16F10` | 211 | UnwindData |  |
| 144 | *Ordinal Only* | `0x16FF0` | 864 | UnwindData |  |
| 188 | *Ordinal Only* | `0x17440` | 130 | UnwindData |  |
| 168 | *Ordinal Only* | `0x177F0` | 252 | UnwindData |  |
| 111 | `DllCanUnloadNow` | `0x185D0` | 42 | UnwindData |  |
| 115 | `DllGetClassObject` | `0x18600` | 65 | UnwindData |  |
