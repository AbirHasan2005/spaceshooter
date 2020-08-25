# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCiMgLSotIGNvZGluZzogdXRmLTggLSotCgojIENvZGVkIGJ5IEBBYmlySGFzYW4yMDA1CiMgUGxlYXNlIGpvaW4gbXkgVGVsZWdyYW0gR3JvdXA6IGh0dHA6Ly90Lm1lL2xpbnV4X3JlcG8KCmZyb20gX19mdXR1cmVfXyBpbXBvcnQgZGl2aXNpb24KaW1wb3J0IHB5Z2FtZQppbXBvcnQgcmFuZG9tCmZyb20gb3MgaW1wb3J0IHBhdGgKCiMjIGFzc2V0cyBmb2xkZXIKaW1nX2RpciA9IHBhdGguam9pbihwYXRoLmRpcm5hbWUoX19maWxlX18pLCAnYXNzZXRzJykKc291bmRfZm9sZGVyID0gcGF0aC5qb2luKHBhdGguZGlybmFtZShfX2ZpbGVfXyksICdzb3VuZHMnKQoKIyMgdG8gYmUgcGxhY2VkIGluICJjb25zdGFudC5weSIgbGF0ZXIKV0lEVEggPSA0ODAKSEVJR0hUID0gNjAwCkZQUyA9IDYwClBPV0VSVVBfVElNRSA9IDUwMDAKQkFSX0xFTkdUSCA9IDEwMApCQVJfSEVJR0hUID0gMTAKCiMgRGVmaW5lIENvbG9ycyAKV0hJVEUgPSAoMjU1LCAyNTUsIDI1NSkKQkxBQ0sgPSAoMCwgMCwgMCkKUkVEID0gKDI1NSwgMCwgMCkKR1JFRU4gPSAoMCwgMjU1LCAwKQpCTFVFID0gKDAsIDAsIDI1NSkKWUVMTE9XID0gKDI1NSwgMjU1LCAwKQoKIyMgdG8gcGxhY2VkIGluICJfX2luaXRfXy5weSIgbGF0ZXIKIyMgaW5pdGlhbGl6ZSBweWdhbWUgYW5kIGNyZWF0ZSB3aW5kb3cKcHlnYW1lLmluaXQoKQpweWdhbWUubWl4ZXIuaW5pdCgpICAjIyBGb3Igc291bmQKc2NyZWVuID0gcHlnYW1lLmRpc3BsYXkuc2V0X21vZGUoKFdJRFRILCBIRUlHSFQpKQpweWdhbWUuZGlzcGxheS5zZXRfY2FwdGlvbigiU3BhY2UgU2hvb3RlciBHYW1lIGJ5IEBBYmlySGFzYW4yMDA1IikKY2xvY2sgPSBweWdhbWUudGltZS5DbG9jaygpICMjIEZvciBzeW5jaW5nIHRoZSBGUFMKCmZvbnRfbmFtZSA9IHB5Z2FtZS5mb250Lm1hdGNoX2ZvbnQoJ2FyaWFsJykKCmRlZiBtYWluX21lbnUoKToKICAgIGdsb2JhbCBzY3JlZW4KCiAgICBtZW51X3NvbmcgPSBweWdhbWUubWl4ZXIubXVzaWMubG9hZChwYXRoLmpvaW4oc291bmRfZm9sZGVyLCAibWVudS5vZ2ciKSkKICAgIHB5Z2FtZS5taXhlci5tdXNpYy5wbGF5KC0xKQoKICAgIHRpdGxlID0gcHlnYW1lLmltYWdlLmxvYWQocGF0aC5qb2luKGltZ19kaXIsICJtYWluLnBuZyIpKS5jb252ZXJ0KCkKICAgIHRpdGxlID0gcHlnYW1lLnRyYW5zZm9ybS5zY2FsZSh0aXRsZSwgKFdJRFRILCBIRUlHSFQpLCBzY3JlZW4pCgogICAgc2NyZWVuLmJsaXQodGl0bGUsICgwLDApKQogICAgcHlnYW1lLmRpc3BsYXkudXBkYXRlKCkKCiAgICB3aGlsZSBUcnVlOgogICAgICAgIGV2ID0gcHlnYW1lLmV2ZW50LnBvbGwoKQogICAgICAgIGlmIGV2LnR5cGUgPT0gcHlnYW1lLktFWURPV046CiAgICAgICAgICAgIGlmIGV2LmtleSA9PSBweWdhbWUuS19SRVRVUk46CiAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICBlbGlmIGV2LmtleSA9PSBweWdhbWUuS19xOgogICAgICAgICAgICAgICAgcHlnYW1lLnF1aXQoKQogICAgICAgICAgICAgICAgcXVpdCgpCiAgICAgICAgZWxpZiBldi50eXBlID09IHB5Z2FtZS5RVUlUOgogICAgICAgICAgICAgICAgcHlnYW1lLnF1aXQoKQogICAgICAgICAgICAgICAgcXVpdCgpIAogICAgICAgIGVsc2U6CiAgICAgICAgICAgIGRyYXdfdGV4dChzY3JlZW4sICJQcmVzcyBbRU5URVJdIFRvIEJlZ2luIiwgMzAsIFdJRFRILzIsIEhFSUdIVC8yKQogICAgICAgICAgICBkcmF3X3RleHQoc2NyZWVuLCAib3IgW1FdIFRvIFF1aXQiLCAzMCwgV0lEVEgvMiwgKEhFSUdIVC8yKSs0MCkKICAgICAgICAgICAgcHlnYW1lLmRpc3BsYXkudXBkYXRlKCkKCiAgICAjcHlnYW1lLm1peGVyLm11c2ljLnN0b3AoKQogICAgcmVhZHkgPSBweWdhbWUubWl4ZXIuU291bmQocGF0aC5qb2luKHNvdW5kX2ZvbGRlciwnZ2V0cmVhZHkub2dnJykpCiAgICByZWFkeS5wbGF5KCkKICAgIHNjcmVlbi5maWxsKEJMQUNLKQogICAgZHJhd190ZXh0KHNjcmVlbiwgIkdFVCBSRUFEWSEiLCA0MCwgV0lEVEgvMiwgSEVJR0hULzIpCiAgICBweWdhbWUuZGlzcGxheS51cGRhdGUoKQogICAgCgpkZWYgZHJhd190ZXh0KHN1cmYsIHRleHQsIHNpemUsIHgsIHkpOgogICAgIyMgc2VsZWN0aW5nIGEgY3Jvc3MgcGxhdGZvcm0gZm9udCB0byBkaXNwbGF5IHRoZSBzY29yZQogICAgZm9udCA9IHB5Z2FtZS5mb250LkZvbnQoZm9udF9uYW1lLCBzaXplKQogICAgdGV4dF9zdXJmYWNlID0gZm9udC5yZW5kZXIodGV4dCwgVHJ1ZSwgV0hJVEUpICMjIFRydWUgZGVub3RlcyB0aGUgZm9udCB0byBiZSBhbnRpLWFsaWFzZWQgCiAgICB0ZXh0X3JlY3QgPSB0ZXh0X3N1cmZhY2UuZ2V0X3JlY3QoKQogICAgdGV4dF9yZWN0Lm1pZHRvcCA9ICh4LCB5KQogICAgc3VyZi5ibGl0KHRleHRfc3VyZmFjZSwgdGV4dF9yZWN0KQoKCmRlZiBkcmF3X3NoaWVsZF9iYXIoc3VyZiwgeCwgeSwgcGN0KToKICAgICMgaWYgcGN0IDwgMDoKICAgICMgICAgIHBjdCA9IDAKICAgIHBjdCA9IG1heChwY3QsIDApIAogICAgIyMgbW92aW5nIHRoZW0gdG8gdG9wCiAgICAjIEJBUl9MRU5HVEggPSAxMDAKICAgICMgQkFSX0hFSUdIVCA9IDEwCiAgICBmaWxsID0gKHBjdCAvIDEwMCkgKiBCQVJfTEVOR1RICiAgICBvdXRsaW5lX3JlY3QgPSBweWdhbWUuUmVjdCh4LCB5LCBCQVJfTEVOR1RILCBCQVJfSEVJR0hUKQogICAgZmlsbF9yZWN0ID0gcHlnYW1lLlJlY3QoeCwgeSwgZmlsbCwgQkFSX0hFSUdIVCkKICAgIHB5Z2FtZS5kcmF3LnJlY3Qoc3VyZiwgR1JFRU4sIGZpbGxfcmVjdCkKICAgIHB5Z2FtZS5kcmF3LnJlY3Qoc3VyZiwgV0hJVEUsIG91dGxpbmVfcmVjdCwgMikKCgpkZWYgZHJhd19saXZlcyhzdXJmLCB4LCB5LCBsaXZlcywgaW1nKToKICAgIGZvciBpIGluIHJhbmdlKGxpdmVzKToKICAgICAgICBpbWdfcmVjdD0gaW1nLmdldF9yZWN0KCkKICAgICAgICBpbWdfcmVjdC54ID0geCArIDMwICogaQogICAgICAgIGltZ19yZWN0LnkgPSB5CiAgICAgICAgc3VyZi5ibGl0KGltZywgaW1nX3JlY3QpCgoKCmRlZiBuZXdtb2IoKToKICAgIG1vYl9lbGVtZW50ID0gTW9iKCkKICAgIGFsbF9zcHJpdGVzLmFkZChtb2JfZWxlbWVudCkKICAgIG1vYnMuYWRkKG1vYl9lbGVtZW50KQoKY2xhc3MgRXhwbG9zaW9uKHB5Z2FtZS5zcHJpdGUuU3ByaXRlKToKICAgIGRlZiBfX2luaXRfXyhzZWxmLCBjZW50ZXIsIHNpemUpOgogICAgICAgIHB5Z2FtZS5zcHJpdGUuU3ByaXRlLl9faW5pdF9fKHNlbGYpCiAgICAgICAgc2VsZi5zaXplID0gc2l6ZQogICAgICAgIHNlbGYuaW1hZ2UgPSBleHBsb3Npb25fYW5pbVtzZWxmLnNpemVdWzBdCiAgICAgICAgc2VsZi5yZWN0ID0gc2VsZi5pbWFnZS5nZXRfcmVjdCgpCiAgICAgICAgc2VsZi5yZWN0LmNlbnRlciA9IGNlbnRlcgogICAgICAgIHNlbGYuZnJhbWUgPSAwIAogICAgICAgIHNlbGYubGFzdF91cGRhdGUgPSBweWdhbWUudGltZS5nZXRfdGlja3MoKQogICAgICAgIHNlbGYuZnJhbWVfcmF0ZSA9IDc1CgogICAgZGVmIHVwZGF0ZShzZWxmKToKICAgICAgICBub3cgPSBweWdhbWUudGltZS5nZXRfdGlja3MoKQogICAgICAgIGlmIG5vdyAtIHNlbGYubGFzdF91cGRhdGUgPiBzZWxmLmZyYW1lX3JhdGU6CiAgICAgICAgICAgIHNlbGYubGFzdF91cGRhdGUgPSBub3cKICAgICAgICAgICAgc2VsZi5mcmFtZSArPSAxCiAgICAgICAgICAgIGlmIHNlbGYuZnJhbWUgPT0gbGVuKGV4cGxvc2lvbl9hbmltW3NlbGYuc2l6ZV0pOgogICAgICAgICAgICAgICAgc2VsZi5raWxsKCkKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIGNlbnRlciA9IHNlbGYucmVjdC5jZW50ZXIKICAgICAgICAgICAgICAgIHNlbGYuaW1hZ2UgPSBleHBsb3Npb25fYW5pbVtzZWxmLnNpemVdW3NlbGYuZnJhbWVdCiAgICAgICAgICAgICAgICBzZWxmLnJlY3QgPSBzZWxmLmltYWdlLmdldF9yZWN0KCkKICAgICAgICAgICAgICAgIHNlbGYucmVjdC5jZW50ZXIgPSBjZW50ZXIKCgpjbGFzcyBQbGF5ZXIocHlnYW1lLnNwcml0ZS5TcHJpdGUpOgogICAgZGVmIF9faW5pdF9fKHNlbGYpOgogICAgICAgIHB5Z2FtZS5zcHJpdGUuU3ByaXRlLl9faW5pdF9fKHNlbGYpCiAgICAgICAgIyMgc2NhbGUgdGhlIHBsYXllciBpbWcgZG93bgogICAgICAgIHNlbGYuaW1hZ2UgPSBweWdhbWUudHJhbnNmb3JtLnNjYWxlKHBsYXllcl9pbWcsICg1MCwgMzgpKQogICAgICAgIHNlbGYuaW1hZ2Uuc2V0X2NvbG9ya2V5KEJMQUNLKQogICAgICAgIHNlbGYucmVjdCA9IHNlbGYuaW1hZ2UuZ2V0X3JlY3QoKQogICAgICAgIHNlbGYucmFkaXVzID0gMjAKICAgICAgICBzZWxmLnJlY3QuY2VudGVyeCA9IFdJRFRIIC8gMgogICAgICAgIHNlbGYucmVjdC5ib3R0b20gPSBIRUlHSFQgLSAxMAogICAgICAgIHNlbGYuc3BlZWR4ID0gMCAKICAgICAgICBzZWxmLnNoaWVsZCA9IDEwMAogICAgICAgIHNlbGYuc2hvb3RfZGVsYXkgPSAyNTAKICAgICAgICBzZWxmLmxhc3Rfc2hvdCA9IHB5Z2FtZS50aW1lLmdldF90aWNrcygpCiAgICAgICAgc2VsZi5saXZlcyA9IDMKICAgICAgICBzZWxmLmhpZGRlbiA9IEZhbHNlCiAgICAgICAgc2VsZi5oaWRlX3RpbWVyI'
love = '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'
god = 'VjdC5yaWdodCA+IFdJRFRIICsgMjApOgogICAgICAgICAgICBzZWxmLnJlY3QueCA9IHJhbmRvbS5yYW5kcmFuZ2UoMCwgV0lEVEggLSBzZWxmLnJlY3Qud2lkdGgpCiAgICAgICAgICAgIHNlbGYucmVjdC55ID0gcmFuZG9tLnJhbmRyYW5nZSgtMTAwLCAtNDApCiAgICAgICAgICAgIHNlbGYuc3BlZWR5ID0gcmFuZG9tLnJhbmRyYW5nZSgxLCA4KSAjIyBmb3IgcmFuZG9taXppbmcgdGhlIHNwZWVkIG9mIHRoZSBNb2IKCiMjIGRlZmluZXMgdGhlIHNwcml0ZSBmb3IgUG93ZXJ1cHMKY2xhc3MgUG93KHB5Z2FtZS5zcHJpdGUuU3ByaXRlKToKICAgIGRlZiBfX2luaXRfXyhzZWxmLCBjZW50ZXIpOgogICAgICAgIHB5Z2FtZS5zcHJpdGUuU3ByaXRlLl9faW5pdF9fKHNlbGYpCiAgICAgICAgc2VsZi50eXBlID0gcmFuZG9tLmNob2ljZShbJ3NoaWVsZCcsICdndW4nXSkKICAgICAgICBzZWxmLmltYWdlID0gcG93ZXJ1cF9pbWFnZXNbc2VsZi50eXBlXQogICAgICAgIHNlbGYuaW1hZ2Uuc2V0X2NvbG9ya2V5KEJMQUNLKQogICAgICAgIHNlbGYucmVjdCA9IHNlbGYuaW1hZ2UuZ2V0X3JlY3QoKQogICAgICAgICMjIHBsYWNlIHRoZSBidWxsZXQgYWNjb3JkaW5nIHRvIHRoZSBjdXJyZW50IHBvc2l0aW9uIG9mIHRoZSBwbGF5ZXIKICAgICAgICBzZWxmLnJlY3QuY2VudGVyID0gY2VudGVyCiAgICAgICAgc2VsZi5zcGVlZHkgPSAyCgogICAgZGVmIHVwZGF0ZShzZWxmKToKICAgICAgICAjIHNob3VsZCBzcGF3biByaWdodCBpbiBmcm9udCBvZiB0aGUgcGxheWVyCiAgICAgICAgc2VsZi5yZWN0LnkgKz0gc2VsZi5zcGVlZHkKICAgICAgICAjIyBraWxsIHRoZSBzcHJpdGUgYWZ0ZXIgaXQgbW92ZXMgb3ZlciB0aGUgdG9wIGJvcmRlcgogICAgICAgIGlmIHNlbGYucmVjdC50b3AgPiBIRUlHSFQ6CiAgICAgICAgICAgIHNlbGYua2lsbCgpCgogICAgICAgICAgICAKCiMjIGRlZmluZXMgdGhlIHNwcml0ZSBmb3IgYnVsbGV0cwpjbGFzcyBCdWxsZXQocHlnYW1lLnNwcml0ZS5TcHJpdGUpOgogICAgZGVmIF9faW5pdF9fKHNlbGYsIHgsIHkpOgogICAgICAgIHB5Z2FtZS5zcHJpdGUuU3ByaXRlLl9faW5pdF9fKHNlbGYpCiAgICAgICAgc2VsZi5pbWFnZSA9IGJ1bGxldF9pbWcKICAgICAgICBzZWxmLmltYWdlLnNldF9jb2xvcmtleShCTEFDSykKICAgICAgICBzZWxmLnJlY3QgPSBzZWxmLmltYWdlLmdldF9yZWN0KCkKICAgICAgICAjIyBwbGFjZSB0aGUgYnVsbGV0IGFjY29yZGluZyB0byB0aGUgY3VycmVudCBwb3NpdGlvbiBvZiB0aGUgcGxheWVyCiAgICAgICAgc2VsZi5yZWN0LmJvdHRvbSA9IHkgCiAgICAgICAgc2VsZi5yZWN0LmNlbnRlcnggPSB4CiAgICAgICAgc2VsZi5zcGVlZHkgPSAtMTAKCiAgICBkZWYgdXBkYXRlKHNlbGYpOgogICAgICAgICMgc2hvdWxkIHNwYXduIHJpZ2h0IGluIGZyb250IG9mIHRoZSBwbGF5ZXIKICAgICAgICBzZWxmLnJlY3QueSArPSBzZWxmLnNwZWVkeQogICAgICAgICMjIGtpbGwgdGhlIHNwcml0ZSBhZnRlciBpdCBtb3ZlcyBvdmVyIHRoZSB0b3AgYm9yZGVyCiAgICAgICAgaWYgc2VsZi5yZWN0LmJvdHRvbSA8IDA6CiAgICAgICAgICAgIHNlbGYua2lsbCgpCgogICAgICAgICMjIG5vdyB3ZSBuZWVkIGEgd2F5IHRvIHNob290CiAgICAgICAgIyMgbGV0cyBiaW5kIGl0IHRvICJzcGFjZWJhciIuCiAgICAgICAgIyMgYWRkaW5nIGFuIGV2ZW50IGZvciBpdCBpbiBHYW1lIGxvb3AKCiMjIEZJUkUgWkUgTUlTU0lMRVMKY2xhc3MgTWlzc2lsZShweWdhbWUuc3ByaXRlLlNwcml0ZSk6CiAgICBkZWYgX19pbml0X18oc2VsZiwgeCwgeSk6CiAgICAgICAgcHlnYW1lLnNwcml0ZS5TcHJpdGUuX19pbml0X18oc2VsZikKICAgICAgICBzZWxmLmltYWdlID0gbWlzc2lsZV9pbWcKICAgICAgICBzZWxmLmltYWdlLnNldF9jb2xvcmtleShCTEFDSykKICAgICAgICBzZWxmLnJlY3QgPSBzZWxmLmltYWdlLmdldF9yZWN0KCkKICAgICAgICBzZWxmLnJlY3QuYm90dG9tID0geQogICAgICAgIHNlbGYucmVjdC5jZW50ZXJ4ID0geAogICAgICAgIHNlbGYuc3BlZWR5ID0gLTEwCgogICAgZGVmIHVwZGF0ZShzZWxmKToKICAgICAgICAjIHNob3VsZCBzcGF3biByaWdodCBpbiBmcm9udCBvZiB0aGUgcGxheWVyCiAgICAgICAgc2VsZi5yZWN0LnkgKz0gc2VsZi5zcGVlZHkKICAgICAgICBpZiBzZWxmLnJlY3QuYm90dG9tIDwgMDoKICAgICAgICAgICAgc2VsZi5raWxsKCkKCgojIyBMb2FkIGFsbCBnYW1lIGltYWdlcwoKYmFja2dyb3VuZCA9IHB5Z2FtZS5pbWFnZS5sb2FkKHBhdGguam9pbihpbWdfZGlyLCAnc3RhcmZpZWxkLnBuZycpKS5jb252ZXJ0KCkKYmFja2dyb3VuZF9yZWN0ID0gYmFja2dyb3VuZC5nZXRfcmVjdCgpCgpwbGF5ZXJfaW1nID0gcHlnYW1lLmltYWdlLmxvYWQocGF0aC5qb2luKGltZ19kaXIsICdwbGF5ZXJTaGlwMV9vcmFuZ2UucG5nJykpLmNvbnZlcnQoKQpwbGF5ZXJfbWluaV9pbWcgPSBweWdhbWUudHJhbnNmb3JtLnNjYWxlKHBsYXllcl9pbWcsICgyNSwgMTkpKQpwbGF5ZXJfbWluaV9pbWcuc2V0X2NvbG9ya2V5KEJMQUNLKQpidWxsZXRfaW1nID0gcHlnYW1lLmltYWdlLmxvYWQocGF0aC5qb2luKGltZ19kaXIsICdsYXNlclJlZDE2LnBuZycpKS5jb252ZXJ0KCkKbWlzc2lsZV9pbWcgPSBweWdhbWUuaW1hZ2UubG9hZChwYXRoLmpvaW4oaW1nX2RpciwgJ21pc3NpbGUucG5nJykpLmNvbnZlcnRfYWxwaGEoKQojIG1ldGVvcl9pbWcgPSBweWdhbWUuaW1hZ2UubG9hZChwYXRoLmpvaW4oaW1nX2RpciwgJ21ldGVvckJyb3duX21lZDEucG5nJykpLmNvbnZlcnQoKQptZXRlb3JfaW1hZ2VzID0gW10KbWV0ZW9yX2xpc3QgPSBbCiAgICAnbWV0ZW9yQnJvd25fYmlnMS5wbmcnLAogICAgJ21ldGVvckJyb3duX2JpZzIucG5nJywgCiAgICAnbWV0ZW9yQnJvd25fbWVkMS5wbmcnLCAKICAgICdtZXRlb3JCcm93bl9tZWQzLnBuZycsCiAgICAnbWV0ZW9yQnJvd25fc21hbGwxLnBuZycsCiAgICAnbWV0ZW9yQnJvd25fc21hbGwyLnBuZycsCiAgICAnbWV0ZW9yQnJvd25fdGlueTEucG5nJwpdCgpmb3IgaW1hZ2UgaW4gbWV0ZW9yX2xpc3Q6CiAgICBtZXRlb3JfaW1hZ2VzLmFwcGVuZChweWdhbWUuaW1hZ2UubG9hZChwYXRoLmpvaW4oaW1nX2RpciwgaW1hZ2UpKS5jb252ZXJ0KCkpCgojIyBtZXRlb3IgZXhwbG9zaW9uCmV4cGxvc2lvbl9hbmltID0ge30KZXhwbG9zaW9uX2FuaW1bJ2xnJ10gPSBbXQpleHBsb3Npb25fYW5pbVsnc20nXSA9IFtdCmV4cGxvc2lvbl9hbmltWydwbGF5ZXInXSA9IFtdCmZvciBpIGluIHJhbmdlKDkpOgogICAgZmlsZW5hbWUgPSAncmVndWxhckV4cGxvc2lvbjB7fS5wbmcnLmZvcm1hdChpKQogICAgaW1nID0gcHlnYW1lLmltYWdlLmxvYWQocGF0aC5qb2luKGltZ19kaXIsIGZpbGVuYW1lKSkuY29udmVydCgpCiAgICBpbWcuc2V0X2NvbG9ya2V5KEJMQUNLKQogICAgIyMgcmVzaXplIHRoZSBleHBsb3Npb24KICAgIGltZ19sZyA9IHB5Z2FtZS50cmFuc2Zvcm0uc2NhbGUoaW1nLCAoNzUsIDc1KSkKICAgIGV4cGxvc2lvbl9hbmltWydsZyddLmFwcGVuZChpbWdfbGcpCiAgICBpbWdfc20gPSBweWdhbWUudHJhbnNmb3JtLnNjYWxlKGltZywgKDMyLCAzMikpCiAgICBleHBsb3Npb25fYW5pbVsnc20nXS5hcHBlbmQoaW1nX3NtKQoKICAgICMjIHBsYXllciBleHBsb3Npb24KICAgIGZpbGVuYW1lID0gJ3NvbmljRXhwbG9zaW9uMHt9LnBuZycuZm9ybWF0KGkpCiAgICBpbWcgPSBweWdhbWUuaW1hZ2UubG9hZChwYXRoLmpvaW4oaW1nX2RpciwgZmlsZW5hbWUpKS5jb252ZXJ0KCkKICAgIGltZy5zZXRfY29sb3JrZXkoQkxBQ0spCiAgICBleHBsb3Npb25fYW5pbVsncGxheWVyJ10uYXBwZW5kKGltZykKCiMjIGxvYWQgcG93ZXIgdXBzCnBvd2VydXBfaW1hZ2VzID0ge30KcG93ZXJ1cF9pbWFnZXNbJ3NoaWVsZCddID0gcHlnYW1lLmltYWdlLmxvYWQocGF0aC5qb2luKGltZ19kaXIsICdzaGllbGRfZ29sZC5wbmcnKSkuY29udmVydCgpCnBvd2VydXBfaW1hZ2VzWydndW4nXSA9IHB5Z2FtZS5pbWFnZS5sb2FkKHBhdGguam9pbihpbWdfZGlyLCAnYm9sdF9nb2xkLnBuZycpKS5jb252ZXJ0KCkKCgojIyMgTG9hZCBhbGwgZ2FtZSBzb3VuZHMKc2hvb3Rpbmdfc291bmQgPSBweWdhbWUubWl4ZXIuU291bmQocGF0aC5qb2luKHNvdW5kX2ZvbGRlciwgJ3Bldy53YXYnKSkKbWlzc2lsZV9zb3VuZCA9IHB5Z2FtZS5taXhlci5Tb3VuZChwYXRoLmpvaW4oc291bmRfZm9sZGVyLCAncm9ja2V0Lm9nZycpKQpleHBsX3NvdW5kcyA9IFtdCmZvciBzb3VuZCBpbiBbJ2V4cGwzLndhdicsICdleHBsNi53YXYnXToKICAgIGV4cGxfc291bmRzLmFwcGVuZChweWdhbWUubWl4ZXIuU291bmQocGF0aC5qb2luKHNvdW5kX2ZvbGRlciwgc291bmQpKSkKCiMjIG1haW4gYmFja2dyb3VuZCBtdXNpYwojcHlnYW1lLm1peGVyLm11c2ljLmxvYWQocGF0aC5qb2luKHNvdW5kX2ZvbGRlciwgJ3RnZmNvZGVyLUZyb3plbkphbS1TZWFtbGVzc0xvb3Aub2dnJykpCnB5Z2FtZS5taXhlci5tdXNpYy5zZXRfdm9sdW1lKDAuMikgICAgICAjIyBzaW1tZXJlZCB0aGUgc291bmQgZG93biBhIGxpdHRsZQoKcGxheWV'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))