# Visual Grammar Foundry

[English](README.md) · [简体中文](README.zh-CN.md)

面向独立 `style-skill` 子项目的公共互操作契约。

## 仓库分层

本仓库与私有生产系统分离：

```text
私有仓库：visual-grammar-foundry-core
公共仓库：visual-grammar-foundry
子项目仓库：visual-grammar-<slug>
```

公共仓库定义子项目包的结构，并提供可复用的子项目模板。它**不包含**父级编排流水线、私有协议、源素材清单、来源记录、研究笔记或运行产物。私有核心负责生成和验证子项目；每个已发布子项目都会被导出到独立仓库。

## 公共契约

当前公共包契约为 `contract_version: 1`。一个已发布的子项目必须是独立可运行的，并至少包含：

- 作为公共入口的 `SKILL.md`；
- `README.md`、`CHANGELOG.md`、`LICENSE`、`ASSET-LICENSE.md` 和 `REFERENCES.md`；
- 包含 SemVer 和公共边界声明的 `release.json`；
- 公共 `design-system/` catalog 和 `evals/` 契约文件；
- 至少三个原创演示；
- `scripts/validate_public.py` 及其独立 CI 工作流。

兼容规则见 [`docs/CONTRACT.md`](docs/CONTRACT.md)，子项目脚手架见 [`templates/public-child/`](templates/public-child/)。

## 验证

验证公共契约仓库本身：

```bash
python3 scripts/validate_contract.py
```

生成并发布的子项目应在自身目录中运行独立验证器：

```bash
python3 scripts/validate_public.py
```

## 命名

- 内部项目：**Visual Grammar Foundry**
- 私有核心仓库：`visual-grammar-foundry-core`
- 公共契约仓库：`visual-grammar-foundry`
- 公共子项目仓库：`visual-grammar-<slug>`

## 许可证

公共契约仓库采用 MIT License。你可以按照 [`LICENSE`](LICENSE) 中的版权声明和免责声明，使用、复制、修改、分发、再许可和销售本仓库中的原创 schemas、模板、校验器和文档。

MIT 不代表你可以访问 `visual-grammar-foundry-core`、私有运行产物、未公开的方法或第三方内容。子项目有自己的许可证和权利记录；子项目中的 MIT 只覆盖其创建者有权许可的原创内容。源素材、字体、商标、logo、用户提供的文字和其他第三方内容仍受各自条款约束。使用 MIT 覆盖的仓库代码进行商业活动通常不需要额外付费或授权，但仍必须审查所有第三方权利和具体子项目许可证。

## 权利与原创性

本契约不授予复制源素材的权利。子项目不得重新分发未经验证的源素材、复制的文字、logo、签名、独特字形、精确布局或来源特有的元数据。署名不等于许可；每次发布都必须自行负责许可证、权利记录和人工原创性审查。
