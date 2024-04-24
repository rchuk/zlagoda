import {Breadcrumbs, Button} from "@mui/material";
import {ReactElement, useEffect, useState} from "react";
import {useRouter} from "next/router";


type BreadcrumbItemSegment = {
  title: string,
  icon?: () => ReactElement,
  path: string
}

export interface BreadcrumbItem {
  title: string,
  icon?: () => ReactElement
}

export type BreadcrumbServiceHandle = {
  push: (item: BreadcrumbItem) => void,
  replace: (item: BreadcrumbItem) => void,
  modify: (item: BreadcrumbItem) => void
};

export interface BreadcrumbMap extends BreadcrumbItem {
  children?: Record<string, BreadcrumbMap>
}

type BreadcrumbsComponentProps = {
  segmentMap: BreadcrumbMap,
  setHandle?: (value: BreadcrumbServiceHandle) => void
};

export default function BreadcrumbsComponent(props: BreadcrumbsComponentProps) {
  const [items, setItems] = useState<BreadcrumbItemSegment[]>([]);
  const router = useRouter();

  function createItemSegment(item: BreadcrumbItem, path: string): BreadcrumbItemSegment {
    return {
      title: item.title,
      icon: item.icon,
      path: path
    };
  }

  useEffect(() => {
    if (!router.isReady)
      return;

    const path = router.asPath;
    const segments = [...path.split("/").filter(segment => segment.length !== 0), ""]; //hack

    let currPath = "/";
    let node = props.segmentMap;
    let newItems = []

    for (const segment of segments) {
      newItems.push(createItemSegment(node, currPath));
      currPath += segment;
      currPath += "/";

      if (node.children === undefined)
        break;
      node = node.children[segment];
      if (node === undefined)
        break;
    }

    setItems(newItems);
  }, [router.asPath]);

  function pushItem(item: BreadcrumbItem) {
    setItems([...items, createItemSegment(item, router.asPath)]);
  }

  function replaceItem(item: BreadcrumbItem) {
    setItems([...items.slice(0, -1), createItemSegment(item, router.asPath)]);
  }

  function modifyLastItem(newItem: BreadcrumbItem) {
    if (items.findLast(item => item.path === router.asPath))
      replaceItem(newItem);
    else
      pushItem(newItem);
  }

  useEffect(() => {
    props.setHandle?.({
      push: pushItem,
      replace: replaceItem,
      modify: modifyLastItem
    });
  }, [items, router.asPath]);

  function handleClick(item: BreadcrumbItemSegment) {
    router.push(item.path);
  }

  return (
    <Breadcrumbs sx={{ height: "40px" }}>
      {
        items.map((item, index) => (
          <Button key={index} startIcon={item.icon?.()} onClick={_ => handleClick(item)}>
            {item.title}
          </Button>
        ))
      }
    </Breadcrumbs>
  );
}
