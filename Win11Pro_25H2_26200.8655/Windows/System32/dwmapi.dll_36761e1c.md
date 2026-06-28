# Binary Specification: dwmapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dwmapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `36761e1c4f2dcd587e216471b808e7a928090de4f7a9c9a1d25e0ee85698aceb`
* **Total Exported Functions:** 113

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 170 | *Ordinal Only* | `0x1090` | 398 | UnwindData |  |
| 205 | `DwmSetIconicThumbnail` | `0x12E0` | 957 | UnwindData |  |
| 136 | `DwmpAllocateSecurityDescriptor` | `0x17A0` | 493 | UnwindData |  |
| 131 | `DwmpSetColorizationParameters` | `0x1C20` | 402 | UnwindData |  |
| 159 | *Ordinal Only* | `0x1F80` | 161 | UnwindData |  |
| 149 | `DwmIsCompositionEnabled` | `0x2030` | 211 | UnwindData |  |
| 125 | `DwmGetCompositionTimingInfo` | `0x2180` | 17 | UnwindData |  |
| 132 | *Ordinal Only* | `0x2200` | 833 | UnwindData |  |
| 208 | `DwmShowContact` | `0x2560` | 213 | UnwindData |  |
| 211 | `DwmUnregisterThumbnail` | `0x2640` | 256 | UnwindData |  |
| 121 | `DwmExtendFrameIntoClientArea` | `0x2910` | 613 | UnwindData |  |
| 162 | *Ordinal Only* | `0x2B80` | 183 | UnwindData |  |
| 117 | `DwmDefWindowProc` | `0x2E10` | 119 | UnwindData |  |
| 100 | `DwmpDxGetWindowSharedSurface` | `0x30E0` | 1,861 | UnwindData |  |
| 122 | `DwmFlush` | `0x4360` | 271 | UnwindData |  |
| 207 | `DwmSetWindowAttribute` | `0x4E20` | 84 | UnwindData |  |
| 134 | `DwmGetWindowAttribute` | `0x5280` | 90 | UnwindData |  |
| 127 | `DwmpGetColorizationParameters` | `0x57E0` | 200 | UnwindData |  |
| 169 | *Ordinal Only* | `0x58B0` | 1,117 | UnwindData |  |
| 147 | *Ordinal Only* | `0x5E30` | 779 | UnwindData |  |
| 123 | `DwmGetColorizationColor` | `0x71F0` | 197 | UnwindData |  |
| 212 | `DwmUpdateThumbnailProperties` | `0x7560` | 402 | UnwindData |  |
| 163 | *Ordinal Only* | `0x7740` | 484 | UnwindData |  |
| 146 | `DwmInvalidateIconicBitmaps` | `0x7930` | 235 | UnwindData |  |
| 128 | `DwmpDxgiIsThreadDesktopComposited` | `0x8640` | 59 | UnwindData |  |
| 186 | *Ordinal Only* | `0x90C0` | 1,124 | UnwindData |  |
| 200 | `DwmQueryThumbnailSourceSize` | `0x9670` | 323 | UnwindData |  |
| 114 | *Ordinal Only* | `0x97C0` | 209 | UnwindData |  |
| 113 | *Ordinal Only* | `0x9AA0` | 48 | UnwindData |  |
| 187 | *Ordinal Only* | `0x9AE0` | 770 | UnwindData |  |
| 139 | *Ordinal Only* | `0x9E50` | 38 | UnwindData |  |
| 141 | *Ordinal Only* | `0x9E80` | 210 | UnwindData |  |
| 179 | *Ordinal Only* | `0x9F60` | 447 | UnwindData |  |
| 199 | `DwmModifyPreviousDxFrameDuration` | `0xA310` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `DwmSetDxFrameDuration` | `0xA310` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `DwmSetPresentParameters` | `0xA310` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | *Ordinal Only* | `0xA310` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | *Ordinal Only* | `0xA310` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | *Ordinal Only* | `0xA310` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `DwmEnableBlurBehindWindow` | `0xA3B0` | 943 | UnwindData |  |
| 185 | *Ordinal Only* | `0xA900` | 120 | UnwindData |  |
| 140 | *Ordinal Only* | `0xA9A0` | 146 | UnwindData |  |
| 148 | *Ordinal Only* | `0xAC50` | 268 | UnwindData |  |
| 138 | *Ordinal Only* | `0xAE20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `DwmRegisterThumbnail` | `0xAE70` | 192 | UnwindData |  |
| 124 | *Ordinal Only* | `0xAF40` | 320 | UnwindData |  |
| 120 | `DwmEnableMMCSS` | `0xB090` | 165 | UnwindData |  |
| 161 | *Ordinal Only* | `0xB1F0` | 188 | UnwindData |  |
| 145 | *Ordinal Only* | `0xB460` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | *Ordinal Only* | `0xB5C0` | 117 | UnwindData |  |
| 183 | `DwmpUpdateProxyWindowForCapture` | `0xB640` | 121 | UnwindData |  |
| 137 | `DwmpFreeSecurityDescriptor` | `0xB6C0` | 46 | UnwindData |  |
| 174 | *Ordinal Only* | `0xB840` | 97 | UnwindData |  |
| 173 | *Ordinal Only* | `0xB8B0` | 97 | UnwindData |  |
| 180 | *Ordinal Only* | `0xB920` | 131 | UnwindData |  |
| 164 | *Ordinal Only* | `0xB9B0` | 557 | UnwindData |  |
| 102 | `DwmEnableComposition` | `0xC050` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `DwmTetherTextContact` | `0xC050` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `DwmpDxUpdateWindowSharedSurface` | `0xC050` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `DwmpEnableDDASupport` | `0xC050` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | *Ordinal Only* | `0xC050` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | *Ordinal Only* | `0xC050` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `DwmAttachMilContent` | `0xC380` | 21,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `DwmDetachMilContent` | `0xC380` | 21,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `DwmGetGraphicsStreamClient` | `0xC380` | 21,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `DwmGetGraphicsStreamTransformHint` | `0xC380` | 21,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | *Ordinal Only* | `0xC380` | 21,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | *Ordinal Only* | `0xC380` | 21,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | *Ordinal Only* | `0xC380` | 21,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | *Ordinal Only* | `0x11680` | 119 | UnwindData |  |
| 150 | *Ordinal Only* | `0x11700` | 119 | UnwindData |  |
| 152 | *Ordinal Only* | `0x11780` | 116 | UnwindData |  |
| 153 | *Ordinal Only* | `0x11800` | 172 | UnwindData |  |
| 155 | *Ordinal Only* | `0x118C0` | 166 | UnwindData |  |
| 178 | *Ordinal Only* | `0x11970` | 170 | UnwindData |  |
| 154 | *Ordinal Only* | `0x11A20` | 151 | UnwindData |  |
| 107 | *Ordinal Only* | `0x11AC0` | 281 | UnwindData |  |
| 192 | *Ordinal Only* | `0x137B0` | 124 | UnwindData |  |
| 190 | *Ordinal Only* | `0x13840` | 97 | UnwindData |  |
| 181 | *Ordinal Only* | `0x138B0` | 97 | UnwindData |  |
| 194 | *Ordinal Only* | `0x13920` | 462 | UnwindData |  |
| 189 | *Ordinal Only* | `0x13B00` | 102 | UnwindData |  |
| 106 | *Ordinal Only* | `0x13B70` | 158 | UnwindData |  |
| 197 | *Ordinal Only* | `0x13C20` | 197 | UnwindData |  |
| 157 | *Ordinal Only* | `0x13CF0` | 76 | UnwindData |  |
| 195 | *Ordinal Only* | `0x13D50` | 187 | UnwindData |  |
| 171 | *Ordinal Only* | `0x13E20` | 124 | UnwindData |  |
| 191 | *Ordinal Only* | `0x13EB0` | 117 | UnwindData |  |
| 182 | *Ordinal Only* | `0x13F30` | 117 | UnwindData |  |
| 176 | *Ordinal Only* | `0x13FB0` | 117 | UnwindData |  |
| 158 | *Ordinal Only* | `0x14030` | 162 | UnwindData |  |
| 196 | *Ordinal Only* | `0x140E0` | 198 | UnwindData |  |
| 193 | *Ordinal Only* | `0x141B0` | 120 | UnwindData |  |
| 175 | *Ordinal Only* | `0x14230` | 199 | UnwindData |  |
| 184 | *Ordinal Only* | `0x14300` | 120 | UnwindData |  |
| 167 | *Ordinal Only* | `0x149C0` | 213 | UnwindData |  |
| 165 | *Ordinal Only* | `0x14AA0` | 61 | UnwindData |  |
| 202 | `DwmRenderGesture` | `0x14B70` | 518 | UnwindData |  |
| 209 | `DwmTetherContact` | `0x14D80` | 266 | UnwindData |  |
| 135 | `DwmpRenderFlick` | `0x14E90` | 283 | UnwindData |  |
| 130 | `DwmGetTransportAttributes` | `0x14FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `DwmGetUnmetTabRequirements` | `0x14FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | *Ordinal Only* | `0x14FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `DwmSetIconicLivePreviewBitmap` | `0x15010` | 791 | UnwindData |  |
| 166 | *Ordinal Only* | `0x15330` | 568 | UnwindData |  |
| 160 | *Ordinal Only* | `0x15570` | 1,577 | UnwindData |  |
| 142 | *Ordinal Only* | `0x15BA0` | 158 | UnwindData |  |
| 210 | `DwmTransitionOwnedWindow` | `0x15D30` | 211 | UnwindData |  |
| 144 | *Ordinal Only* | `0x15E10` | 871 | UnwindData |  |
| 188 | *Ordinal Only* | `0x16260` | 130 | UnwindData |  |
| 168 | *Ordinal Only* | `0x16610` | 252 | UnwindData |  |
| 111 | `DllCanUnloadNow` | `0x17070` | 42 | UnwindData |  |
| 115 | `DllGetClassObject` | `0x170A0` | 65 | UnwindData |  |
